from findunique.collect_framework import CLCountUnique
from unittest import mock

def test_CLCountUniqueCase_string(capfd):
        CLCountUnique().run(['--string', 'asasdasd asdasd kjm'])
        expected="Уникальных символов: 3\n"
        actual, err= capfd.readouterr()
        assert expected==actual

def test_CLCountUniqueCase_file(capfd):
    # expected = 5
    # actual = CLCountUnique().run(['--file', 'path_to_file'])
    # assert expected == actual
    pass