from . import entrypoint_exists

def test_default_entrypoint_installed():
    default_entrypoint = 'aibs.pyproject_template'
    assert entrypoint_exists(default_entrypoint)

