### Very QuickStart

#### Pre-reqs:
<pre>`pip install cookiecutter`
`pip install tox`</pre>

#### Get Project Template
`git clone http://rossh@stash.corp.alleninstitute.org/scm/~rossh/pyproj_template.git`

#### Set Basic Defaults
Edit `pyproj_template/user_config.yml` and replace / add / remove any values you want.

#### Create a new project
`cookiecutter -user-config <path-to>/pyproject_template/user_config.yml <path-to>/pyproject_template`
