# !/usr/bin/env python

from distutils.core import setup
setup(
    name='{{ cookiecutter.project_name }}',
    packages=[],
    version='0.1.0',
    description='{{ cookiecutter.project_short_description }}',
    author='{{ cookiecutter.full_name }}',
    license='{{ cookiecutter.open_source_license }}',
    author_email='{{ cookiecutter.email }}',
    url='{{ cookiecutter.stash_url }}',
    keywords=['{{ cookiecutter.project_name }}', 'template', 'package', ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development',
    ],
)
