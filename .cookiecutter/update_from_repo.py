from cookiecutter.main import cookiecutter as cc
import ruamel.yaml as yaml

settings = yaml.load('./.cookiecutter.yaml')

cc(settings['_template'],
    output_dir="../..",
    config_file=".cookiecutter.yaml",
    no_input=True,
    overwrite_if_exists=True)
