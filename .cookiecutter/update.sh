PROJECT_DIR=$(pwd)/..

cookiecutter https://github.com/nicain/pyproject_template -o ../.. --config-file .cookiecutter.yaml --no-input --overwrite-if-exists --checkout 25

# Add post-cookiecutter commands that you always want run here:
rm -r $PROJECT_DIR/tests
rm -r $PROJECT_DIR/aibs
rm -r $PROJECT_DIR/tox.ini
rm -r $PROJECT_DIR/test_requirements.txt
rm -r $PROJECT_DIR/requirements_dev.txt
rm -r $PROJECT_DIR/setup.py

git checkout -- $PROJECT_DIR/README.md
git checkout -- $PROJECT_DIR/AUTHORS.rst
git checkout -- $PROJECT_DIR/requirements.txt
git checkout -- $PROJECT_DIR/.bumpversion.cfg
git checkout -- $PROJECT_DIR/setup.cfg
git checkout -- $PROJECT_DIR/MANIFEST.in

# Enter patch mode on remaining diffs:
git add -p