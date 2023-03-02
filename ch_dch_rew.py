"""
Script to compute the charge-discharge reward
"""

import sys

def reward(soc, up_lim = 5, low_lim = -1000):
    """
    Function to compute charge/discharge reward value.
    Takes as input the state of charge, in percent, and
    returns the reward value.
    """

    return soc
