"""
Script to shape the specific fuel consumption reward.
"""
import math

def rew_sfc(sfc):
    """
    Function to compute specific fuel consumption reward value.
    Takes as input the specific fuel consumption, in kg/kWh.
    Returns the reward value.
    """
    if sfc <= 0.4:
        return 100 * math.e ** (10.063 * (0.18 - sfc))
    else:
        return -5 * math.e ** (45.38 * (sfc - 0.45))
