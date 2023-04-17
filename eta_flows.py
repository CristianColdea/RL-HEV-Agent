"""
Script to compute each elementary power flow efficiency.
For further details please see flows_efficiencies_rewards.md file
"""

def flow1(pinput, sfc, eta_trans = 0.95, q_i = 41.84):
    """
    Function to compute overall efficiency from ICE to the wheels.
    Takes as inputs the input power, specific fuel consumption, in g/kWh,
    overall transmission efficiency,
    and fuel burning value, in MJ/kg (for gasoline just use 43.93).
    Returns a tuple with the delivered power
    and the efficiency of the power flow.
    """

    eta_ice = 3600 / (sfc * 41.84)
    
    return (pinput * eta_ice * eta_trans), (eta_ice * eta_trans)

def flow2(pinput, eta_dch=0.89, eta_inv=0.9, eta_trans=0.98, eta_EM):
    """
    Function to compute overall efficiency from battery to the wheels,
    via EM.
    Takes as inputs the input power, in kW, the discharge efficiency,
    the inverter unit overall efficiency, EM gear ratio efficiency,
    and the EM efficiency.
    Returns a tuple with the delivered power
    and the efficiency of the power flow.
    """

    return (pinput * eta_dch * eta_inv * eta_trans * eta_EM),\
           (eta_dch * eta_inv * eta_trans * eta_EM)

def flow3(pinput, eta_trans=0.985, eta_EG, eta_rectif=0.92, eta_ch=0.88):
    return
