from formulae import bxy, byx, findX, findY, correlation_coefficient

def main(X, Y, mode, value):
    if len(X) != len(Y) or len(X) < 2:
        return "Invalid data"

    N = len(X)

    EX = sum(X)
    EY = sum(Y)
    EX2 = sum(x*x for x in X)
    EY2 = sum(y*y for y in Y)
    EXY = sum(x*y for x, y in zip(X, Y))

    b_xy = bxy(N, EX, EY, EY2, EXY)
    b_yx = byx(N, EX, EY, EX2, EXY)

    x_mean = EX / N
    y_mean = EY / N

    if mode == "x":
        return f"Predicted x = {findX(value, x_mean, y_mean, b_xy):.4f}"

    elif mode == "y":
        return f"Predicted y = {findY(value, x_mean, y_mean, b_yx):.4f}"

    else:
        r = correlation_coefficient(b_xy, b_yx)
        return f"Correlation coefficient r = {r:.4f}"
