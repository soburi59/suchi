import numpy as np

def simulate_pendulum(p):
    l = p['l']
    m = p['m']
    k = p['k']
    g = p['g']
    theta_0 = p['theta_0']
    theta_dot_0 = p['theta_dot_0']
    t_f = p['t_f']
    t_e = p['t_e']
    h = p['h']

    theta = [theta_0]
    theta_dot = [theta_dot_0]
    t = [t_f]

    # オイラー法で微分方程式を解く
    i = 0
    while t[i] <= t_e:
        theta_ddot = -(k/m)*theta_dot[i] - (g/l)*np.sin(theta[i]) #θ''
        theta_dot.append(theta_dot[i] + h*theta_ddot) #θ'
        theta.append(theta[i] + h*theta_dot[i]) #θ
        t.append(t[i] + h)
        i += 1
    return theta
