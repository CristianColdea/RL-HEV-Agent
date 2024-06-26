"""
Within this script the SFC script call is going to take place.
A total number of 19 variables are needed to be passed as
arguments to the classes and functions within SFC simulator.
Out of this total number of variables 15 are 'fixed', i.e., are
not changing with the conditions at agent/drive train level.
In order to simplify the SFC script invocation the 'fixed'
variables are to be passed as a list build only once.
As for the other mutable variables these must be passed
individually. Please read the explanatory document carefully to
understand which script are belonging to either category and the
order of arguments.
"""

import simfc6 as sfc
#import dyn_seq as dyn

#the 'fixed' vars list
fixs = []

# vehicle speed 
v_init = 4

# movement duration in seconds
t = 2 

# transmission final ratio (fixed)
xi_f = 3.961

fixs.append(xi_f)

# list of gearbox ratios
xi_gs = [5.503, 3.333, 2.315, 1.661, 1.211, 1.0, 0.717, 0.65, 0.601]

# gearbox ratio
xi_g = 5.503

# slip factor (fixed)
s_f = 1.05

fixs.append(s_f)

# wheel rolling radius (fixed)
r_d = 0.317

fixs.append(r_d)

# engine maximum speed (fixed)
n_max = 5000

fixs.append(n_max)

# engine maximum output/power (fixed)
P_max = 147

fixs.append(P_max)

# engine type (fixed)
type = 'CIE'

fixs.append(type)

# transmission overall efficiency (fixed)
eta_t = 0.95

fixs.append(eta_t)

# engine peak efficiency (fixed)
eta_max = 0.4

fixs.append(eta_max)

# vehicle mass (fixed)
m_a = 2355

fixs.append(m_a)

# rolling resistance coefficient (fixed)
c_r = 0.009

fixs.append(c_r)

# coefficient of aerodynamic drag (wind coefficient) (fixed)
C_d = 0.28

fixs.append(C_d)

# vehicle frontal area (fixed)
A_f = 2.19

fixs.append(A_f)

# air density (fixed)
ro_a = 1.225

fixs.append(ro_a)

# acceleration
a = 0 

# diesel fuel calorific value, J/l (fixed)
Q_f = 37200000

fixs.append(Q_f)

# diesel fuel density (fixed)
ro_f = 0.846

fixs.append(ro_f)

if len(fixs) != 15:
    print("The total number of 'fixed' variables is incorrect!\n"
           "There must be 15 'fixed' variables, you collected: ",len(fixs))
    exit()
# ==========

#print(sfc.unpack_f(fixs))
#print(sfc.unpack_d([0, 3.6, 0.6, 2]))
"""
SFC simulator call and results return
"""

# list to store tuple results
#list_res = []

# append the dynamic variables
#dyns = []
#dyns.append(v_init)
#dyns.append(xi_gs[2])
#dyns.append(a)
#dyns.append(t)

#csfc = sfc.simfc_call(fixs, dyns)

#print("The 100 km fuel consumption is: ", csfc[0], "l/100 km")
#print("The hourly fuel consumption is: ", csfc[1], "kg/h")
#print("The specific fuel consumption is: ",csfc[2], "kg/kWh")
