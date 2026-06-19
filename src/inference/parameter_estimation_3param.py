from scipy.optimize import minimize
from src.inference.objective_function_3param import objective_function_3param
from src.core.config import (
    UA_initial_3param, 
    mh_initial_3param, 
    mc_initial_3param
    )

def estimate_UA_mh_mc(
    Cph,
    Cpc,
    y0,
    t_span,
    t_eval,
    Th_meas,
    Tc_meas,
    UA_initial=UA_initial_3param,
    mh_initial=mh_initial_3param,
    mc_initial=mc_initial_3param
    ):
    """
    Estimate:

        UA
        mh
        mc

    using nonlinear least squares optimization.
    """

    initial_guess = [
        UA_initial,
        mh_initial,
        mc_initial
    ]

    bounds = [
        (1.0, 5000.0),   # UA
        (1.0, 50.0),     # mh
        (1.0, 50.0)      # mc
    ]

    result = minimize(
        objective_function_3param,
        x0=initial_guess,
        args=(
            Cph,
            Cpc,
            y0,
            t_span,
            t_eval,
            Th_meas,
            Tc_meas
        ),
        bounds=bounds
    )

    UA_est = result.x[0]
    mh_est = result.x[1]
    mc_est = result.x[2]

    return (
        UA_est,
        mh_est,
        mc_est
    )