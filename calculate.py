from math import sqrt, sin, cos, asin, pi


def calculate(a, b, c, alpha, beta, gamma):
    if a != 0 and b != 0 and c != 0:
        return threeSide(a, b, c)
    elif a != 0 and b != 0 and alpha != 0:
        return twoSideOneAngle(a, b, alpha)
    elif a != 0 and b != 0 and beta != 0:
        return twoSideOtherAngle(a, b, beta)
    elif a != 0 and b != 0 and gamma != 0:
        return twoSideInternalAngle(a, b, gamma)
    elif a != 0 and alpha != 0 and beta != 0:
        return twoAngleOneSide(a, alpha, beta)
    elif a != 0 and beta != 0 and gamma != 0:
        return two2AngleOneSide(a, beta, gamma)
    elif a != 0 and gamma != 0 and alpha != 0:
        return two3AngleOneSide(a, alpha, gamma)


def threeSide(x, y, z):
    p = (x + y + z) / 2
    S = sqrt(p*(p-x)*(p-y)*(p-z))
    R = x*y*z/(4*S)
    angleX = asin(x/(2*R))
    angleY = asin(y / (2 * R))
    angleZ = asin(z / (2 * R))
    return [x, y, z, angleX, angleY, angleZ, 2*p, S, R]


def twoSideInternalAngle(x, y, angleZ):
    z = sqrt(x**2 + y**2 - 2*x*y*cos(angleZ))
    twoR = z/sin(angleZ)
    angleX = asin(x/twoR)
    angleY = asin(y/twoR)
    P = x + y + z
    S = x * y * sin(angleZ) / 2
    return [x, y, z, angleX, angleY, angleZ, P, S, twoR/2]


def twoSideOneAngle(x, y, angleX):
    twoR = x/sin(angleX)
    angleY = asin(y/twoR)
    angleZ = pi - angleX - angleY
    z = sqrt(x**2 + y**2 - 2*x*y*cos(angleZ))
    P = x + y + z
    S = x * y * sin(angleZ) / 2
    return [x, y, z, angleX, angleY, angleZ, P, S, twoR/2]


def twoSideOtherAngle(x, y, angleY):
    r = twoSideOneAngle(y, x, angleY)
    return [r[1], r[0], r[2], r[4], r[3], r[5],  r[6],  r[7],  r[8]]


def twoAngleOneSide(x, angleX, angleY):
    twoR = x / sin(angleX)
    y = sin(angleY) * twoR
    return twoSideOneAngle(x, y, angleX)


def two2AngleOneSide(x, angleY, angleZ):
    angleX = pi - angleY - angleZ
    return twoAngleOneSide(x, angleX, angleY)


def two3AngleOneSide(x, angleX, angleZ):
    angleY = pi - angleX - angleZ
    return twoAngleOneSide(x, angleX, angleY)


# degrees = 180/pi
#
# result = calculate(a, b, c, alpha, beta, gamma)
#
# print("Perimeter a: " + str(result[0]))
# print("Area a: " + str(result[1]))
# print("Radius a: " + str(result[2]))
# print("Angle A: " + str(result[3] * degrees))
# print("Angle B: " + str(result[4] * degrees))
# print("Angle C: " + str(result[5] * degrees))
# print("Side a: " + str(result[6]))
# print("Side b: " + str(result[7]))
# print("Side c: " + str(result[8]))


