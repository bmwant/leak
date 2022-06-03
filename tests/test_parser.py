import pytest

from leak.parser import versions_split


def test_versions_split():
    assert versions_split("1.8.1") == [1, 8, 1]
    assert versions_split("1.4") == [1, 4, 0]
    assert versions_split("2") == [2, 0, 0]


def test_versions_split_str_mapping():
    assert versions_split("1.11rc1", type_applyer=str) == ["1", "11rc1", "0"]
    assert versions_split("1.10b1", type_applyer=str) == ["1", "10b1", "0"]
    assert versions_split("text", type_applyer=str) == ["text", "0", "0"]


def test_wrong_versions_split():
    # too many dots
    assert versions_split("1.2.3.4") == [0, 0, 0]

    # test missing numeric version
    with pytest.raises(ValueError):
        versions_split("not.numeric")

    # test not string provided
    with pytest.raises(AttributeError):
        versions_split(12345)
