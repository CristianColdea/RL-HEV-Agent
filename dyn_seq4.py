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

# medium speed section
med_raw = [[0, 49, 600, 615], [49, 44, 615, 625],
           [44, 57, 625, 652], [57, 11, 652, 654],
           [11, 40,654, 675], [40, 18, 675, 685],
           [18, 33, 685, 700], [33, 12, 700, 710],
           [12, 22, 710, 718], [22, 12, 718, 725],
           [12, 40, 725, 732], [40, 50, 732, 750],
           [50, 12, 750, 770], [12, 66, 770, 795],
           [66, 41, 795, 800], [41, 53, 800, 815],
           [53, 17, 815, 822], [17, 47, 822, 830],
           [47, 77, 830, 870], [77, 67, 870, 880],
           [67, 42, 880, 915], [42, 65, 915, 925],
           [65, 53, 925, 940], [53, 25, 940, 960],
           [25, 52, 960, 970], [52, 0, 970, 985]]

# high speed section
high_raw = [[0, 53, 1025, 1050], [53, 11, 1050, 1060],
            [11, 63, 1060, 1080], [63, 58, 1080, 1085],
            [58, 64, 1085, 1100], [64, 58, 1100, 1110],
            [58, 70, 1110, 1120], [70, 14, 1120, 1140],
            [14, 25, 1140, 1145], [25, 12, 1145, 1155],
            [12, 97, 1155, 1250], ]

# ultra high speed section
ultra_high_raw = [[0, 48, 1480, 1500],
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

def null_speed(processed, tstep=0.5, n_stab=1000):
    """
    Function to ensure that the vehicle starts in first gear
    at null speed.
    Takes as arguments the list of processed with above functions,
    namely initial speed, in m/s, 0, acceleration, in m/s**2, time, in s,
    and the time step, in s,
    engine stable working speed.
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


def process_input(processed, gear_ini, min_lim=1800, max_lim=3100, tstep=0.5,
                  n_stab=1000, n_max=5000):
    """
    Function to handle the processed list in order to get the
    gearbox ratio, according to the rule of MAX and MIN engine speed limits.
    Takes as arguments the list processed with above functions,
    namely initial speed, in m/s, 0, acceleration, in m/s**2, time, in s,
    the initial (last known or imposed) gear,
    MIN and MAX engine speed limits,
    time step, in s,
    engine stable working speed,
    and engine max speed.
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
    print("v_ref , ", v_ref)

    print("processed, ", processed)

    print("gear_ini, ", gear_ini)

    gear_i = gear_ini

    print("gear_i, ", gear_i)

    if processed[0] == 0:
        processed = null_speed(processed)
        ret.append(processed[:])
        gear_i = sc.xi_gs[0]
       
    # get the current gear index
    pos = 0
    for index, gear in enumerate(sc.xi_gs):
        if gear == gear_i:
            pos = index 

    # uniform movement
    n_i = sfc.engine_speed(processed[0], dict_fix['xi_f'],
                           gear_i, dict_fix['r_d'],
                           dict_fix['s_f'], dict_fix['n_max'])

    
    if(processed[2] == 0):
        processed[1] = gear_i   # allocate the gear for uniform movement

        if(processed[1] > 0):  #in a certain gear
            if(n_i > n_stab) and (n_i < n_max): #within proper speed
                return processed
            else:
                print("Engine speed is either too low or too high. Please\
                adjust!")
                exit()
        else:
            print("Please provide a proper gear.")
            exit()

    # accelerated movement, starting from the current gear
    if(processed[2] > 0):
        
        for posi, gear in enumerate(sc.xi_gs[pos:]):
                    
            n_i = sfc.engine_speed(processed[0], dict_fix['xi_f'],
                                   gear, dict_fix['r_d'],
                                   dict_fix['s_f'], dict_fix['n_max'])
            
                    
            if (n_i > dict_fix['n_max']):
                continue

            if(n_i < n_stab):
                print("Engine speed is too low. Please adjust!")
                exit()

            # print("engine speed before stab, ", n_i)
            # print("processed[0] before stab, ", processed[0])

            # if engine speed is less than stable working speed
            # if(n_i <= n_stab):
            #    processed[0] = (n_stab * dict_fix['r_d']) /\
            #       (9.55 * dict_fix['xi_f'] * sc.xi_gs[0] * dict_fix['s_f'])

            # print("engine speed after stab, ", n_i)
            # print("processed[0] after stab, ", processed[0])
            # print((n_stab * dict_fix['r_d']) /\
            #       (9.55 * dict_fix['xi_f'] * sc.xi_gs[0] * dict_fix['s_f']))


            if gear != sc.xi_gs[-1]:    # while not in the last gear
                # next gear engine speed
                # print("Processed[0], ", processed[0])
                n_next = sfc.engine_speed(processed[0], dict_fix['xi_f'],
                                       sc.xi_gs[posi+1], dict_fix['r_d'],
                                       dict_fix['s_f'], dict_fix['n_max'])
                
                # increase speed by timestep, within engine speed limits
                while (n_next <= min_lim):
                    # print("processed inside while, ", processed)
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

                    # print("n_next as control variable not in the last gear, ", n_next)
                    # print("processed[0], ", processed[0])
                    n_next = sfc.engine_speed(processed[0], dict_fix['xi_f'],
                                       sc.xi_gs[posi+1], dict_fix['r_d'],
                                       dict_fix['s_f'], dict_fix['n_max'])

            
            else:   # in the last gear
                # current engine speed
                n_i = sfc.engine_speed(processed[0], dict_fix['xi_f'],
                                       gear, dict_fix['r_d'],
                                       dict_fix['s_f'], dict_fix['n_max'])

                # increase speed by timestep up to MAX limit
                while (n_i <= n_max):
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
                    
                    n_i = sfc.engine_speed(processed[0], dict_fix['xi_f'],
                                       gear, dict_fix['r_d'],
                                       dict_fix['s_f'], dict_fix['n_max'])

                                            
                if (processed[0] < v_ref):
                    print("The final imposed speed is too high.")
                    exit()
                    
                                        
    # print("n_i as a control variable in the last gear, ", n_i)
    
    # deccelerated movement, starting from the current gear
    else:                

        for posi, gear in reversed(list(enumerate(sc.xi_gs[:(pos+1)]))):
            
            # print("deccelerated movement gears, ", gear)
            # print("current posi, ", posi)

            n_i = sfc.engine_speed(processed[0], dict_fix['xi_f'],
                                   gear, dict_fix['r_d'],
                                   dict_fix['s_f'], dict_fix['n_max'])
           
                                
            if (n_i > dict_fix['n_max']):
                print("The engine speed is too high. Please adjust!")
                exit()

            if(n_i < n_stab):
                continue

            if gear != sc.xi_gs[0]:    # while not in the first gear
                # backward (descending) next gear engine speed
                
                n_next = sfc.engine_speed(processed[0], dict_fix['xi_f'],
                                       sc.xi_gs[posi-1], dict_fix['r_d'],
                                       dict_fix['s_f'], dict_fix['n_max'])
                
                # print("n_next, ", n_next)

                # decrease speed by timestep, within engine speed limits
                while (n_next >= max_lim):
                    # print("processed inside while, ", processed)
                    processed[0] = processed[0] + tstep * processed[2]
                    processed[1] = gear
                    processed[3] = tstep

                    if (processed[0] <= v_ref):   # reached the end of sequence
                        processed[0] = v_ref
                        if (t_init % tstep > 0):
                            processed[3] = t_init % tstep
                        ret.append(processed[:])
                        return ret
                    
                    ret.append(processed[:])

                    # print("n_next as control variable not in the last gear, ", n_next)
                    # print("processed[0], ", processed[0])
                    n_next = sfc.engine_speed(processed[0], dict_fix['xi_f'],
                                       sc.xi_gs[posi-1], dict_fix['r_d'],
                                       dict_fix['s_f'], dict_fix['n_max'])

            
            else:   # in the first gear
                # current engine speed
                n_i = sfc.engine_speed(processed[0], dict_fix['xi_f'],
                                       gear, dict_fix['r_d'],
                                       dict_fix['s_f'], dict_fix['n_max'])

                # print("current gear is, ", gear)
                # print("current engine speed is, ", n_i)

                # decrease speed by timestep down to stable speed limit
                while (n_i >= n_stab):
                    processed[0] = processed[0] + tstep * processed[2]
                    processed[1] = gear
                    processed[3] = tstep

                    if (processed[0] <= v_ref):   # reached the end of sequence
                        processed[0] = v_ref
                        if (t_init % tstep > 0):
                            processed[3] = t_init % tstep

                        ret.append(processed[:])

                        return ret

                    ret.append(processed[:])
                    
                    n_i = sfc.engine_speed(processed[0], dict_fix['xi_f'],
                                       gear, dict_fix['r_d'],
                                       dict_fix['s_f'], dict_fix['n_max'])
                    #print("n_i as a control variable in the first gear, ", n_i)

                if (processed[0] > v_ref):
                    print("The final imposed speed is too low.")
                    exit()
                                                         

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

# print("expand, ", expand)

for sequence in low_raw:
    # if expand empty
    if not expand:
        # print("expand bool, ", not expand)
        # print("current sequence, ", sequence)
        expand.extend(process_input(raw_proc(sequence),
                                    raw_proc(sequence)[1]))
        print(expand)
        print("**********")

    else:   # use the previous sequence gear
        print("last gear, ", expand[-1][1])    
        expand.extend(process_input(raw_proc(sequence),
                                    expand[-1][1]))
        # print("current sequence, ", sequence)

        print(expand)
        print("**********")

#print(process_input(raw_proc(low_raw[0]), low_raw[0][1]))
# print(process_input(raw_proc(low_raw[1]), 1.211))
# print(process_input([3.333, 0, 0, 10], 5.503))

# print(process_input(raw_proc([12, 12, 0, 10]), 5.503))

#print("**********")
# print(expand)
