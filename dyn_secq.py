"""
This is the script for storing the needed secquences of dynamically
changing variables, i.e. gear ratio, initial speed, acceleration,
and time of accelerated movement.
The script will be read subsequently by the RL agent, the mentioned
values being used to compute specific fuel/enegy consumption.
"""

"""
the changing values are stored in a list of tuples,
in the following order: gear ratio, initial speed,
acceleration and time.
"""

dyns = []   #list for storing tuples

# first tuple: gear ratio, initial null speed,
# acceleration 1.2 m/s**2 applied for 12 seconds

a = 0.94, 0, 1.2, 12
dyns.append(a)   #append the tuple
