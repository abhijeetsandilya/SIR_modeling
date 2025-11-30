import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sir_model import deriv, rk4

N = 10**6
i0 = 10
r0 = 0
s0 = N - i0 - r0

beta = 0.3
gamma = 0.1

y0 = np.array([s0, i0, r0])


t0 = 0
tf = 160
steps = 1600

t, y = rk4(deriv, y0, t0, tf, steps, (beta, gamma, N))

S = y[:,0]
I = y[:,1]
R = y[:,2]


I_frac = I / N
peak = I_frac.max()
peak_day = t[I_frac.argmax()]
R0 = beta/gamma

print("R0:", R0)
print("peak infected fraction:", peak)
print("peak day:", peak_day)
print("final recovered fraction:", R[-1]/N)


df = pd.DataFrame({
    "time": t,
    "S": S,
    "I": I,
    "R": R
})
df.to_csv("sir_output.csv", index=False)

plt.plot(t, S, label='S')
plt.plot(t, I, label='I')
plt.plot(t, R, label='R')
plt.legend()
plt.xlabel("days")
plt.ylabel("people")
plt.title("SIR model")
plt.grid()
plt.show()
