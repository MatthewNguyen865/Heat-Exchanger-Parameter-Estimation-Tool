from scipy.optimize import minimize
from src.inference.objective_function_2param import objective_function_2param

def estimate_UA_mh(
    mc,
    Cph,
    Cpc,
    y0,
    t_span,
    t_eval,
    Th_meas,
    Tc_meas,
    UA_initial=300,
    mh_initial=8
    ):

    result = minimize(
        objective_function_2param,
        x0=[UA_initial, mh_initial],
        args=(
            mc,
            Cph,
            Cpc,
            y0,
            t_span,
            t_eval,
            Th_meas,
            Tc_meas
        ),
        bounds=[
            (1, 5000),
            (1, 50)
        ]
    )

    UA_est = result.x[0]
    mh_est = result.x[1]

    return UA_est, mh_est