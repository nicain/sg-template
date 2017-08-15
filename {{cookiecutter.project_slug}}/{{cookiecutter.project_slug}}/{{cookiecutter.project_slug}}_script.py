# -*- coding: utf-8 -*-
import {{cookiecutter.project_slug}}
import logging


def main(args=None):
    {{cookiecutter.project_slug}}.init_log()
    logging.info(f'Starting {{cookiecutter.project_slug}}')
    return 0


if __name__ == "__main__":
    main()
