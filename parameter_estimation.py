import numpy as np
from scipy.optimize import minimize
from simulation import simulate_heat_exchanger

def objective_function(UA_guess,
                       mh, mc, Cph, Cpc,
                       y0, t_span, t_eval,
                       Th_meas, Tc_meas):

    solution = simulate_heat_exchanger(
        mh, mc, Cph, Cpc, UA_guess,
        y0, t_span, t_eval
    )

    Th_sim = solution.y[0]
    Tc_sim = solution.y[1]

    error = np.sum((Th_meas - Th_sim)**2 + (Tc_meas - Tc_sim)**2)

    return error

def estimate_UA(mh, mc, Cph, Cpc,
                y0, t_span, t_eval,
                Th_meas, Tc_meas,
                UA_initial=100.0):
    result = minimize(
        objective_function,
        x0=[UA_initial],
        args=(mh, mc, Cph, Cpc,
              y0, t_span, t_eval,
              Th_meas, Tc_meas),
        bounds=[(1, 5000)]
    )

    UA_est = result.x[0]

    return UA_est