"""
Script to compute transmission final gear ratio, please read the next
docstring.
Code reused from specific fuel consumption script (simfc3.py).
"""

def final_ratio(v_max, xi_g, r_d, n_max, s_f=1.05):
    """
    Function to compute engine speed related to vehicle speed.
    Takes as parameters vehicle speed, in km/h, final gear ratio,
    gearbox ratio, rolling/dynamic radius of the wheel, in m
    and the slip factor.
    Returns transmission final ratio.
    """

    xi_f = (3.6 * r_d * n_max) /  (9.55 * v_max * xi_g * s_f)
    
    return xi_f

# function call with v_max = 239 km/h, n_max = 5000 rpm, 
# the ninth gear, xi_g = 0.601, and rolling radius r_d = 0.317 m.

print(final_ratio(239, 0.601, 0.317, 5000))
