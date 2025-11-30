import numpy as np

def deriv(t, y, b, g, N):
    S, I, R = y
    dS = -(b * S * I) / N
    dI = (b * S * I) / N - g * I
    dR = g * I
    return np.array([dS, dI, dR])


def rk4(f, y0, t0, tf, steps, args):
    h = (tf - t0) / steps
    T = np.linspace(t0, tf, steps+1)
    Y = np.zeros((steps+1, len(y0)))
    Y[0] = y0

    for i in range(steps):
        ti = T[i]
        yi = Y[i]

        k1 = f(ti, yi, *args)
        k2 = f(ti + h*0.5, yi + h*0.5*k1, *args)
        k3 = f(ti + h*0.5, yi + h*0.5*k2, *args)
        k4 = f(ti + h, yi + h*k3, *args)

        Y[i+1] = yi + (h/6)*(k1 + 2*k2 + 2*k3 + k4)

    return T, Y
