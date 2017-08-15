# -*- coding: utf-8 -*-

import sys
import os
import logging.config
import yaml


__author__ = """{{ cookiecutter.full_name }}"""
__email__ = '{{ cookiecutter.email }}'
__version__ = '{{ cookiecutter.version }}'


def init_log(log_config_file=None):
    """
    Standard log initialization boiler plate that attempts to find a configuration file
    from the log_config_file variable, then the LOG_CONFIG_FILE environment variable. If
    neither file exists, it sets a basic DEBUG  console logger as the default.

    If the log is initialized at the __main__ level, all modules using logging downstream
    will pick up this configuration.

    :param log_config_file: The filename of a yaml based log configuration file.
    """
    if log_config_file is None:
        log_config_file = os.getenv('LOG_CONFIG_FILE', f'{__path__[0]}/resources/logging.yml')

    if os.path.exists(log_config_file):
        with open(log_config_file) as f:
            config = yaml.safe_load(f)
        config['handlers']['file_handler']['filename'] = sys.argv[0] + '.log'
        config['handlers']['debug_file_handler']['filename'] = sys.argv[0] + '_debug.log'
        logging.config.dictConfig(config)

    else:
        logging.basicConfig(level=logging.DEBUG)
        logging.warning(f'could not find {log_config_file}.  Using default configuration.')
