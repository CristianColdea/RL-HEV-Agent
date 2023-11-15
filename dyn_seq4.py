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

# initial list of lists (list of sequences) for WLTP cycle low speed section
low_raw = [[0, 45, 10, 30], [45, 12, 30, 55], [12, 40, 55, 75],
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


def process_input(processed, gear_ini, min_lim=1800, max_lim=3100, tstep=0.5):
    """
    Function to handle the processed list in order to get the
    gearbox ratio, according to the rule of MAX and MIN engine speed limits.
    Takes as arguments the list processed with above functions,
    namely initial speed, in m/s, 0, acceleration, in m/s**2, time, in s,
    the initial (last known or imposed) gear,
    MIN and MAX engine speed limits, time step, in s.
    Returns the complete list of sublists for fuel consumption calculation
    and the last allocated gear of the current sequence.
    Importan note for a better understanding of this function: accelerated and
    deccelerated vehicle movements require two different approaches.
    """
    
    ret = []  # collect each time step sublist
            
    dict_fix = sfc.unpack_f(sc.fixs)
    
    # the initial total time per sequence
    t_init = processed[3]
    
    # reference speed per sequence
    v_ref = processed[0] + processed[3] * processed[2]
    print("v_ref is, ", v_ref)

    gear_i = gear_ini

    if processed[0] == 0:
        processed = null_speed(processed)
        ret.append(processed[:])
        gear_i = sc.xi_gs[0]
       
    # get the current gear index
    pos = 0
    for index, gear in enumerate(sc.xi_gs):
        if gear == gear_i:
            pos = index 

    # accelerated movement, starting from the current gear
    for posi, gear in enumerate(sc.xi_gs[pos:]):
        # print("processedA, ", processed)
        
        n_i = sfc.engine_speed(processed[0], dict_fix['xi_f'],
                               gear, dict_fix['r_d'],
                               dict_fix['s_f'], dict_fix['n_max'])
        
                
        if (n_i > dict_fix['n_max']):
            continue
        
        if gear != sc.xi_gs[-1]:    # while not in the last gear
            # next gear engine speed
            n_next = sfc.engine_speed(processed[0], dict_fix['xi_f'],
                                   sc.xi_gs[posi+1], dict_fix['r_d'],
                                   dict_fix['s_f'], dict_fix['n_max'])
            
            # increase speed by timestep, within engine speed limits
            while (n_next <= min_lim):
                processed[0] = processed[0] + tstep * processed[2]
                processed[1] = gear
                processed[3] = tstep

                if (processed[0] >= v_ref):   # reached the end of sequence
                    processed[0] = v_ref
                    if (t_init % tstep > 0):
                        processed[3] = t_init % tstep
                    ret.append(processed[:])
                    return ret

                ret.append(processed[:])

                print("n_next as control variable, ", n_next)
                n_next = sfc.engine_speed(processed[0], dict_fix['xi_f'],
                                   sc.xi_gs[posi+1], dict_fix['r_d'],
                                   dict_fix['s_f'], dict_fix['n_max'])

        
        else:   # in the last gear
            # current engine speed
            n_i = sfc.engine_speed(processed[0], dict_fix['xi_f'],
                                   gear, dict_fix['r_d'],
                                   dict_fix['s_f'], dict_fix['n_max'])

            # increase speed by timestep up to MAX limit
            while (n_i <= max_lim):
                processed[0] = processed[0] + tstep * processed[2]
                processed[1] = gear
                processed[3] = tstep

                if (processed[0] >= v_ref):   # reached the end of sequence
                    processed[0] = v_ref
                    if (t_init % tstep > 0):
                        processed[3] = t_init % tstep

                ret.append(processed[:])
                
            if (processed[0]< v_ref):
                print("The final imposed speed is too high.")
                exit()
                
                return ret
                
                n_i = sfc.engine_speed(processed[0], dict_fix['xi_f'],
                                   gear, dict_fix['r_d'],
                                   dict_fix['s_f'], dict_fix['n_max'])
                print("n_i as a control variable, ", n_i)

#for seq in low_raw:
#    print(process_input(raw_proc(seq)))
# collect sublist from the entire low speed profile
# the list for the final sublists
# fin = []
# for seq in low_raw:
#    fin.extend(process_input(raw_proc(seq)))

# print(fin)
# print("Raw values, first sequence, from the speed profile, ", low_raw[0])
# print("First sequence processed for speed, acceleration, time, ", 
#       raw_proc(low_raw[0]))

# the loop to cycle through the list of sequences, i.e. low_raw
# the list to store expanded values
expand = []

for sequence in low_raw[:2]:
    # if expand empty
    if not expand:
    #    expand.extend(process_input(raw_proc(sequence), sequence[1]))
        print("Seq 1, ", sequence)
    else:   # use the previous sequence gear
    #    expand.extend(process_input(raw_proc(sequence),
    #                                         expand[-1][1]))
        print("Seq 2, ", sequence)

print(process_input(raw_proc(low_raw[0]), low_raw[0][1]))
print("**********")
# print(expand)
