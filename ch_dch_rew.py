"""
Script to compute the charge-discharge reward
"""

import sys

def reward(soc, prev_rew, rew_up_lim = 5, rew_low_lim = -1000, soc_up =80, soc_low = 40):
    """
    Function to compute charge/discharge reward value.
    Takes as input the state of charge (SoC), in percent,
    previous charge reward value,
    upper and lower limits of the reward,
    upper and lower limits of the SoC, and
    returns the SoC and depth of discharge (DoC) reward values.
    """

    return soc_rew, dod_rew
