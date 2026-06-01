import numpy as np
from scipy.optimize import minimize
from src.inference.objective_function import objective_function


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