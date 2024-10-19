"""
Salt state module
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "aws_management"


def __virtual__():
    # To force a module not to load return something like:
    #   return (False, "The aws-management state module is not implemented yet")

    # Replace this with your own logic
    if "aws_management.example_function" not in __salt__:
        return False, "The 'aws_management' execution module is not available"
    return __virtualname__


def exampled(name):
    """
    This example function should be replaced
    """
    ret = {"name": name, "changes": {}, "result": False, "comment": ""}
    value = __salt__["aws_management.example_function"](name)
    if value == name:
        ret["result"] = True
        ret["comment"] = f"The 'aws_management.example_function' returned: '{value}'"
    return ret
