# !/usr/bin/env python

from distutils.core import setup
setup(
    name='{{ cookiecutter.project_slug }}',
    packages=[],
    version='{{ cookiecutter.version }}',
    description='{{ cookiecutter.project_slug }}',
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    license="{{ cookiecutter.open_source_license }}",
    author_email='{{ cookiecutter.email }}',
    url='/{{ cookiecutter.stash_url }}',
    keywords=['{{ cookiecutter.project_slug }}'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development',
    ],
)
