import pytest
import salt.modules.test as testmod

import saltext.aws_management.modules.aws_management_mod as aws_management_module
import saltext.aws_management.states.aws_management_mod as aws_management_state


@pytest.fixture
def configure_loader_modules():
    return {
        aws_management_module: {
            "__salt__": {
                "test.echo": testmod.echo,
            },
        },
        aws_management_state: {
            "__salt__": {
                "aws_management.example_function": aws_management_module.example_function,
            },
        },
    }


def test_replace_this_this_with_something_meaningful():
    echo_str = "Echoed!"
    expected = {
        "name": echo_str,
        "changes": {},
        "result": True,
        "comment": f"The 'aws_management.example_function' returned: '{echo_str}'",
    }
    assert aws_management_state.exampled(echo_str) == expected
