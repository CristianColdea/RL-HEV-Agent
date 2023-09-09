"""
Within this script the values for the engine torque curve on the engine speed
range are computed and stored.
It makes use of simfc5.py and sfc_call.py programmes already scripted.
"""

import simfc5 as sfc
import sfc_call as sc

# engine maximum output
P_max = sc.P_max

# engine maximum speed
n_max = sc.n_max

# print("Engine max output, ", P_max)
# print("Engine max speed, ", n_max)
# engine minimum stable speed
n_min = 800

trq = {}
for n in range(n_min, n_max, 50):
    # curent output according to engine speed and type
    P_i = sfc.Mus.p_maxn(P_max, n, n_max, engine_tp = 'CIE')
    trq[n] = (9549.2 * P_i) / n

print(trq)
