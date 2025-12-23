import pytest
from GitHub_Copilot import add


def test_add_integers():
    assert add(1, 2) == 3


def test_add_floats():
    assert add(1.5, 2.25) == pytest.approx(3.75)


def test_add_strings_concatenates():
    assert add("a", "b") == "ab"


def test_add_lists_concatenates():
    assert add([1, 2], [3]) == [1, 2, 3]


def test_add_non_compatible_raises_type_error():
    with pytest.raises(TypeError):
        add(1, "a")
