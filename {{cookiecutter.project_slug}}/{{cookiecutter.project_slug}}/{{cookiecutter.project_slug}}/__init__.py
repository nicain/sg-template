# -*- coding: utf-8 -*-

import os
import logging.config
import yaml
import datetime
import shutil
import sys

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
        log_config_file = 'log_config_v1.yml'

    config = source_project_configuration(log_config_file)
    if config is None:
        logging.basicConfig(level=logging.DEBUG)
        logging.warning(f'could not find {log_config_file}.  Using default configuration.')
        return

    config['handlers']['file_handler']['filename'] = sys.argv[0] + '.log'
    config['handlers']['debug_file_handler']['filename'] = sys.argv[0] + '_debug.log'
    logging.config.dictConfig(config)


def parse_config(configuration_file):
    """
    FileExists and YAML checking boilerplate
    :param configuration_file:
    :return:
    """
    try:
        with open(configuration_file) as f:
            return yaml.safe_load(f)
    except FileNotFoundError as err:
        logging.warning(f'configuration not found: {configuration_file}')
        return None


def cache_remote_config(configuration_file):
    """
    Creates a back up of the local configuration and copies the remote configuration into the project path
    :param configuration_file:
    :return:
    """
    local_path = f'{__path__[0]}/resources/{configuration_file}'
    remote_path = f'{os.getenv("MPE_CONFIGURATION_PATH", "//allen/aibs/mpe/Rigs/configuration")}/{configuration_file}'

    logging.info('caching remote configuration')
    if os.path.exists(local_path):
        timestamp = datetime.datetime.strftime(datetime.datetime.now(), '%y%m%d-%H%M%S')
        backup_file = f'{local_path}.{timestamp}.bck'
        logging.info(f'Copying previous configuration to {backup_file}')
        shutil.copyfile(local_path, backup_file)

    shutil.copyfile(remote_path, local_path)


def source_project_configuration(configuration_file, override_local=True):
    """
    Find a project configuration file on the network, compare it to the local configuration and cache it.
    :param configuration_file:  Name of the configuration file
    :param override_local:  Default==True.  If true, overwrite the local configuration with the remote configuration
        if the remote configuration is newer.  The old local configuration is copied to <configuration_file.yml.old>
    :return: A dict corresponding to the programs configuration file
    """
    local_path = f'{__path__[0]}/resources/{configuration_file}'
    remote_path = f'{os.getenv("MPE_CONFIGURATION_PATH", "//allen/aibs/mpe/Rigs/configuration")}/{configuration_file}'

    local_config = parse_config(local_path)
    remote_config = parse_config(remote_path)

    if not local_config and not remote_config:
        raise FileNotFoundError('no valid configurations found.')

    if not remote_config or not override_local:
        return local_config

    if not local_config:
        cache_remote_config(configuration_file)
        return remote_config

    local_modify_time = os.path.getmtime(local_path)
    remote_modify_time = os.path.getmtime(remote_path)
    if remote_modify_time > local_modify_time:
        cache_remote_config(configuration_file)

    return remote_config
