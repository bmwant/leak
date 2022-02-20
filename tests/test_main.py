from unittest import mock

from leak import main


def test_wrong_package_name(capsys):

    with mock.patch(
        "leak.main.get_package_data", side_effect=ValueError
    ) as get_package_data_mock:
        main.main("wrong_package")
        get_package_data_mock.assert_called_once_with("wrong_package")

    out, err = capsys.readouterr()

    assert "No such package" in out
