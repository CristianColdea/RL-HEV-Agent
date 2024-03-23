"""
Work done by the net force of a moving (accelerated) body is equal to kinetic energy variation during movement, W = delta E_k.
"""

def kE (m, v_init, a, t, gamma=1.08, eta_t=0.98, eta_max=0.4):
    """
    Function to compute kinetic energy variation during accelerated period.
    Takes as inputs the vehicle mass, initial speed, acceleration, time,
    coefficient of rotational masses, vehicle transmission efficiency and
    engine max. efficiency.
    Returns the kinetic energy variation.
    Note: at this stage engine efficiency coefficients are not taken into account.
    """
    kE = ((m * gamma_m * a * t) / (2 * eta_t * eta_max)) / (2 * v_init + a * t)

    return kE

