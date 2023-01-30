"""
Script to compute Electric Motor (EM) reduction gear ratio,
please read the next docstring.
Code reused from specific fuel consumption script (simfc3.py).
The rationale behind this whole idea is to provide an evently distributed
maximum possible efficiency for both urban and non-urban driving.
"""

def reduction_ratio(v, r_d, n_em, n_max, v_max, s_f=1.05):
    """
    Function to compute engine speed related to vehicle speed.
    Takes as parameters vehicle speed, in km/h, rolling/dynamic
    radius of the wheel, in m, EM maximum efficiency speed,
    EM maximum speed, vehicle maximum speed, and the slip factor.
    Check to not exceed the maximum vehicle speed when on electric traction,
    at maximum EM speed, as a safety measure.
    Returns EM reduction ratio.
    """

    xi_red = (3.6 * r_d * n_em) /  (9.55 * v * s_f) 
    
    # compute vehicle speed at maximum EM revs, for the determined
    # reduction ratio
    v_em = (3.6 * r_d * n_max) / (9.55 * xi_red * s_f)
    
    # return tuple 
    
    return(bool(v_em > v_max), xi_red)

# function call with v = 90 km/h, n_em = 3200 rpm, n_max = 12 krpm,
# v_max = 239 km/h, and rolling radius r_d = 0.317 m.

print(reduction_ratio(90, 0.317, 3200, 12000, 239))
