#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':
    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    home_path = os.path.expanduser('~')

    create_python_envs = {{ cookiecutter.create_python_environments }}

    if create_python_envs:
        python27_path = '{{ cookiecutter.python27_path}}'
        python36_path = '{{ cookiecutter.python36_path}}'
        if not os.path.exists(f'{python27_path}'):
            print(f'Creating new Python 2.7 environment for tox: {python27_path}')
            os.system(f'conda create -p {python27_path} python=2.7 -y')
        if not os.path.exists(f'{python36_path}'):
            print(f'Create new Python 3.6 environment for tox: {python36_path}')
            os.system(f'conda create -p {python36_path} python=3.6 -y')
        if not os.path.exists('{python27_path}'.format(python27_path=python27_path)):
            print('Creating new Python 2.7 environment for tox: {python27_path}'.format(python27_path=python27_path))
            os.system('conda create -p {python27_path} python=2.7 -y'.format(python27_path=python27_path))
        if not os.path.exists('{python36_path}'.format(python36_path=python36_path)):
            print('Create new Python 3.6 environment for tox: {python36_path}'.format(python36_path=python36_path))
            os.system('conda create -p {python36_path} python=3.6 -y'.format(python36_path=python36_path))
    else:
        print('Not creating environments for Tox.  You may need to modify tox.ini for tox to function correctly')

    create_project_env = {{ cookiecutter.create_project_env }}
    if create_project_env:
        project_env = '{{ cookiecutter.project_slug }}'
        print(f'Creating project environment: {project_env}')
        os.system(f'conda create --name {project_env} python=3.6 -y')
        print('Creating project environment: {project_env}'.format(project_env=project_env))
        os.system('conda create --name {project_env} python=3.6 -y'.format(project_env=project_env))

    print('After activating your development environment, run `pip install -r requirements_dev.txt`')
