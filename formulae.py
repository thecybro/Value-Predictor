def bxy(N, Ex, Ey, Ey2, Exy):
    return (N*Exy - Ex*Ey) / (N*Ey2 - Ey**2)

def byx(N, Ex, Ey, Ex2, Exy):
    return (N*Exy - Ex*Ey) / (N*Ex2 - Ex**2)

def findX(y, xmean, ymean, bxy):
    return xmean + bxy * (y - ymean)

def findY(x, xmean, ymean, byx):
    return ymean + byx * (x - xmean)

def correlation_coefficient(bxy, byx):
    r = (bxy * byx) ** 0.5
    return -r if bxy * byx < 0 else r
