import numpy as np
from src.experiments.synthetic_data import generate_clean_data, add_noise
from src.core.config import (
    mh,
    mc,
    Cph,
    Cpc,
    UA_true,
    y0,
    t_span,
    t_eval,
    random_seed
    )
from src.inference.parameter_estimator import estimate_UA
from src.analysis.metrics import percent_error
from src.utils.data_export import save_study_results
from src.core.config import NOISE_SENSITIVITY_DATA, NOISE_SENSITIVITY_PLOT
from src.analysis.plotting import plot_noise_sensitivity

def run_noise_sensitivity_study():
    noise_levels = [
        0.1,
        0.5,
        1.0,
        2.0,
        5.0
        ]

    results = []
    noise_values = []
    error_values = []

    np.random.seed(random_seed)

    for noise_std in noise_levels:
        print(f"\nRunning estimation with noise std = {noise_std} K")
        print("=" * 50)

        # Generate Clean Data
        time, Th_true, Tc_true = generate_clean_data(
            mh,
            mc,
            Cph,
            Cpc,
            UA_true,
            y0,
            t_span,
            t_eval
        )

        # Generate Synthetic Measurements
        Th_meas, Tc_meas = add_noise(
            Th_true,
            Tc_true,
            noise_std=noise_std,
        )

        # Estimate UA
        UA_est = estimate_UA(
            mh,
            mc,
            Cph,
            Cpc,
            y0,
            t_span,
            t_eval,
            Th_meas,
            Tc_meas
        )
        print(f"Estimated UA: {UA_est:.2f} W/K")

        # Compute Error
        error = percent_error(UA_true, UA_est)
        print(f"Percent Error: {error:.2f}%")

        # Store results
        results.append((noise_std, UA_true, UA_est, error))
        noise_values.append(noise_std)
        error_values.append(error)

    save_study_results(
        NOISE_SENSITIVITY_DATA,
        results
        )
    
    plot_noise_sensitivity(
    noise_values,
    error_values,
    filename=NOISE_SENSITIVITY_PLOT
)