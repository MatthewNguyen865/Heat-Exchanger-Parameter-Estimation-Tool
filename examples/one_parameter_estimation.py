import numpy as np
from src.core.config import (
    mh,
    mc,
    Cph,
    Cpc,
    UA_true,
    y0,
    t_span,
    t_eval,
    noise_std,
    random_seed,
    UA_initial,
    ESTIMATION_DATA,
    ESTIMATION_PLOT
)
from src.experiments.synthetic_data import generate_clean_data, add_noise
from src.inference.parameter_estimator import estimate_UA
from src.simulation.simulator import simulate_heat_exchanger
from src.analysis.plotting import plot_estimation_results
from src.analysis.metrics import percent_error
from src.utils.data_export import save_table

def run_one_parameter_estimation():
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
        random_seed=random_seed
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
        Tc_meas,
        UA_initial=UA_initial
    )

    # Simulate Estimated Model
    solution_est = simulate_heat_exchanger(
        mh,
        mc,
        Cph,
        Cpc,
        UA_est,
        y0,
        t_span,
        t_eval
    )

    Th_est = solution_est.y[0]
    Tc_est = solution_est.y[1]

    # Results
    print("\nParameter Estimation Results")
    print("-" * 35)

    print(f"True UA      : {UA_true:.2f} W/K")
    print(f"Estimated UA : {UA_est:.2f} W/K")

    error = percent_error(
        UA_true,
        UA_est
    )
    print(f"Percent Error: {error:.2f}%")

    # Save Results
    headers = ["UA_true", "UA_est", "Percent_error"]
    rows = [(UA_true, UA_est, error)]
    save_table(filename=ESTIMATION_DATA, headers=headers, rows=rows)

    # SSE
    residual_hot = np.sum((Th_meas - Th_est) ** 2)
    residual_cold = np.sum((Tc_meas - Tc_est) ** 2)

    print(f"SSE Hot : {residual_hot:.4f}")
    print(f"SSE Cold: {residual_cold:.4f}")

    # Plot Results
    plot_estimation_results(
        time,
        Th_true,
        Tc_true,
        Th_meas,
        Tc_meas,
        Th_est,
        Tc_est,
        filename=ESTIMATION_PLOT
    )

    # Return Results
    return {
        "UA_True": UA_true,
        "UA_est": UA_est,
        "SSE_hot": residual_hot,
        "SSE_cold": residual_cold,
        "SSE_total": residual_hot + residual_cold
    }