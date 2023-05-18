import numpy as np

def simulate_pendulum(l, m, k, g, theta_0, theta_dot_0, t_f, t_e, h):
    t = np.arange(t_f, t_e, h)
    n = len(t)
    theta = np.zeros(n)
    theta_dot = np.zeros(n)

    theta[0] = theta_0
    theta_dot[0] = theta_dot_0

    for i in range(1, n):
        theta_ddot = -(k/m) * theta_dot[i-1] - (g/l) * np.sin(theta[i-1])  # θ''
        theta_dot[i] = theta_dot[i-1] + h * theta_ddot  # θ'
        theta[i] = theta[i-1] + h * theta_dot[i-1]  # θ

    return theta
