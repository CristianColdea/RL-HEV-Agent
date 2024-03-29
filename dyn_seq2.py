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
    is always completed with 0, acceleration, in m/s**2,
    and time, in seconds.
    """
        
    processed = []  #list to store the returned results
    processed.append(raw_list[0]/3.6)  # initial speed
    processed.append(0)  # the second position reserved
    processed.append((raw_list[1] - raw_list[0]) /\
                 (3.6 * (raw_list[3] - raw_list[2])))  # acceleration
    processed.append(raw_list[3] - raw_list[2])  # time

    return processed

def null_speed(processed, tstep=0.5, n_stab=800):
    """
    Function to ensure that the vehicle starts in first gear
    at null speed.
    Takes as arguments the list of processed with above functions,
    namely initial speed, in m/s, 0, acceleration, in m/s**2, time, in s,
    and the time step, in s.
    Returns the processed with non null initial speed.
    """
    
    if processed[0] == 0:
        processed[1] = sc.xi_gs[0]
        processed[3] = tstep 
        # print("Processed before acceleration applied, ", processed)
        accelerated = processed[0] + tstep * processed[2]
        dict_fix = sfc.unpack_f(sc.fixs)
        # kinematic link between engine and wheels
        idle = (n_stab * dict_fix['r_d']) /\
               (9.55 * dict_fix['xi_f'] * sc.xi_gs[0] * dict_fix['s_f'])
        processed[0] = max(accelerated, idle)
        # print("Speed as a result of acceleration applied, ", accelerated)
        # print("Speed as a result at idle engine speed, ", idle)
    return processed

def process_input(processed, max_lim=3100, min_lim=1800, tstep=0.5):
    """
    Function to handle the processed list in order to get the
    gearbox ratio, according to the rule of MAX and MIN engine speed limits.
    Takes as arguments the list processed with above functions,
    namely initial speed, in m/s, 0, acceleration, in m/s**2, time, in s,
    MAX and MIN engine speed limits, time step, in s.
    Returns the complete list of sublists for fuel consumption calculation.
    """
    
    ret = []  # collect each time step sublist
            
    dict_fix = sfc.unpack_f(sc.fixs)
    
    v_max = processed[0] + processed[3] * processed[2]
    # print("Max speed, ", v_max)
    # print("Processed before cycle, ", processed)
    
    while (processed[0] < v_max):
        if processed[0] == 0:
            processed = null_speed(processed)
            ret.append(processed)
            # continue
        #print("Before 'for' cycle, ", processed)

        for gear in sc.xi_gs:
            print("processed[0]A, ", processed[0])
            # print("current gear, ", gear)
            n_i = sfc.engine_speed(processed[0], dict_fix['xi_f'],
                                   gear, dict_fix['r_d'],
                                   dict_fix['s_f'], dict_fix['n_max'])
            print("n_iA, ", n_i)
            # print("n_iA2, ", sfc.engine_speed(processed[0], dict_fix['xi_f'],
            #                       sc.xi_gs[0], dict_fix['r_d'],
            #                       dict_fix['s_f'], dict_fix['n_max']))

            # print("n_iB, ", (9.55 * processed[0] * dict_fix['xi_f'] *
            #                sc.xi_gs[0] * dict_fix['s_f'])/dict_fix['r_d'])
            
            #print("Engine speed early, ", n_i)   
            # print(n_i, processed)
            # check engine speed conditions
            while (n_i < min_lim):
                print("processed[0]B, ", processed[0])
                print("current gear B, ", gear)
                processed[0] = processed[0] + tstep * processed[2]
                processed[1] = gear
                processed[3] = tstep
                ret.append(processed)

                n_i = sfc.engine_speed(processed[0], dict_fix['xi_f'],
                                       gear, dict_fix['r_d'],
                                       dict_fix['s_f'], dict_fix['n_max'])

                if (processed[0] >= v_max):   # reached the end of sequence
                    # processed[0] = v_max
                    # break   # finish the inner while
                    return ret
                
                                         
            print("processed[0]C, ", processed[0])
            n_i = sfc.engine_speed(processed[0], dict_fix['xi_f'],
                                   gear, dict_fix['r_d'],
                                   dict_fix['s_f'], dict_fix['n_max'])
            print("n_iC, ", n_i)

            
            if (n_i >= min_lim and n_i <= max_lim):
                processed[0] = processed[0] + tstep * processed[2]
                processed[1] = gear
                processed[3] = tstep
                ret.append(processed)

                if (processed[0] >= v_max):   # reached the the end of sequence
                    # processed[0] = v_max

                    # break  # finish of the sequence
                    return ret
                if (processed[0]< v_max and gear == sc.xi_gs[-1]):
                    print("The final speed is too high.")
                    exit()
                           
        # processed[0] = processed[0] + tstep * processed[2]
        # print("Speed, ", processed[0])
        # print("Engine speed, ", n_i)
                
    # return ret

# print("Raw values, first sequence, from the speed profile, ", low_raw[0])
# print("First sequence processed for speed, acceleration, time, ", 
#       raw_proc(low_raw[0]))
print(process_input(raw_proc(low_raw[0])))
# print("Null speed, ", null_speed(raw_proc(low_raw[0])))
# print(low_raw[0])
# print(raw_proc(low_raw[0]))
# print(int(tmstp(raw_proc(low_raw[0])[-1])[0]))
#print(process_input(raw_proc(low_raw[0]),
#                    int(tmstp(raw_proc(low_raw[0])[-1])[0])))
# process_input(raw_proc(low_raw[0]),
#                    int(tmstp(raw_proc(low_raw[0])[-1])[0]))
