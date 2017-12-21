import sys
import textwrap
import os

base_dir = os.path.dirname(__file__)
splash_file_name = os.path.join(base_dir, '..','{{ cookiecutter.project_namespace + \'.\' if cookiecutter.project_namespace else \'\' }}{{ cookiecutter.project_slug }}','docs','splash.txt')

sys.stdout = open(os.path.abspath(splash_file_name), 'w')

print("="*80)

txt = "Thanks for using the AIBS cookiecutter python project template."
print( "\n".join(textwrap.wrap(txt, width=80)) )

print("\nLicense:")
txt = "Your project is currently unlicensed (i.e. does not have a LICENSE file in the repository). If you would like to publicly release this code, you will need to submit your project to Innovation Central (http://ai/Legal/Innovation/SitePages/Home.aspx).  For more information on code release policies and procedures, check out http://confluence.corp.alleninstitute.org/display/PP/Github+FAQ"
print( "\n".join(textwrap.wrap(txt, width=80)) )

print("\nContributing:")
txt = "Your public facing project should have a statement about what level of support users should expect. Here are 4 example suggestions about a level of support notification you could include on your github repo; by default the first example (no expectation of support) is included in README.md, but feel free to customize:"
print( "\n".join(textwrap.wrap(txt, width=80, replace_whitespace=False)) )

txt = """
    1. We are not currently supporting this code, but simply releasing it to the community AS IS but are not able to provide any guarantees of support.  The community is welcome to submit issues, but you should not expect an active response.

    2. We are planning on occasional updating this tool with no fixed schedule. Community involvement is encouraged through both issues and pull requests.

    3. This code is an important part of the internal Allen Institute code base and we are actively using and maintaining it. Issues are encouraged, but because this tool is so central to our mission pull requests might not be accepted if they conflict with our existing plans.

    4. We are releasing this code to the public as a tool we expect others to use. Issues are welcomed and we expect to address them promptly, pull requests will vetted by our staff before inclusion.
"""

print( "\n".join(textwrap.wrap(txt, width=80, replace_whitespace=False, initial_indent='    ', subsequent_indent='    ')) )

print("="*80)