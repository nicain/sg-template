#!/usr/bin/env python
import os
import shutil
import json
import ruamel.yaml as yaml
import textwrap
from subprocess import call
import textwrap
from io import StringIO

MAX_WIDTH = 4096
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
COOKIECUTTER_CONFIG_DIR = os.path.join(PROJECT_DIRECTORY, '.cookiecutter')

def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def get_splash_text():
    
    buf = StringIO()

    buf.write(unicode("="*80+"\n"))

    txt = "Thanks for using the AIBS cookiecutter python project template."
    buf.write(unicode( "\n".join(textwrap.wrap(txt, width=80)) +"\n"))

    buf.write(unicode("\nLicense:"+"\n"))
    txt = "Your project is currently unlicensed (i.e. does not have a LICENSE file in the repository). If you would like to publicly release this code, you will need to submit your project to Innovation Central (http://ai/Legal/Innovation/SitePages/Home.aspx).  For more information on code release policies and procedures, check out http://confluence.corp.alleninstitute.org/display/PP/Github+FAQ"
    buf.write(unicode( "\n".join(textwrap.wrap(txt, width=80)) +"\n"))

    buf.write(unicode("\nContributing:"+"\n"))
    txt = "Your public facing project should have a statement about what level of support users should expect. Here are 4 example suggestions about a level of support notification you could include on your github repo; by default the first example (no expectation of support) is included in README.md, but feel free to customize:"
    buf.write(unicode( "\n".join(textwrap.wrap(txt, width=80, replace_whitespace=False)) +"\n"))

    txt = """
        1. We are not currently supporting this code, but simply releasing it to the community AS IS but are not able to provide any guarantees of support.  The community is welcome to submit issues, but you should not expect an active response.

        2. We are planning on occasional updating this tool with no fixed schedule. Community involvement is encouraged through both issues and pull requests.

        3. This code is an important part of the internal Allen Institute code base and we are actively using and maintaining it. Issues are encouraged, but because this tool is so central to our mission pull requests might not be accepted if they conflict with our existing plans.

        4. We are releasing this code to the public as a tool we expect others to use. Issues are welcomed and we expect to address them promptly, pull requests will vetted by our staff before inclusion.
    """

    buf.write(unicode( "\n".join(textwrap.wrap(txt, width=80, replace_whitespace=False, initial_indent='    ', subsequent_indent='    ')) +"\n"))

    buf.write(unicode("="*80))

    return str(buf.getvalue())

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

    # # Download aibs_sphinx templating files:
    # return_code = call('git clone https://github.com/AllenInstitute/aibs_sphinx.git', shell=True)
    # assert return_code == 0
    # shutil.rmtree(os.path.join('aibs_sphinx', '.git'))
    # if os.path.exists(os.path.join('docs', 'aibs_sphinx')):
    #     shutil.rmtree(os.path.join('docs', 'aibs_sphinx'))
    # shutil.move( 'aibs_sphinx', 'docs')

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

    print(get_splash_text())