"""
Script to compute the charge-discharge reward
"""

import sys

def reward(soc, rew_up_lim = 5, rew_low_lim = -1000, soc_low = 40, soc_low = 80):
    """
    Function to compute charge/discharge reward value.
    Takes as input the state of charge, in percent, and
    returns the reward value.
    """

    return soc
