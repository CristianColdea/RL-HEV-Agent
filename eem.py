"""
Script for Electric Motor (EM) Efficiency computation.
"""

#import sys

def eem(T_inst, n_inst, n_max, T_cont, c_ovr, c_lb, P_rat, type='SPM',
        T_const=False, P_const=False):
    """
    Function to compute efficiency based on regression.
    Takes as inputs instantaneous torque, in Newton x meter,
    instantaneous speed, in krpm, maximum speed, in krpm,
    continous torque, in Newton x meter,
    overload torque capability as coefficient of the continous torque,
    maximum loss as coefficient of the  rated power,
    rated power, in kW, EM type, wether the motor works in constant
    torque or power regime.
    Outputs whether the inputed torque and speed isnt't exceeding
    the rated power, and the EM efficiency on the given conditions.
    """

    # compute overload torque
    T_ovr = c_ovr * T_cont

    # check for the instantaneous torque in relation to overload
    if(T_inst > T_ovr):
        return(bool(T_inst < T_ovr), 0)
   
    # check for the instantantaneous speed in relation to max
    if(n_inst > n_max):
        return(bool(n_inst < n_max), 0)
                    
    T = T_inst / T_ovr
    n = n_inst / n_max
    
    if(T_const or P_const):  # if EM is under constant torque or power regimes
        if(type == 'IPM'):
            # loss for the constant torque working regime
            if(T_const):
                loss = (-0.004 + (0.117 * n) + (0.175 * T) - 
                       (0.316 * (n**2)) - (0.028 * T * n) + (0.64 * (T**2)) +
                       (0.131 * (n**3)) + (0.8 * (n**2) * T) -
                       (0.034 * (T**2) * n) + (0.084 * (T**3)))
            # loss for the constant power working regime
            if(P_const):
                loss = (0.103 - (0.647 * n) + (0.958 * T) + (1.2 * (n**2)) -
                       (1.547 * T * n) - (0.944 * (T**2)) -
                       (0.626 * (n**3)) + (0.728 * (n**2) * T) +
                       (1.466 * (T**2) * n) + (1.008 * (T**3)))
        else: print("Two equation fitting is computed for IPM motor type only.")
    else:
        if(type == 'SPM'):
            loss = (-0.002 + (0.175 * n) - (0.065 * T) + (0.181 * (n**2)) +
                   (0.577 * T * n) + (0.697 * (T**2)) + (0.443 * (n**3)) -
                   (0.542 * (n**2) * T) - (1.043 * (T**2) * n) +
                   (0.942 * (T**3)))
        if(type == 'IPM'):
            loss = (-0.033 + (0.239 * n) + (0.47 * T) - (0.334 * (n**2)) -
                   (1.022 * T * n) + (0.103 * (T**2)) + (0.171 * (n**3)) +
                   (0.534 * (n**2) * T) + (1.071 * (T**2) * n) +
                   (0.339 * (T**3)))

    #print("The loss is: ", (c_lb * P_rat * loss), " [kW]")
    #print("The instantaneous power is ", (T_inst * n_inst * (11 / 105000)), " [kW]")
       
    return(bool(T_inst * n_inst * (11 / 105000) < P_rat),
          ((T_inst * n_inst * (11 / 105000)) /  
          (T_inst * n_inst * (11 / 105000) + (c_lb * P_rat * loss))))

# check the script with a function call
#print(eem(230, 3180, 12000, 230, 1.08, 0.08, 75)) 
