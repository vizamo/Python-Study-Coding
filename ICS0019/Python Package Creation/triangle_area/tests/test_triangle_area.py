import pytest
from triangle_area_package import triangle_area as t
area = t.triangle_area


def test_area_int():
    assert area(100, 2) == 100, "Should be 100"


def test_area_minor_int_height():
    assert area(-10, 2) == "Negative values are not allowed", "Should be warning"


def test_area_minor_int_base():
    assert area(11, -232) == "Negative values are not allowed", "Should be warning"


def test_area_double_minor_int():
    assert area(-23, -2) == "Negative values are not allowed", "Should be warning"


def test_area_zero_int_height():
    assert area(0, 2) == "Negative values are not allowed", "Should be warning"


def test_area_zero_int_base():
    assert area(265, 0) == "Negative values are not allowed", "Should be warning"


def test_area_double_zero_int():
    assert area(0, 0) == "Negative values are not allowed", "Should be warning"


def test_huge_int():
    assert area(32145, 233132) == 3747014070, "Should be 3747014070"


def test_float():
    assert area(231.3546, 13224.745) == 1529802.7947885, "Should be 1529802.7947885"


if __name__ == '__main__':
    pytest.main()
