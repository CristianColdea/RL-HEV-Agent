"""
Work done by the net force of a moving (accelerated) body is equal to kinetic energy variation during movement, W = delta E_k.
"""

def kE (m, v_init, a, t, gamma=1.08, eta_t=0.98, eta_max=0.4):
    kE = ((m * gamma_m * a * t) / (2 * eta_t * eta_max)) / (2 * v_init + a * t)

    return kE

