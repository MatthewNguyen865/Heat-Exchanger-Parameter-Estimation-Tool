import numpy as np
from src.analysis.plotting import plot_monte_carlo_histogram
from src.core.config import (
    MONTE_CARLO_DATA,
    MONTE_CARLO_PLOT,
    mh,
    mc,
    Cph,
    Cpc,
    UA_true,
    y0,
    t_span,
    t_eval,
    MONTE_CARLO_TRIALS,
    MONTE_CARLO_NOISE_STD,
    MONTE_CARLO_SEED
    )

from src.experiments.synthetic_data import generate_clean_data, add_noise
from src.inference.parameter_estimator import estimate_UA
from src.utils.data_export import save_table

def run_monte_carlo_estimation():
    np.random.seed(MONTE_CARLO_SEED)
    UA_estimates = []
    results = []
    for trial in range(MONTE_CARLO_TRIALS):
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
            noise_std=MONTE_CARLO_NOISE_STD,
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

        UA_estimates.append(UA_est)
        results.append((trial + 1, UA_est))

    # Save results
    save_table(
        filename=MONTE_CARLO_DATA,
        headers=[
            "iteration",
            "UA_estimate"
        ],
        rows=results
    )

    # Compute statistics
    std_UA = np.std(UA_estimates)
    mean_UA = np.mean(UA_estimates)
    min_UA = np.min(UA_estimates)
    max_UA = np.max(UA_estimates)

    mean_error = abs((mean_UA - UA_true) / UA_true) * 100

    # Print Results
    print("\nMonte Carlo Estimation Results:")
    print(f"Mean UA Estimate: {mean_UA:.2f} W/K")
    print(f"Standard Deviation: {std_UA:.2f} W/K")
    print(f"Min UA Estimate: {min_UA:.2f} W/K")
    print(f"Max UA Estimate: {max_UA:.2f} W/K")
    print(f"Mean Percent Error: {mean_error:.2f}%")

    # Plot histogram of estimates
    plot_monte_carlo_histogram(
        UA_estimates,
        UA_true,
        filename=MONTE_CARLO_PLOT
    )

    # Return results for further analysis if needed
    return {
        "mean": mean_UA,
        "std": std_UA,
        "min": min_UA,
        "max": max_UA,
        "mean_error": mean_error,
        "estimates": UA_estimates
    }