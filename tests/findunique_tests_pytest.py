import pytest
from findunique import CountUnique

cases = [
    ("asasdasd asdasd kjm", 3),
    ("asasdasd asdasd", 1),
    ("12345 6789a", 11),
    ("@^%#$^", 4),
    ("", 0),
]


def test_findunique_success():
    c = CountUnique()
    for text, count_unique_symbols in cases:
        assert c.count(text) == count_unique_symbols


def test_findunique_cache():
    c = CountUnique()
    hits = c.count.cache_info()[0]
    c.count("asasdasd asdasd kjm")
    c.count("asasdasd asdasd")
    c.count("asasdasd asdasd kjm")
    assert c.count.cache_info()[0] == hits + 1


def test_findunique_exception_empty_param():
    c = CountUnique()
    with pytest.raises(TypeError):
        c.count()


def test_findunique_exception_int_param():
    c = CountUnique()
    with pytest.raises(TypeError):
        c.count(123)
