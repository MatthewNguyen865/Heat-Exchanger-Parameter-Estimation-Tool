import numpy as np
from scipy.integrate import solve_ivp
from heat_exchanger_model import heat_exchanger_odes

def simulate_heat_exchanger(mh, mc, Cph, Cpc, UA, y0, t_span, t_eval):

    solution = solve_ivp(
        heat_exchanger_odes,
        t_span,
        y0,
        args=(mh, mc, Cph, Cpc, UA),
        t_eval=t_eval
    )

    return solution