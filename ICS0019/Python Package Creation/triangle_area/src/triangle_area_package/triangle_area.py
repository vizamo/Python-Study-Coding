"""Project for finding triangle area"""


def triangle_area(b: float, h: float):
    """
    Simple function that finds area of triangle.
    Function inputs are: base b and height h.
    Function returns the area S.
    """
    if b <= 0 or h <= 0:
        return "Negative values are not allowed"
    else:
        s = (h * b)/2
        return s

