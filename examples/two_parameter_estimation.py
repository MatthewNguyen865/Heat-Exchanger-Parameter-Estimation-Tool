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
    TWO_PARAMETER_PLOT,
    TWO_PARAMETER_DATA
)
from src.inference.parameter_estimation_2param import estimate_UA_mh
from src.utils.data_export import save_table
from src.analysis.plotting import plot_two_parameter_estimation
from src.simulation.simulator import simulate_heat_exchanger

def run_two_parameter_estimation():
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

    # Estimate UA and mh
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

    # Simulate heat exchanger with estimated parameters
    solution_est = simulate_heat_exchanger(
        mh_est,
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

    # Calculate Percent Errors
    UA_error = percent_error(UA_true, UA_est)
    mh_error = percent_error(mh, mh_est)

    # Save Results
    headers = ["UA_true", "UA_est", "UA_percent_error", "mh_true", "mh_est", "mh_percent_error"]
    rows = [(UA_true, UA_est, UA_error, mh, mh_est, mh_error)]
    
    save_table(filename=TWO_PARAMETER_DATA, headers=headers, rows=rows)

    # Plot Results
    plot_two_parameter_estimation(
        time,
        Th_true,
        Tc_true,
        Th_meas,
        Tc_meas,
        Th_est,
        Tc_est,
        UA_est,
        mh_est,
        filename=TWO_PARAMETER_PLOT
    )


    print("Two-Parameter Estimation Results")
    print("=" * 50)

    print(f"True UA: {UA_true:.2f} W/K")
    print(f"Estimated UA: {UA_est:.2f} W/K")
    print(f"Percent Error UA: {UA_error:.2f}%")

    print(f"True mh: {mh:.2f} kg")
    print(f"Estimated mh: {mh_est:.2f} kg")
    print(f"Percent Error mh: {mh_error:.2f}%")