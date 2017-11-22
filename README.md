### Very QuickStart
This is a cookiecutter template that enables the following:
* Consistent and standard project layout including 
    * default tests and project code
    * .gitignore
    * .editorconfig
* BumpVersion Configuration
* Tox automation for test and build
* Pytest for unittesting
* Flake8 for linting and style
* Sphinx documentation is generated with all the normal stubs and is buildable

Using this template ensures all your projects have the same structure and your
tooling is correctly setup and ready to go. It also provides the tools
necessary to test on various version of python and lets you start devloping
the project right away rather than spend time setting up your file system.

#### Pre-reqs:
`pip install cookiecutter`  
`pip install tox`

#### Get Project Template
`git clone https://github.com/AllenInstitute/pyproject_template.git`

#### Set Basic Defaults
Edit `pyproj_template/user_config.yaml` and replace / add / remove any values
corresponding to keys in cookiecutter.json that you want.

#### Create a new project
`cookiecutter -user-config <path-to>/pyproject_template/user_config.yaml <path-to>/pyproject_template`

#### Project configuration
Currently the main configuration will probably be the 
* tox.ini file which defines the environments you want to build against
* your requirements.txt - though that will change frequently
* possibly .bumpversion.cfg

To use, simply run <code>tox</code> to test your builds.
