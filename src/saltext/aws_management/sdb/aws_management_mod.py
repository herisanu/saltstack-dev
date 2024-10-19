"""
Salt SDB module
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "aws_management"


def __virtual__():
    # To force a module not to load return something like:
    #   return (False, "The aws-management sdb module is not implemented yet")

    # Replace this with your own logic
    if "aws_management.example_function" not in __salt__:
        return False, "The 'aws_management' execution module is not available"
    return __virtualname__


def get(key, profile=None):
    """
    This example function should be replaced

    CLI Example:

    .. code-block:: bash

        salt '*' sdb.get "sdb://aws_management/foo"
    """
    profile = profile or {}
    return profile.get(key, key)
