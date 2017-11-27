#!/usr/bin/env python
import os
import json
import ruamel.yaml as yaml

MAX_WIDTH = 4096
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

if __name__ == '__main__':
    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    # Read the json file generated from the user input:
    config_file_name_read = os.path.join(PROJECT_DIRECTORY, '.cookiecutter.json')
    cookiecutter_json = json.load(open(config_file_name_read, 'r'))

    # Pop off the _template; this was not input by the user
    cookiecutter_json.pop('_template')
    
    # Write back out to a yaml file compatible with --config-file command line option
    config_file_name_write = os.path.join(PROJECT_DIRECTORY, '.cookiecutter.yaml')
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
