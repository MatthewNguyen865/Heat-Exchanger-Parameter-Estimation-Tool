import numpy as np
from src.analysis.metrics import percent_error
from src.experiments.synthetic_data import add_noise, generate_clean_data
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
    THREE_PARAMETER_PLOT,
    THREE_PARAMETER_DATA
)
from src.inference.parameter_estimation_3param import estimate_UA_mh_mc
from src.utils.data_export import save_table
from src.analysis.plotting import plot_three_parameter_estimation
from src.simulation.simulator import simulate_heat_exchanger

def run_three_parameter_estimation(save_results=True, create_plots=True, print_results=True):
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

    # Add Noise
    Th_meas, Tc_meas = add_noise(
        Th_true,
        Tc_true,
        noise_std=noise_std,
        random_seed=random_seed
    )

    # Estimate UA, mh, and mc
    UA_est, mh_est, mc_est = estimate_UA_mh_mc(
        Cph,
        Cpc,
        y0,
        t_span,
        t_eval,
        Th_meas,
        Tc_meas
    )

    # Simulate heat exchanger with estimated parameters
    solution_est = simulate_heat_exchanger(
        mh_est,
        mc_est,
        Cph,
        Cpc,
        UA_est,
        y0,
        t_span,
        t_eval
    )

    Th_est = solution_est.y[0]
    Tc_est = solution_est.y[1]

    # Calculate Percent Errors
    UA_error = percent_error(UA_true, UA_est)
    mh_error = percent_error(mh, mh_est)
    mc_error = percent_error(mc, mc_est)

    # Save Results
    headers = [
        "UA_true", 
        "UA_est", 
        "UA_percent_error", 
        "mh_true", 
        "mh_est", 
        "mh_percent_error", 
        "mc_true", 
        "mc_est", 
        "mc_percent_error"
        ]
    rows = [(UA_true, UA_est, UA_error, mh, mh_est, mh_error, mc, mc_est, mc_error)]
    if save_results:
        save_table(THREE_PARAMETER_DATA, headers=headers, rows=rows)

    # Plot Results
    if create_plots:
        plot_three_parameter_estimation(
            time,
            Th_true,
            Tc_true,
            Th_meas,
            Tc_meas,
            Th_est,
            Tc_est,
            THREE_PARAMETER_PLOT
        )

    # SSE
    residual_hot = np.sum((Th_meas - Th_est) ** 2)
    residual_cold = np.sum((Tc_meas - Tc_est) ** 2)

    # Print Results with Statistics
    if print_results:
        print("\nThree-Parameter Estimation Results")
        print("=" * 50)

        print(f"True UA: {UA_true:.2f} W/K")
        print(f"Estimated UA: {UA_est:.2f} W/K")
        print(f"Percent Error UA: {UA_error:.2f}%")
        print()

        print(f"True mh: {mh:.2f} kg/s")
        print(f"Estimated mh: {mh_est:.2f} kg/s")
        print(f"Percent Error mh: {mh_error:.2f}%")
        print()

        print(f"True mc: {mc:.2f} kg/s")
        print(f"Estimated mc: {mc_est:.2f} kg/s")
        print(f"Percent Error mc: {mc_error:.2f}%")

        print(f"SSE Hot : {residual_hot:.4f}")
        print(f"SSE Cold: {residual_cold:.4f}")

        # Identifiability Diagnostics
        print("\nIdentifiability Diagnostics")
        print("-" * 40)

        print(f"UA/mh true: {UA_true / mh:.2f}")
        print(f"UA/mh est : {UA_est / mh_est:.2f}")

        print(f"UA/mc true: {UA_true / mc:.2f}")
        print(f"UA/mc est : {UA_est / mc_est:.2f}")

        print(
            f"Max Hot Temp Difference: "
            f"{max(abs(Th_true - Th_est)):.6f}"
        )

        print(
            f"Max Cold Temp Difference: "
            f"{max(abs(Tc_true - Tc_est)):.6f}"
        )

    # Return Results
    return {
        "UA_est": UA_est,
        "UA_error": UA_error,
        "mh_est": mh_est,
        "mh_error": mh_error,
        "mc_est": mc_est,
        "mc_error": mc_error,
        "SSE_hot": residual_hot,
        "SSE_cold": residual_cold,
        "SSE_total": residual_hot + residual_cold
    }