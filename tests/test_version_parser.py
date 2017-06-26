import pytest

from leak.version_parser import versions_split


def test_versions_split():
    pass


def test_wrong_versions_split():
    # too many dots
    assert versions_split('1.2.3.4') == [0, 0, 0]

    # test missing numeric version
    with pytest.raises(ValueError):
        versions_split('not.numeric')

    # test not string provided
    with pytest.raises(AttributeError):
        versions_split(12345)
