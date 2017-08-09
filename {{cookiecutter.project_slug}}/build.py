from pybuilder.core import use_plugin, init, task, Author
from pybuilder.errors import BuildFailedException
import pytest
import os

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


@task(descript='fab_deploy')
def deploy(logger):
    logger.info('Publishing to AIBSPI')
    os.system('fab -p aibspi publish')
    os.system('fab -p aibspi publish_docs')


@init(environments='deploy')
def initialize_deploy(logger):
    deploy(logger)


@init
def initialize(project, logger):
    project.set_property('verbose', True)

    # modules / dist
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
                         {'console_scripts': ['{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}:main']})
