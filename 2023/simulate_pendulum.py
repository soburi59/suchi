import numpy as np
def simulate_pendulum(p):
    l = p['l']
    m = p['m']
    k = p['k']
    g = p['g']
    theta_dot = p['theta_dot']
    t_f = p['t_f']
    t_e = p['t_e']
    h = p['h']

    theta = [p['theta']]
    t = [t_f]

    # オイラー法で微分方程式を解く
    i = 0
    while t[i] <= t_e:
        theta_ddot = -(k/m)*theta_dot - (g/l)*np.sin(theta[i]) #θ''
        theta.append(theta[i] + h*theta_dot) #θ
        theta_dot+= h*theta_ddot #θ'
        t.append(t[i] + h)
        i += 1
    return theta,t
