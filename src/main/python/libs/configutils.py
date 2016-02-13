#!/usr/bin/env python
# vim: tabstop=4:shiftwidth=4:expandtab:
from __future__ import with_statement

import argparse
import ConfigParser
import gettext
import logging
import os
from os.path import dirname, realpath  # for library path manipulation
import sys

# For translations
i18n = gettext.translation('', '{}/../i18n'.format(dirname(realpath(__file__))), fallback = True)
_ = i18n.lgettext

__author__ = "Travis Goldie"
__email__ = "tgoldie@gmail.com"
__copyright__ = "(c) Beeryard Tech 2016"

__log__ = logging.getLogger(__name__)


def main(args):
    pass


def add_args(current_dir, args):
    """ Add arguments to parser. Return new parser """
    parser = argparse.ArgumentParser(prog = args[0], prefix_chars = '-')

    parser.add_argument(
        "-d",
        "--debug",
        action = "store_true",
        default = None,
        help = _("add debug information to the output, default  =  False"),
        required = False,
    )

    parser.add_argument(
        "--config",
        # This is the only default defined here
        default = "{}/dbdiff.ini".format(current_dir),
        help = _("Path to config file."),
    )

    parser.add_argument(
        "-q",
        "--quiet",
        action = "store_true",
        default = None,
        help = _("Stop all logging. Only output data."),
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action = "store_true",
        default = None,
        help = _("make the output more verbose, default = False"),
        required = False,
    )

    return parser


def merge(configopts, argopts):
    """
    Merges the config options from the file and command line argumetns
    """
    config = {}
    for sect_name in configopts.sections():
        # secct_items is a list of tuples
        sect_items = dict(configopts.items(sect_name))
        config.update(sect_items)

    # Merge in argopts values
    for arg_key, arg_val in vars(argopts).items():
        config[arg_key] = arg_val

    return config


def merge_configs(config_path, argopts):
    """
    Loads and merges the configs
    """
    configopts = load_config(config_path)
    merge_result = merge(configopts, argopts)

    return merge_result


def load_config(config_path):
    """ Create config parser from file """
    config_parser = ConfigParser.ConfigParser()

    # Get config file
    if os.path.exists(config_path):
        config_parser.read(config_path)

    return config_parser


if __name__ == '__main__':
    main(sys.argv)
