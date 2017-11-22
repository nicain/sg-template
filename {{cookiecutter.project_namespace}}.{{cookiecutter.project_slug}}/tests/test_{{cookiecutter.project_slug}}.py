#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_{{ cookiecutter.project_slug }}
----------------------------------

Tests for `{{ cookiecutter.project_slug }}` module.
"""
import pytest


@pytest.fixture
def decorated_example():
    """Sample pytest fixture.
    See more at: http://doc.pytest.org/en/latest/fixture.html
    """

def test_example(decorated_example):
    """Sample pytest test function with the pytest fixture as an argument.
    """
    import {{cookiecutter.project_namespace}}.{{cookiecutter.project_slug}}
    from {{cookiecutter.project_namespace}} import {{cookiecutter.project_slug}}




