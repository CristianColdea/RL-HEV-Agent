"""
This is the script for storing the needed secquences of dynamically
changing variables, i.e. initial speed, gear ratio, acceleration,
and time of accelerated movement.
The script will be read subsequently by the RL agent, the mentioned
values being used to compute specific fuel/energy consumption.
"""

"""
the changing values are stored in a list of lists,
in the following order: initial speed, gearbox ratio,
acceleration and time.
"""

dyns = []   #list for storing lists

# first list: initial null speed, gearbox ratio,
# acceleration 1.2 m/s**2 applied for 12 seconds

a = [0, 0.94, 1.2, 12]
dyns.append(a)   #append the list
b = [3, 2.94, 0.3, 12]    #second list
dyns.append(b)

for secq in dyns:
    for item in secq:
        print(item)
