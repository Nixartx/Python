import pytest
from findunique import CLCountUnique
from unittest.mock import patch, mock_open


def test_CLCountUniqueCase_string(capfd):
    CLCountUnique().run(['--string', 'asasdasd asdasd kjm'])
    expected = "Уникальных символов: 3\n"
    actual, err = capfd.readouterr()
    assert expected == actual


def test_CLCountUniqueCase_file(capfd):
    expected = "Строка: 1. Уникальных символов: 3\n"
    with patch('builtins.open', mock_open(read_data='asasdasd asdasd kjm')):
        CLCountUnique().run(['--file', 'path_to_file'])
        actual, err = capfd.readouterr()
        assert actual == expected


def test_CLCountUniqueCase_String_and_File(capfd):
    expected = "Строка: 1. Уникальных символов: 3\n"
    with patch('builtins.open', mock_open(read_data='asasdasd asdasd kjm')):
        CLCountUnique().run(['--file', 'path_to_file', '--string', 'abcd'])
        actual, err = capfd.readouterr()
        assert actual == expected

def test_CLCountUniqueCase_file_exception():
    #expected = "Error: File does not appear to exist."
    with pytest.raises(FileNotFoundError):
        CLCountUnique().run(['--file', 'abc'])
