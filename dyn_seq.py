"""
This is the script for storing the needed secquences of dynamically
changing variables, i.e. initial speed, gear ratio, acceleration,
and time of accelerated movement.
The script will be read subsequently by the RL agent, the mentioned
values being used to compute specific fuel/energy consumption.
"""

"""
The changing values are stored in a final list of lists,
in the following order: initial speed, gearbox ratio,
acceleration and time.
_____
The initial list of lists, as value resulted from the WLTP cycle speed
profile, is introduced.
The values are intial speed, final speed, initial time, final time,
precisely in this order.
"""

# initial list of list (list of sequences) for WLTP cycle low speed section
low_row = [[0, 45, 10, 30], [45, 12,30, 55], [12, 40, 55, 75],
           [40, 0, 75, 100], [0, 30, 140, 150], [30, 12, 150, 155],
           [12, 38, 155, 170], [38, 25, 170, 175], [25, 30, 175, 180],
           [30, 12, 180, 200], [12, 57, 200, 225], [57, 14, 225, 255],
           [14, 52, 255, 275], [52, 20, 275, 285], [20, 50, 285, 295],
           [50, 46, 295, 300], [46, 13, 300, 340], [13, 27, 340, 350],
           [27, 20, 350, 365], [20, 25, 365, 370], [25, 0, 370, 385],
           [0, 30, 385, 400], [30, 13, 400, 415], [13, 33, 415, 435],
           ]
# first list: initial null speed, gearbox ratio,
# acceleration 1.2 m/s**2 applied for 12 seconds

a = [0, 0.94, 1.2, 12]
dyns.append(a)   #append the list
b = [3, 2.94, 0.3, 12]    #second list
dyns.append(b)

"""
class to process the input list
"""

class Process_inputs:
    def __init__(self, input_list):
        self.input_list[0]
        self.input_list[1]
        self.input_
