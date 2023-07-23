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

import simfc4 as sfc

# initial list of list (list of sequences) for WLTP cycle low speed section
low_raw = [[0, 45, 10, 30], [45, 12,30, 55], [12, 40, 55, 75],
           [40, 0, 75, 100], [0, 30, 140, 150], [30, 12, 150, 155],
           [12, 38, 155, 170], [38, 25, 170, 175], [25, 30, 175, 180],
           [30, 12, 180, 200], [12, 57, 200, 225], [57, 14, 225, 255],
           [14, 52, 255, 275], [52, 20, 275, 285], [20, 50, 285, 295],
           [50, 46, 295, 300], [46, 13, 300, 340], [13, 27, 340, 350],
           [27, 20, 350, 365], [20, 25, 365, 370], [25, 0, 370, 385],
           [0, 30, 385, 400], [30, 13, 400, 415], [13, 33, 415, 435],
           [33, 0, 435, 450], [0, 22, 520, 530], [22, 0, 530, 540],
           [0, 30, 540, 550], [30, 12, 550, 565], [12, 18, 565, 570],
           [18, 0, 570, 575]
           ]

"""
class to process the input list
"""

class Process_inputs:
    def __init__(self, input_list):
        self.input_list[0] = input_list[0]
        self.input_list[1] = input_list[1]
        self.input_list[2] = input_list[2]
        self.input_list[3] = input_list[3]

    def raw_proc(input_list):
        """
        Method to process the raw list of values as collected
        from the speed profile.
        Takes the list of four values, i.e. initial/final speeds, in km/h,
        and initial/final time read on the WLTP speed profile time axis.
        Returns a list with intial speed, in m/s, second place in the list
        reserved for gearbox ratio, acceleration, in m/s**2, and time, in
        secodns.
        """
        print(type(input_list[0]))
        finals = []  #list to store the returned results
        finals.append(list[0])
        finals.append(0)
        a = (list[1] - list[0]) / (list[3] - list[2])
        finals.append(a)
        t = list[3] - list[2]
        finals.append(t)

        return finals

sec = low_raw[0]
print(Process_inputs.raw_proc(sec))
