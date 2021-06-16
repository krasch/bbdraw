import pytest
import numpy as np

from bbdraw.polygon import parse_rectangle


def test_tuple_int():
    rectangle = [(0, 3), (1, 4)]

    expected = [(0, 3), (1, 3), (1, 4), (0, 4)]
    actual = parse_rectangle(rectangle).vertices

    assert actual == expected


def test_tuple_float():
    rectangle = [(0.2, 3.8), (1.1, 4.5)]

    expected = [(0, 3), (1, 3), (1, 4), (0, 4)]
    actual = parse_rectangle(rectangle).vertices

    assert actual == expected


def test_tuple_too_few_entries():
    rectangle = [(0, ), (1, )]
    with pytest.raises(ValueError):
        parse_rectangle(rectangle)


def test_tuple_too_many_entries():
    rectangle = [(0, 1, 2), (1, 2, 3)]
    with pytest.raises(ValueError):
        parse_rectangle(rectangle)


def test_tuple_wrong_type():
    rectangle = [(0, 1), (1, "ladida")]
    with pytest.raises(ValueError):
        parse_rectangle(rectangle)


def test_numpy_2D():
    rectangle = np.array([[0, 3], [1, 4]])

    expected = [(0, 3), (1, 3), (1, 4), (0, 4)]
    actual = parse_rectangle(rectangle).vertices

    assert actual == expected


def test_list_int():
    rectangle = [0, 3, 1, 4]

    expected = [(0, 3), (1, 3), (1, 4), (0, 4)]
    actual = parse_rectangle(rectangle).vertices

    assert actual == expected


def test_list_float():
    rectangle = [0.2, 3.8, 1.1, 4.5]

    expected = [(0, 3), (1, 3), (1, 4), (0, 4)]
    actual = parse_rectangle(rectangle).vertices

    assert actual == expected


def test_list_too_few_entries():
    rectangle = [0, 3, 1]

    with pytest.raises(ValueError):
        parse_rectangle(rectangle)


def test_list_too_many_entries():
    rectangle = [0, 3, 1, 2, 0]

    with pytest.raises(ValueError):
        parse_rectangle(rectangle)


def test_list_wrong_type():
    rectangle = [0, 1, 1, "ladida"]
    with pytest.raises(ValueError):
        parse_rectangle(rectangle)


def test_numpy_1D():
    rectangle = np.array([0, 3, 1, 4])

    expected = [(0, 3), (1, 3), (1, 4), (0, 4)]
    actual = parse_rectangle(rectangle).vertices

    assert actual == expected


