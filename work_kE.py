"""
Work done by the net force of a moving (accelerated) body is equal to kinetic energy variation during movement, W = delta E_k.
"""

def kE (m, v_init, a, t, gamma_m=1.08, eta_t=0.95, eta_max=0.4):
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

def wk (m, v_init, a, t, gamma_m=1.08, eta_t=0.95, eta_max=0.4):
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


def kE_mus (m, v_init, a, t, mu_init, mu_fin, gamma_m=1.08,
            eta_t=0.95, eta_max=0.4):
    """
    Function to compute kinetic energy variation during accelerated period.
    Takes as inputs the vehicle mass, initial speed, acceleration, time,
    coefficient of rotational masses, vehicle transmission efficiency,
    engine max. efficiency, engine initial efficiency coefficient and
    engine final efficiency coefficient.
    Returns the kinetic energy variation.
    Note:  engine efficiency coefficients across speed and output
    ranges are taken into account.
    """

    # same coefficient for facile formula writting
    C1 = (m * gamma_m) / (2 * eta_t * eta_max)

    kE_mus = (C1 * v_init**2 * ((1/mu_fin) - (1/mu_init)) + ((C1 * a * t) /
              (mu_fin)) * (2 * v_init + a * t))

    return kE_mus


def wk_avf_mus(m, v_init, a, t, mu_init, mu_fin, gamma_m=1.08, 
               eta_t=0.95, eta_max=0.4):
    """
    Function to compute the work of the average inertial force during
    accelerated period.
    Takes as inputs the vehicle mass, initial speed, acceleration, time,
    coefficient of rotational masses, vehicle transmission efficiency,
    engine max. efficiency, engine initial efficiency coefficient and
    engine final efficiency coefficient.
    Returns the kinetic energy variation.
    Note:  engine efficiency coefficients across speed and output
    ranges are taken into account.
    """

    # same coefficient for facile formula writting
    C2 = ((m * gamma_m * a) / (2 * eta_t * eta_max)) * ((1 / mu_init) + (1 /
                                                                     mu_fin))

    wk_fav_mus = C2 * (v_init * t + (a * t**2) / 2)

    return wk_fav_mus


def wk_avmus(m, v_init, a, t, mu_init, mu_fin, gamma_m=1.08,
             eta_t=0.95, eta_max=0.4):
    """
    Function to compute the work of the inertial force with average mus during
    accelerated period.
    Takes as inputs the vehicle mass, initial speed, acceleration, time,
    coefficient of rotational masses, vehicle transmission efficiency,
    engine max. efficiency, engine initial efficiency coefficient and
    engine final efficiency coefficient.
    Returns the kinetic energy variation.
    Note:  engine efficiency coefficients across speed and output
    ranges are taken into account.
    """

    # same coefficient for facile formula writting
    C3 = (2 * m * gamma_m * a) / (eta_t * eta_max * (mu_init + mu_fin))

    wk_avmus = C3 * (v_init * t + (a * t**2) / 2)

    return wk_avmus

# The data to be used to check scenarios
m = 2235
a = 0.38889
t = 1
v_init = 3.72222
eta_max = 0.4
eta_t = 0.95
mu_init = 0.544684
mu_fin = 0.363850


print("Kinetic energy variation, no mus, ", kE(m, v_init, a, t))
print("Work done by net/inertia force, no mus, ", wk(m, v_init, a, t))
print("Kinetic energy variation, with mus, ", kE_mus(m, v_init, a, t, mu_init,
                                                     mu_fin))
print("Work done by the average inertia force, with mus, ", wk_avf_mus(m,
                                                            v_init, a, t,
                                                                       mu_init,
                                                                       mu_fin))
print("Work done by the inertia force, with average mu, ", wk_avmus(m, v_init,
                                                                    a, t,
                                                                    mu_init,
                                                                    mu_fin))
