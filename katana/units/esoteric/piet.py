"""
Piet esoteric language

This unit will extract the text returned by a given
Piet language image using the npiet command-line
utility.

"""


import subprocess
from typing import Any

from katana.unit import FileUnit, NotApplicable


class Unit(FileUnit):

    # Groups we belong to
    GROUPS = ["esoteric", "npiet", "npiet"]

    # It would not make sense to recurse into ourself
    RECURSE_SELF = False

    # Binary dependencies
    DEPENDENCIES = ["npiet"]

    # Moderately high priority due to speed and broadness of applicability
    PRIORITY = 30

    def __init__(self, *args, **kwargs):
        super(Unit, self).__init__(*args, **kwargs, keywords=["image"])

    def evaluate(self, case: Any):

        # Run npiet against the image
        p = subprocess.Popen(
            ["npiet", self.target.path], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

        # Look for flags, add the results, and recurse on all output
        for line in p.stdout:
            self.manager.register_data(self, line)