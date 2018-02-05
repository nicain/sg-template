from setuptools import setup, find_packages

setup(
    name = '{{ cookiecutter.project_namespace + '.' if cookiecutter.project_namespace else '' }}{{ cookiecutter.project_slug }}',
    version = '{{ cookiecutter.version }}',
    description = """{{ cookiecutter.project_short_description }}""",
    author = "{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email = "{{ cookiecutter.email }}",
    url = '{{ cookiecutter.repo_url }}',
    packages = find_packages(),
    include_package_data=True,
    entry_points={
          'console_scripts': [
              '{{ cookiecutter.project_namespace + '.' if cookiecutter.project_namespace else '' }}{{ cookiecutter.project_slug }} = {{ cookiecutter.project_namespace + '.' if cookiecutter.project_namespace else '' }}{{ cookiecutter.project_slug }}.__main__:main'
        ]
    },
    setup_requires=['pytest-runner'],
)
