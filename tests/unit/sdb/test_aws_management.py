import pytest

import saltext.aws_management.sdb.aws_management_mod as aws_management_sdb


@pytest.fixture
def configure_loader_modules():
    module_globals = {
        "__salt__": {"this_does_not_exist.please_replace_it": lambda: True},
    }
    return {
        aws_management_sdb: module_globals,
    }


def test_replace_this_this_with_something_meaningful():
    assert "this_does_not_exist.please_replace_it" in aws_management_sdb.__salt__
    assert aws_management_sdb.__salt__["this_does_not_exist.please_replace_it"]() is True
