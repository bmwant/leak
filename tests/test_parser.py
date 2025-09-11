import pytest

from leak.parser import get_author, get_email, get_homepage, get_license, versions_split


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


@pytest.mark.parametrize(
    "package_name,expected_license",
    [
        ("django", "BSD-3-Clause"),
        ("pydantic", "MIT"),
        ("typing_extensions", "PSF-2.0"),  # FIXME: not an email
    ],
)
def test_get_license(package_name, expected_license, package_data):
    package_data = package_data(package_name)
    email = get_license(package_data)
    assert email == expected_license


@pytest.mark.parametrize(
    "package_name,expected_author",
    [
        ("django", "Django Software Foundation"),
        ("pydantic", "Samuel Colvin"),
        ("typing_extensions", ""),  # FIXME: wrong
    ],
)
def test_get_author(package_name, expected_author, package_data):
    package_data = package_data(package_name)
    author = get_author(package_data)
    assert author == expected_author


# TODO: Homepage to take priority from "project_url" field
@pytest.mark.parametrize(
    "package_name,expected_homepage",
    [
        ("django", "https://pypi.org/project/Django/"),
        ("pydantic", "https://pypi.org/project/pydantic/"),
        ("typing_extensions", "https://pypi.org/project/typing-extensions/"),
    ],
)
def test_get_homepage(package_name, expected_homepage, package_data):
    package_data = package_data(package_name)
    homepage = get_homepage(package_data)
    assert homepage == expected_homepage
