from . import entrypoint_exists

DEFAULT_ENTRYPOINT = 'aibs.pyproject_template'

def test_default_entrypoint_installed():
    assert entrypoint_exists(DEFAULT_ENTRYPOINT)
