import tempfile
import os
import inspect

from cookiecutter.main import cookiecutter as cc
import py, pytest
from . import configs

template_dir = os.path.join(os.path.dirname(__file__), '..')

@pytest.fixture(scope='function')
def tmpdir(request):
    """
    Get a temp dir to build in
    """

    dir = py.path.local(tempfile.mkdtemp())
    request.addfinalizer(lambda: dir.remove(rec=True))

    return dir


config_dict = dict([(x[0], x[1]) for x in inspect.getmembers(configs) if x[0][-7:] == "_config"])
@pytest.fixture(params=config_dict.keys())
def config_key(request):
    return request.param

def test_no_namespace(tmpdir, config_key):

    cc(template_dir,
        output_dir = str(tmpdir),
        extra_context = config_dict[config_key],
        no_input = True,
        overwrite_if_exists = True)
