import pytest

pytestmark = [
    pytest.mark.requires_salt_modules("aws_management.example_function"),
]


@pytest.fixture
def aws_management(modules):
    return modules.aws_management


def test_replace_this_this_with_something_meaningful(aws_management):
    echo_str = "Echoed!"
    res = aws_management.example_function(echo_str)
    assert res == echo_str
