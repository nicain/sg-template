from fabric.api import *

env.hosts = 'aibspi@aibspi'

project_name = '{{ cookiecutter.project_slug }}'
__version__ = '{{ cookiecutter.version }}'

def publish():

    local_path = f'dist/{project_name}-{__version__}/dist/*'
    package_path = 'python_index/{project_name}/'
    with settings(warn_only=True):
        run(f'mkdir {package_path}')
    put(local_path, package_path)

def publish_docs():
    local_path = f'docs/_build/html/*'
    package_path = 'python_index/docs/{project_name}/'
    with settings(warn_only=True):
        run(f'mkdir -p {package_path}')
    put(local_path, package_path)


