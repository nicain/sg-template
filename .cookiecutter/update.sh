#!/bin/bash
set -e

PROJECT_DIR=$(pwd)/..

pip install --upgrade --force git+https://github.com/nicain/cookiecutter@1029 # Hack until https://github.com/audreyr/cookiecutter/pull/1030 is merged
python update_from_repo.py

# Add post-cookiecutter commands that you always want run here:
git checkout -- $PROJECT_DIR/README.md
git checkout -- $PROJECT_DIR/AUTHORS.rst
git checkout -- $PROJECT_DIR/Pipfile
git checkout -- $PROJECT_DIR/tox.ini
git checkout -- $PROJECT_DIR/.cookiecutter/update.sh
git checkout -- $PROJECT_DIR/Makefile

# Enter patch mode on remaining diffs:
git add -p
