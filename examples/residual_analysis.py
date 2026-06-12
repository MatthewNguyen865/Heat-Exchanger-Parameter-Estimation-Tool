import numpy as np
from src.experiments.synthetic_data import add_noise, generate_clean_data
from src.core.config import (
    RESIDUAL_ANALYSIS_DATA,
    RESIDUAL_ANALYSIS_PLOT,
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
from src.simulation.simulator import simulate_heat_exchanger
from src.analysis.metrics import rmse
from src.utils.data_export import save_table
from src.analysis.plotting import plot_residuals

def run_residual_analysis():
    
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
        noise_std,
        random_seed
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

    # Simulate Estimated Model
    solution = simulate_heat_exchanger(
        mh,
        mc,
        Cph,
        Cpc,
        UA_est,
        y0,
        t_span,
        t_eval
    )
    Th_est = solution.y[0]
    Tc_est = solution.y[1]

    # Compute Residuals
    hot_residuals = Th_meas - Th_est
    cold_residuals = Tc_meas - Tc_est

    # Compute Root Mean Square Error (RMSE)
    hot_rmse = rmse(Th_meas, Th_est)
    cold_rmse = rmse(Tc_meas, Tc_est)

    print("\nResidual Analysis Results")
    print("=" * 35)
    print(f"Hot-Side RMSE : {hot_rmse:.4f} °C")
    print(f"Cold-Side RMSE: {cold_rmse:.4f} °C")
    print(
        f"Mean Hot Residual : "
        f"{np.mean(hot_residuals):.4f} °C"
    )
    print(
        f"Mean Cold Residual: "
        f"{np.mean(cold_residuals):.4f} °C"
    )
    print(
    f"Maximum Absolute Hot Residual : "
    f"{np.max(np.abs(hot_residuals)):.4f} °C"
    )
    print(
        f"Maximum Absolute Cold Residual : "
        f"{np.max(np.abs(cold_residuals)):.4f} °C"
    )

    # Save results
    headers = ["time", "hot_residual", "cold_residual"]
    rows = list(zip(time, hot_residuals, cold_residuals))
    save_table(headers=headers, rows=rows, filename=RESIDUAL_ANALYSIS_DATA)

    # Plot residuals
    plot_residuals(time, hot_residuals, cold_residuals, RESIDUAL_ANALYSIS_PLOT)