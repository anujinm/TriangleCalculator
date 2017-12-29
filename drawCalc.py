from math import cos


def center(Area, a, b, c, gamma, beta):
    A = 2 * Area / a
    B = c * cos(beta)
    C = b * cos(gamma)

    x = (B+C) / 2
    y = (A**2 + B * C) / 2 / A

    return [x, y]

