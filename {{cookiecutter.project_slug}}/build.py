import glob
import os

from fabric.api import run, env, settings, put
from pybuilder.core import use_plugin, init, task, Author

# plugins
use_plugin('python.distutils')
use_plugin('python.core')
use_plugin('python.install_dependencies')
use_plugin('python.sphinx')
use_plugin('python.flake8')
use_plugin('pybuilder_pytest')

# pybuilder_pytest runs even without a task
default_task = ['install_dependencies',
                'analyze',
                'sphinx_generate_documentation',
                'publish']

# project meta
name = '{{ cookiecutter.project_slug }}'
version = '{{ cookiecutter.version }}'
summary = '{{ cookiecutter.project_short_description }}'
description = __doc__
authors = (Author('{{ cookiecutter.full_name }}', '{{ cookiecutter.email }}'),)
url = '{{ cookiecutter.stash_url }}'


@task(description='deploy project to aibspi')
def deploy():
    """
    Pushes the most recent package and documentation to the aibspi server.

    """
    env.host_string = 'aibspi'
    env.user = 'aibspi'
    env.password = 'aibspi'

    local_path = f'dist/{name}-{version}/dist/*'
    package_path = f'python_index/{name}/'
    with settings(warn_only=True):
        run(f'mkdir {package_path}')
    put(local_path, package_path)

    local_path = f'docs/_build/html/*'
    package_path = f'python_index/docs/{name}-{version}/'
    with settings(warn_only=True):
        run(f'mkdir -p {package_path}')
    put(local_path, package_path)


@init(environments='deploy')
def initialize_deploy(logger):
    """
    Causes the deploy task to run after the default tasks.
    :param logger: PyBuilder Logger
    """
    deploy(logger)


@init
def initialize(project):
    project.set_property('verbose', True)

    # modules / di  st
    project.set_property('dir_source_main_python', '{{ cookiecutter.project_slug }}')
    project.set_property('dir_source_main_scripts', 'scripts')
    project.set_property('dir_dist', 'dist/{0}-{1}'.format(name, version))

    # testing
    project.set_property('dir_source_pytest_python', "tests")

    # documentation
    project.set_property('dir_docs', 'docs')
    project.set_property('sphinx_config_path', 'docs/')
    project.set_property('sphinx_source_dir', 'docs/')
    project.set_property('sphinx_output_dir', 'docs/_build/html')
    project.set_property('sphinx_builder', 'html')

    # linting
    project.set_property('flake8_break_build', False)
    project.set_property('flake8_include_scripts', True)
    project.set_property('flake8_include_test_sources', True)

    # dependencies
    project.build_depends_on_requirements('requirements_dev.txt')
    project.depends_on_requirements('requirements.txt')

    # entry points (typically the .py files in {{ cookiecutter.project_slug }}
    project.set_property('distutils_entry_points',
                         {'console_scripts': [
                             '{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}_script:main',
                             '{{ cookiecutter.project_slug }}_post_install={{ cookiecutter.project_slug }}_post_install:main',
                             '{{ cookiecutter.project_slug }}_uninstall={{ cookiecutter.project_slug }}_uninstall:main']})

    resources = glob.glob('limstk/limstk/resources/*')
    for resource in resources:
        project.include_file('limstk', 'resources/' + os.path.basename(resource))
