import pytest

pytestmark = [
    pytest.mark.requires_salt_states("aws_management.exampled"),
]


@pytest.fixture
def aws_management(states):
    return states.aws_management


def test_replace_this_this_with_something_meaningful(aws_management):
    echo_str = "Echoed!"
    ret = aws_management.exampled(echo_str)
    assert ret.result
    assert not ret.changes
    assert echo_str in ret.comment
