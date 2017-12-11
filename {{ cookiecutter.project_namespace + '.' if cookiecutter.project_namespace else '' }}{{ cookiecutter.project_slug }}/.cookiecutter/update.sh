#!/bin/bash
set -e

PROJECT_DIR=$(pwd)/..

cookiecutter https://github.com/AllenInstitute/pyproject_template -o ../.. --config-file .cookiecutter.yaml --no-input --overwrite-if-exists

# Add post-cookiecutter commands that you always want run here:
git checkout -- $PROJECT_DIR/README.md
git checkout -- $PROJECT_DIR/AUTHORS.rst
git checkout -- $PROJECT_DIR/requirements.txt

# Enter patch mode on remaining diffs:
git add -p
