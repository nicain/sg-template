### Very QuickStart
This is a cookiecutter template that enables the following:
* Consistent and standard project layout including 
    * default tests and project code
    * .gitignore
    * .editorconfig
* BumpVersion Configuration
* Tox automation for test and build
* Py.Test for unittesting
* Flake8 for linting and style
* Pybuilder for build and distribution which currently supports
    * Flake8
    * Py.Test
    * Dependencies
    * SetupTools - Sdist and Bdist
    * Sphinx Doc building
* Sphinx documentation is generated with all the normal stubs and is buildable

Using this template ensures all your projects have the same structure and your tooling is correctly 
setup and ready to go.  It also provides the tools necessary to test on various version of python and
lets you start devloping the project right away rather than spend time setting up your file system.

#### Pre-reqs:
<pre>`pip install cookiecutter`
`pip install tox`</pre>

#### Get Project Template
`git clone http://rossh@stash.corp.alleninstitute.org/scm/~rossh/pyproj_template.git`

#### Set Basic Defaults
Edit `pyproj_template/user_config.yml` and replace / add / remove any values you want.

#### Create a new project
`cookiecutter -user-config <path-to>/pyproject_template/user_config.yml <path-to>/pyproject_template`

#### Project configuration
Currently the main configuration will probably be the 
* tox.ini file which defines the environments you want to build against
* your requirements.txt - though that will change frequently
* possibly .bumpversion.cfg

build.py will be something that becomes more specific to your project structure as time goes on. 

To use, simply run <code>tox</code> to test your builds and <code>pyb</code> to create a distributable 
build.  On windows you will have to specifically point to the pyb script in your system by typing
<code>python path-to-python\scripts\pyb</code>

