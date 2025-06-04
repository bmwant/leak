from unittest.mock import patch

from leak import main


@patch("sys.exit")
def test_wrong_package_name(
    exit_mock,
    capsys,
):
    with patch(
        "leak.main.get_package_data", side_effect=ValueError
    ) as get_package_data_mock:
        main.main("wrong_package")
        get_package_data_mock.assert_called_once_with("wrong_package")

    out, err = capsys.readouterr()

    assert "No such package" in out
    exit_mock.assert_called_once_with(1)
