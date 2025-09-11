import json

import pytest

from leak.parser import get_email, versions_split
from tests.conftest import DATA_DIR


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


@pytest.fixture
def package_data():
    def _get_package_data(package_name: str) -> dict:
        with open(DATA_DIR / f"{package_name}_package_data.json") as f:
            data = json.load(f)
        return data["info"]

    return _get_package_data


@pytest.fixture
def downloads_data():
    def _get_downloads_data(package_name: str) -> dict:
        with open(DATA_DIR / f"{package_name}_downloads_data.json") as f:
            data = json.load(f)
        return data

    return _get_downloads_data


@pytest.mark.parametrize(
    "package_name,expected_email",
    [
        ("django", "foundation@djangoproject.com"),
        ("pydantic", "s@muelcolvin.com"),
        ("typing_extensions", "Guido van Rossum"),  # FIXME: not an email
    ],
)
def test_get_email(package_name, expected_email, package_data):
    package_data = package_data(package_name)
    email = get_email(package_data)
    assert email == expected_email


def test_get_email_not_available():
    pass
