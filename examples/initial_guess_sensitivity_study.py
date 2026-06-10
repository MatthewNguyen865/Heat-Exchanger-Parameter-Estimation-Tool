import numpy as np
from src.analysis.metrics import percent_error
from src.analysis.plotting import plot_initial_guess_sensitivity
from src.experiments.synthetic_data import add_noise, generate_clean_data
from src.core.config import (
    INITIAL_GUESS_DATA,
    INITIAL_GUESS_PLOT,
    initial_guesses,
    mh,
    mc,
    Cph,
    Cpc,
    UA_true,
    y0,
    t_span,
    t_eval,
    noise_std,
    random_seed
)
from src.inference.parameter_estimator import estimate_UA
from src.utils.data_export import save_table

def run_initial_guess_sensitivity_study():
    results = []
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
        noise_std=noise_std,
        random_seed=random_seed
    )

    for UA_initial in initial_guesses:

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

        error = percent_error(UA_true, UA_est)
        results.append((UA_initial, UA_est, error))
    
    errors = [result[2] for result in results]
    estimates = [result[1] for result in results]
    
    # Save results
    save_table(headers=["Initial UA", "Estimated UA", "Percent Error"], rows=results, filename=INITIAL_GUESS_DATA)

    # Plot results
    plot_initial_guess_sensitivity(initial_guesses, estimates, UA_true, INITIAL_GUESS_PLOT)

    print("\nInitial Guess Sensitivity Study Results")
    print("-" * 40)
    print(f"Number of Initial Guesses Tested: {len(initial_guesses)}")

    print(f"Minimum Estimated UA: {min(estimates):.2f} W/K")
    print(f"Maximum Estimated UA: {max(estimates):.2f} W/K")
    estimate_range = max(estimates) - min(estimates)
    print(
        f"Estimate Range: "
        f"{estimate_range:.4f} W/K"
    )
    print(f"Average Percent Error: {np.mean(errors):.4f}%")
