from setuptools import setup, find_packages

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

with open('test_requirements.txt','r') as f:
    test_requirements = f.read().splitlines()

setup(
    name = '{{ cookiecutter.project_namespace + '_' if cookiecutter.project_namespace else '' }}{{ cookiecutter.project_slug }}',
    version = '{{ cookiecutter.version }}',
    description = """{{ cookiecutter.project_short_description }}""",
    author = "{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email = "{{ cookiecutter.email }}",
    url = '{{ cookiecutter.repo_url }}',
    packages = find_packages(),
    include_package_data=True,
    install_requires = requirements,
    entry_points={
          'console_scripts': [
              '{{ cookiecutter.project_namespace + '.' if cookiecutter.project_namespace else '' }}{{ cookiecutter.project_slug }} = {{ cookiecutter.project_namespace + '.' if cookiecutter.project_namespace else '' }}{{ cookiecutter.project_slug }}.__main__:main'
        ]
    },
{%- if cookiecutter.open_source_license != 'Not open source' %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    setup_requires=['pytest-runner'],
    tests_require = test_requirements
)
