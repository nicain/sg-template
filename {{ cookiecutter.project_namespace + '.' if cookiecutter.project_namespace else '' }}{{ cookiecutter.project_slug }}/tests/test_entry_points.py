from . import entrypoint_exists

def test_default_entrypoint_installed():
    default_entrypoint = '{{ cookiecutter.project_namespace + '.' if cookiecutter.project_namespace else '' }}{{ cookiecutter.project_slug }}'
    assert entrypoint_exists(default_entrypoint)

