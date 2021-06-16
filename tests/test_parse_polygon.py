import pytest
import numpy as np

from bbdraw.polygon import parse_polygon


def test_tuple_list_of_integers():
    coordinates = [(0, 3), (1, 4), (4, 5)]

    expected = coordinates.copy()
    actual = parse_polygon(coordinates)

    assert actual.vertices == expected


def test_tuple_list_of_floats():
    coordinates = [(0.1, 3.3), (1.7, 4.1), (4.2, 5.9)]

    expected = [(0, 3), (1, 4), (4, 5)]
    actual = parse_polygon(coordinates)

    assert actual.vertices == expected


def test_tuple_list_bad_type():
    coordinates = [(0.1, 3.3), ("ladida", 4.1), (4.2, 5.9)]

    with pytest.raises(ValueError):
        parse_polygon(coordinates)


def test_tuple_list_too_many_dimensions():
    coordinates = [(0, 3, 1), (1, 4, 0), (4, 5, 2)]
    with pytest.raises(ValueError):
        parse_polygon(coordinates)


def test_2d_array_of_integers():
    coordinates = np.array([[0, 3], [1, 4], [4, 5]])

    expected = [(0, 3), (1, 4), (4, 5)]
    actual = parse_polygon(coordinates)

    assert actual.vertices == expected


def test_2d_array_of_floats():
    coordinates = np.array([[0.1, 3.3], [1.7, 4.1], [4.2, 5.9]])

    expected = [(0, 3), (1, 4), (4, 5)]
    actual = parse_polygon(coordinates)

    assert actual.vertices == expected


def test_3d_array_of_floats():
    coordinates = np.array([[[0.1, 3.3], [1.7, 4.1], [4.2, 5.9]],
                            [[0.1, 3.3], [1.7, 4.1], [4.2, 5.9]]])

    with pytest.raises(ValueError):
        parse_polygon(coordinates)


def test_flat_list_of_integers():
    coordinates = [0, 3, 1, 4, 4, 5]

    expected = [(0, 3), (1, 4), (4, 5)]
    actual = parse_polygon(coordinates)

    assert actual.vertices == expected


def test_flat_list_of_floats():
    coordinates = [0.1, 3.3, 1.7, 4.1, 4.2, 5.9]

    expected = [(0, 3), (1, 4), (4, 5)]
    actual = parse_polygon(coordinates)

    assert actual.vertices == expected


def test_flat_list_bad_type():
    coordinates = [0.1, 3.3, 1.7, 4.1, "ladida", 5.9]
    with pytest.raises(ValueError):
        parse_polygon(coordinates)


def test_flat_list_odd_number_of_entries():
    coordinates = [0, 3, 1, 4, 4, 5, 0]
    with pytest.raises(ValueError):
        parse_polygon(coordinates)


def test_flat_array_of_integers():
    coordinates = np.array([0, 3, 1, 4, 4, 5])

    expected = [(0, 3), (1, 4), (4, 5)]
    actual = parse_polygon(coordinates)

    assert actual.vertices == expected







