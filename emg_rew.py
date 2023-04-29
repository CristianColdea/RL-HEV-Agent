"""
Script to shape the Electric Motor and Generator reward
"""


def emg_rew(eta):
    """
    The function to compute reward value.
    Takes as input the electric machine efficiency.
    Returns the reward value.
    """

    return (-750 * eta**2 + 1625 * eta - 770)

# test the function
# print(emg_rew(0.96))
