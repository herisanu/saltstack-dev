import pytest
import salt.modules.test as testmod

import saltext.aws_management.modules.aws_management_mod as aws_management_module


@pytest.fixture
def configure_loader_modules():
    module_globals = {
        "__salt__": {"test.echo": testmod.echo},
    }
    return {
        aws_management_module: module_globals,
    }


def test_replace_this_this_with_something_meaningful():
    echo_str = "Echoed!"
    assert aws_management_module.example_function(echo_str) == echo_str
