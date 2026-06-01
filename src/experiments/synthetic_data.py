import numpy as np
from src.simulation.simulator import simulate_heat_exchanger

def generate_clean_data(mh, mc, Cph, Cpc, UA,
                        y0, t_span, t_eval):

    solution = simulate_heat_exchanger(
        mh, mc, Cph, Cpc, UA,
        y0, t_span, t_eval
    )

    time = solution.t
    Th = solution.y[0]
    Tc = solution.y[1]

    return time, Th, Tc

def add_noise(Th, Tc, noise_std=0.5, random_seed=None):
    if random_seed is not None:
        np.random.seed(random_seed)

    Th_noisy = Th + np.random.normal(
        loc=0,
        scale=noise_std,
        size=len(Th)
    )

    Tc_noisy = Tc + np.random.normal(
        loc=0,
        scale=noise_std,
        size=len(Tc)
    )

    return Th_noisy, Tc_noisy