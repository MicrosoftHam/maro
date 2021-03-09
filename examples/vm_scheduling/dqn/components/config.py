# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

"""
This file is used to load the configuration and convert it into a dotted dictionary.
"""

import io
import os

import yaml


CONFIG_PATH = os.path.join(os.path.split(os.path.realpath(__file__))[0], "../experiment/configs/combine_net/config.yml")
with io.open(CONFIG_PATH, "r") as in_file:
    config = yaml.safe_load(in_file)

