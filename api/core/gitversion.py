#!/usr/bin/env python
#
# Code inspired by:
# https://github.com/warner/python-ecdsa/blob/9e21c3388cc98ba90877a1e4dbc2aaf66c67d365/setup.py#L33
#

import os
import subprocess
import re


def git_version():
    try:
        p = subprocess.Popen(["git", "describe",
                              "--tags", "--dirty", "--always"],
                             stdout=subprocess.PIPE)
    except EnvironmentError:
        return
    version = p.communicate()[0]
    if p.returncode != 0:
        return
    return version
