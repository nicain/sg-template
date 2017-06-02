from pybuilder.core import use_plugin, init, task, Author

# plugins
use_plugin('python.distutils')
use_plugin('python.core')
use_plugin('python.install_dependencies')
use_plugin('python.sphinx')
use_plugin('python.flake8')

# TODO - this works outside of pyb but not inside it ?
# use_plugin('python.unittest')

default_task = ['publish', 'install_build_dependencies', 'install_dependencies']

# project meta
name = '{{ cookiecutter.project_slug }}'
version = '{{ cookiecutter.version }}'
summary = '{{ cookiecutter.project_short_description }}'
description = __doc__
authors = (Author('{{ cookiecutter.full_name }}', '{{ cookiecutter.email }}'),)
url = '{{ cookiecutter.stash_url }}'

@task
def build_docs(project, logger):
    pass

@init
def initialize(project, logger):
    logger.info('Setting project properties.')

    # modules / dist
    project.set_property('dir_source_main_python', '{{ cookiecutter.project_slug }}')
    project.set_property('dir_source_main_scripts', 'scripts')
    project.set_property('dir_dist', 'dist/{0}-{1}'.format(name, version))

    # testing
    # project.set_property('dir_source_unittest_python', 'tests')
    # project.set_property('unittest_module_glob', 'test_*')

    # documentation
    project.set_property('dir_docs', 'docs')
    project.set_property('sphinx_config_path', 'docs/')
    project.set_property('sphinx_source_dir', 'docs/')
    project.set_property('sphinx_output_dir', 'docs/_build')
    project.set_property('sphinx_builder', 'html')

    # linting
    project.set_property('flake8_break_build', True)
    project.set_property('flake8_include_scripts', True)
    project.set_property('flake8_include_test_sources', True)

    # dependencies
    project.build_depends_on_requirements('requirements_dev.txt')
    project.depends_on_requirements('requirements.txt')


