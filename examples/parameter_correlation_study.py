import numpy as np
from src.core.config import (
    CORRELATION_TRIALS,
    CORRELATION_NOISE_STD,
    CORRELATION_SEED,
    CORRELATION_DATA,
    CORRELATION_PLOT,
    mh,
    mc,
    Cph,
    Cpc,
    UA_true,
    y0,
    t_span,
    t_eval
)
from src.experiments.synthetic_data import generate_clean_data, add_noise
from src.inference.parameter_estimation_2param import estimate_UA_mh
from src.analysis.plotting import plot_parameter_correlation
from src.utils.data_export import save_table

def run_parameter_correlation_study():

    np.random.seed(CORRELATION_SEED)

    UA_estimates = []
    mh_estimates = []

    results = []

    for trial in range(CORRELATION_TRIALS):

        _, Th_true, Tc_true = generate_clean_data(
            mh,
            mc,
            Cph,
            Cpc,
            UA_true,
            y0,
            t_span,
            t_eval
        )

        Th_meas, Tc_meas = add_noise(
            Th_true,
            Tc_true,
            noise_std=CORRELATION_NOISE_STD
        )

        UA_est, mh_est = estimate_UA_mh(
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
        mh_estimates.append(mh_est)

        results.append(
            (
                trial + 1,
                UA_est,
                mh_est
            )
        )

    # Calculate Correlation Coefficient
    correlation = np.corrcoef(
        UA_estimates,
        mh_estimates
    )[0, 1]

    # Save Results
    headers = ["trial", "UA_est", "mh_est"]
    save_table(
        filename=CORRELATION_DATA,
        headers=headers,
        rows=results
    )
    
    # Plot Correlation
    plot_parameter_correlation(
        UA_estimates,
        mh_estimates,
        correlation,
        CORRELATION_PLOT
    )

    # Calculate and Print Statistics
    print("\nParameter Correlation Study")
    print("=" * 50)

    print(
        f"Correlation Coefficient: "
        f"{correlation:.4f}"
    )

    print(
        f"Mean UA Estimate: "
        f"{np.mean(UA_estimates):.2f} W/K"
    )

    print(
        f"Mean mh Estimate: "
        f"{np.mean(mh_estimates):.2f} kg"
    )

    print(f"UA Std Dev: {np.std(UA_estimates):.2f} W/K")
    print(f"mh Std Dev: {np.std(mh_estimates):.4f} kg")
    
    print(
        f"UA Relative Std Dev: "
        f"{100*np.std(UA_estimates)/UA_true:.2f}%"
    )
    print(
        f"mh Relative Std Dev: "
        f"{100*np.std(mh_estimates)/mh:.2f}%"
    )

    # Return Results
    return {
        "correlation": correlation,
        "UA_mean": np.mean(UA_estimates),
        "mh_mean": np.mean(mh_estimates),
        "UA_std": np.std(UA_estimates),
        "mh_std": np.std(mh_estimates)
    }