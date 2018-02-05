from setuptools import setup, find_packages

setup(
    name = 'aibs.pyproject_template',
    version = '0.1.0',
    description = """This is a cookiecutter template. Using this template ensures all your projects have the same structure and your tooling is correctly setup and ready to go. It also provides the tools necessary to test on various version of python and lets you start devloping the project right away rather than spend time setting up your file system.""",
    author = "Jed Perkins",
    author_email = "jedp@alleninstitute.org",
    url = 'https://github.com/AllenInstitute/pyproject_template/',
    packages = find_packages(),
    include_package_data=True,
    entry_points={
          'console_scripts': [
              'aibs.pyproject_template = aibs.pyproject_template.__main__:main'
        ]
    },
    setup_requires=['pytest-runner'],
)
