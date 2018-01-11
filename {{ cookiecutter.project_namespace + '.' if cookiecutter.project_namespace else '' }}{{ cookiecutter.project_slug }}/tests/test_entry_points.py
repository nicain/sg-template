from . import entrypoint_exists

DEFAULT_ENTRYPOINT = '{{ cookiecutter.project_namespace + '.' if cookiecutter.project_namespace else '' }}{{ cookiecutter.project_slug }}'

def test_default_entrypoint_installed():
    assert entrypoint_exists(DEFAULT_ENTRYPOINT)
