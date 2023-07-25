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

import simfc5 as sfc
import sfc_call as sc

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

def raw_proc(raw_list):
    """
    Function to process the raw list of values as collected
    from the speed profile.
    Takes as argument the list of four values, 
    i.e. initial/final speeds, in km/h,
    and initial/final time read on the WLTP speed profile time axis.
    Returns a list with intial speed, in m/s, second place in the list
    is always complete with lowest gearbox ratio, acceleration, in m/s**2,
    and time, in seconds.
    """
        
    processed = []  #list to store the returned results
    processed.append(raw_list[0]/3.6)  # initial speed
    processed.append(0)  # the second position reserved
    processed.append((raw_list[1] - raw_list[0]) /\
                 (3.6 * (raw_list[3] - raw_list[2])))  # acceleration
    processed.append(raw_list[3] - raw_list[2])  # time

    return processed

"""
class to handle the processed list
"""

class Process_inputs:
    def __init__(self, processed):
        self.processed = processed
    
    def tmstp(processed):
        steps = 0
        return processed, steps
    def comp_lst(processed):
        """
        Method to complete the needed list with gearbox ratio.
        Takes as argument the list processed with previous function,
        initial speed, in m/s, 0, acceleration, in m/s**2, time, in s.
        Returns the complete list for fuel consumption calculation,
        with gearbox ratio as the second list item.
        """
        
        # always start in the 1st gear at null speed
        if processed[0] == 0:
            processed[1] = sc.xi_gs[0]
        
        dict_fix = sfc.unpack_f(sc.fixes)
        dict_dyn = sfc.unpack_d(processed)

        # setup flags based on max engine speed 2400 rpm, min 1400 rpm
        n_i = sfc.engine_speed(dict_dyn['v_init'], dict_fix['xi_f'],
                               dict_dyn['xi_g'], dict_fix['r_d'],
                               dict_fix['s_f'], dict_fix['n_max'])
        if(n_i <= 2400 and n_i >= 1400):
            flg = True
        else:
            flg = False
        return processed

# print(raw_proc(low_raw[0]))
print(Process_inputs.comp_lst(raw_proc(low_raw[0])))
