"""
Work done by the net force of a moving (accelerated) body is equal to kinetic energy variation during movement, W = delta E_k.
"""

def kE (m, v_init, a, t, gamma_m=1.08, eta_t=0.98, eta_max=0.4):
    """
    Function to compute kinetic energy variation during accelerated period.
    Takes as inputs the vehicle mass, initial speed, acceleration, time,
    coefficient of rotational masses, vehicle transmission efficiency and
    engine max. efficiency.
    Returns the kinetic energy variation.
    Note: at this stage engine efficiency coefficients across speed and output
    ranges are not taken into account.
    """
    kE = ((m * gamma_m * a * t) / (2 * eta_t * eta_max)) * (2 * v_init + a * t)

    return kE

def wk (m, v_init, a, t, gamma_m=1.08, eta_t=0.98, eta_max=0.4):
    """
    Function to compute work done by the net force during acceleration period.
    Takes as inputs the vehicle mass, initian speed, acceleration, time, coefficient
    of rotational masses, vehicle transmission efficiency and engine max. efficiency.
    Returns the work done.
    Note: at this stage engine efficiency coefficients across speed and output
    ranges are not taken into account.
    """

    work = ((m * gamma_m * a * t) / (2 * eta_t * eta_max)) * (2 * v_init + a * t)
    
    return work

# The data to be used to check scenarios
m = 10
a = 1.5
t = 3
v_init = 2
# eta_max = 0.4
# eta_t = 0.98
# mu_init = 0.81
# mu_fin = 0.83

def kE_mus (m, v_init, a, t, gamma_m=1.08, eta_t=0.98, eta_max=0.4, mu_init=0.81,
            mu_fin=0.83):
    """
    Function to compute kinetic energy variation during accelerated period.
    Takes as inputs the vehicle mass, initial speed, acceleration, time,
    coefficient of rotational masses, vehicle transmission efficiency,
    engine max. efficiency, engine initial efficiency coefficient and
    engine final efficiency coefficient.
    Returns the kinetic energy variation.
    Note:  engine efficiency coefficients across speed and output
    ranges taken into account.
    """
    kE_mus = ((m * gamma_m * a * t) / (2 * eta_t * eta_max)) * (2 * v_init + a * t)

    return kE


print("Kinetic energy variation, no mus, ", kE(m, v_init, a, t))
print("Work done by net/inertia force, no mus, ", wk(m, v_init, a, t))


