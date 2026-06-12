from examples.initial_guess_sensitivity_study import run_initial_guess_sensitivity_study
from examples.residual_analysis import run_residual_analysis
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
    ESTIMATION_PLOT,
    ESTIMATION_DATA)
from src.experiments.synthetic_data import generate_clean_data, add_noise
from src.inference.parameter_estimator import estimate_UA
from src.simulation.simulator import simulate_heat_exchanger
from src.analysis.plotting import plot_estimation_results
from src.analysis.metrics import percent_error
from src.utils.data_export import save_estimation_results
from examples.noise_sensitivity_study import run_noise_sensitivity_study
from examples.monte_carlo_estimation import run_monte_carlo_estimation

def main():

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

    save_estimation_results(
        filename=ESTIMATION_DATA,
        UA_true=UA_true,
        UA_est=UA_est,
        percent_error=error
    )

    print(f"Percent Error: {error:.2f}%")

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

    run_noise_sensitivity_study()

    run_monte_carlo_estimation()

    run_initial_guess_sensitivity_study()

    run_residual_analysis()

if __name__ == "__main__":
    main()