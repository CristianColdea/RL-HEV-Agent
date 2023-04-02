"""
Script for Electric Generator (EG) Efficiency computation.
"""

import eem as em

def generator(eem_func):
    def em(T_inst, n_inst, n_max, T_cont, c_ovr, c_lb, P_rat, type='SPM',
           T_const=False, P_const=False):
        if (eem_func(T_inst, n_inst, n_max, T_cont, c_ovr, c_lb, P_rat,
                    type='SPM', T_const=False, P_const=False)[0] == True):
            return  (eem_func(T_inst, n_inst, n_max, T_cont, c_ovr, c_lb, P_rat,
                    type='SPM', T_const=False, P_const=False)[1],
                    ((T_inst * n_inst * (11 / 105000)) * eem_func(T_inst, n_inst,
                    n_max, T_cont, c_ovr, c_lb, P_rat, type='SPM',
                    T_const=False, P_const=False)[1]))
        else:
            print("Total power exceeding the rated one, i.e.",
                   T_inst * n_inst * (11 / 105000), "vs", P_rat, "kW")
            return 0,0

    return em

@generator
def eeg(T_inst, n_inst, n_max, T_cont, c_ovr, c_lb, P_rat, type='SPM',
        T_const=False, P_const=False):
    return em.eem(T_inst, n_inst, n_max, T_cont, c_ovr, c_lb, P_rat, type='SPM',
                  T_const=False, P_const=False)


# check the script with a function call
# print(eeg(104, 6180, 12000, 230, 1.08, 0.08, 75)) 
