#!/usr/bin/env python
# -*- coding: utf-8 -*-
import {{cookiecutter.project_slug}}
import logging


def main(args=None):
    {{cookiecutter.project_slug}}.init_log()
    {{cookiecutter.project_slug}}.source_project_configuration('{{cookiecutter.project_slug}}_config_v1.yml')
    logging.info(f'Starting {{cookiecutter.project_slug}}')


if __name__ == "__main__":
    main()
