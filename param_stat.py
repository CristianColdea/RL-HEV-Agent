"""
Script to determine the current powertrain status parameters of interest,
per timestep.
"""

import simfc3.py as sfc

# Class to determine the whole bunch of parameters of interest

class Status:
    def __init__(self, v_init, a, tmstp, soc):
        self.v_init = v_init   #vehicle initial speed
        self.a = a   #vehicle acceleration
        self.tmstp = tmstp   #timestep
        self.soc = soc   #State of Charge

    # vehicle speed after applied acceleration during timestep

    def final_speed(v_init, a, tmstp):
        return (v_init + a * tmstp)

    # energy consumption in order to move the vehicle in certain conditions,
    # per timestep
    def e_exp():
