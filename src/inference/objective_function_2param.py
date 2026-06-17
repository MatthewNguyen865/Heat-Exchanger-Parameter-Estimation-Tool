import numpy as np
from src.simulation.simulator import simulate_heat_exchanger

def objective_function_2param(
    params,
    mc,
    Cph,
    Cpc,
    y0,
    t_span,
    t_eval,
    Th_meas,
    Tc_meas
    ):

    UA_guess, mh_guess = params

    solution = simulate_heat_exchanger(
        mh_guess,
        mc,
        Cph,
        Cpc,
        UA_guess,
        y0,
        t_span,
        t_eval
    )

    Th_sim = solution.y[0]
    Tc_sim = solution.y[1]

    error = np.sum((Th_meas - Th_sim)**2 + (Tc_meas - Tc_sim)**2)

    return error