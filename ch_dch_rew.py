"""
Script to compute the charge-discharge reward
"""

import sys

def reward(soc, rew_up_lim = 100, rew_low_lim = -1000, soc_up =80, soc_low = 40):
    """
    Function to compute charge/discharge reward value.
    Takes as input the state of charge (SoC), in percent,
    upper and lower limits of the reward,
    upper and lower limits of the SoC, and
    returns the SoC and depth of discharge (DoC) reward values.
    """
    
    if soc > soc_low and soc < soc_up:
        soc_rew = (-rew_up_lim / (soc_up - soc_low)) * soc + rew_up_lim
        dod_rew = (rew_up_lim / (soc_up - soc_low)) * soc
    else:
        soc_rew = -1000
    return soc_rew, dod_rew
