#!/usr/bin/env python
import os
import shutil
import json
import ruamel.yaml as yaml
import textwrap
from subprocess import call

MAX_WIDTH = 4096
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
COOKIECUTTER_CONFIG_DIR = os.path.join(PROJECT_DIRECTORY, '.cookiecutter')

def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

if __name__ == '__main__':

    # Read the json file generated from the user input:
    config_file_name_read = os.path.join(COOKIECUTTER_CONFIG_DIR, '.cookiecutter.json')
    cookiecutter_json = json.load(open(config_file_name_read, 'r'))
    
    # Write back out to a yaml file compatible with --config-file command line option
    config_file_name_write = os.path.join(COOKIECUTTER_CONFIG_DIR, '.cookiecutter.yaml')
    y = yaml.YAML()

    for key, val in cookiecutter_json.items():
        if len(val) >= MAX_WIDTH:
            raise Exception('Length of %s longer than MAX_WIDTH (%s)\n    See %s' (key, MAX_WIDTH, 'https://stackoverflow.com/questions/42170709/prevent-long-lines-getting-wrapped-in-ruamel-yaml'))

    y.width = 4096 # https://stackoverflow.com/questions/42170709/prevent-long-lines-getting-wrapped-in-ruamel-yaml https://bitbucket.org/ruamel/yaml/issues/108/dump-safe_dump-outputs-invalid-yaml
    y.dump({'default_context':cookiecutter_json}, open(config_file_name_write, 'w'))

    # mock in empy _static folder for documentation assets:
    static_asset_loc = os.path.join(PROJECT_DIRECTORY, 'docs', '_static')
    if not os.path.exists(static_asset_loc):
        os.mkdir(static_asset_loc)

    # Download aibs_sphinx templating files:
    return_code = call('git clone https://github.com/AllenInstitute/aibs_sphinx.git', shell=True)
    assert return_code == 0
    shutil.rmtree(os.path.join('aibs_sphinx', '.git'))
    if os.path.exists(os.path.join('docs', 'aibs_sphinx')):
        shutil.rmtree(os.path.join('docs', 'aibs_sphinx'))
    shutil.move( 'aibs_sphinx', 'docs')

    namespace = '{{ cookiecutter.project_namespace }}'
    slug = '{{ cookiecutter.project_slug }}'  

    # Determine the final directory location:
    if namespace:
        project_loc = '/'.join([namespace, slug])
    else:
        project_loc = slug
    
    if not os.path.exists(project_loc):
        
        # This is a new project
        shutil.move( 'to_slug', slug )

        if namespace:
            shutil.move( 'to_namespace', namespace )
            shutil.move( slug, namespace )
        else:
            shutil.rmtree( 'to_namespace' )

    else:

        # The project already exists, and this is a refresh:
        shutil.rmtree( 'to_namespace' )
        shutil.rmtree( 'to_slug' )

    splash_file_name = os.path.join(PROJECT_DIRECTORY, 'docs', 'splash.txt')
    with open(splash_file_name, 'r') as fin:
        print fin.read()