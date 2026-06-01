import numpy as np

from src.experiments.synthetic_data import (
    generate_clean_data,
    add_noise
)

from src.inference.parameter_estimator import estimate_UA

from src.simulation.simulator import simulate_heat_exchanger

from src.analysis.plotting import plot_results


# Physical parameters
mh = 10.0
mc = 10.0

Cph = 4180.0
Cpc = 4180.0

UA_true = 500.0

# Initial conditions
Th0 = 80.0
Tc0 = 20.0

y0 = [Th0, Tc0]

# Time setup
t_span = (0, 2000)
t_eval = np.linspace(0, 2000, 100)

# Generate synthetic data
time, Th_true, Tc_true = generate_clean_data(
    mh, mc, Cph, Cpc,
    UA_true,
    y0,
    t_span,
    t_eval
)

# Add noise
Th_meas, Tc_meas = add_noise(
    Th_true,
    Tc_true,
    noise_std=0.5,
    random_seed=42
)

# Estimate UA
UA_est = estimate_UA(
    mh, mc, Cph, Cpc,
    y0,
    t_span,
    t_eval,
    Th_meas,
    Tc_meas,
    UA_initial=300.0
)

print(f"True UA      = {UA_true:.2f}")
print(f"Estimated UA = {UA_est:.2f}")

# Simulate using estimated UA
solution_est = simulate_heat_exchanger(
    mh, mc, Cph, Cpc,
    UA_est,
    y0,
    t_span,
    t_eval
)

Th_est = solution_est.y[0]
Tc_est = solution_est.y[1]

# Plot results
plot_results(
    time,
    Th_true,
    Tc_true,
    Th_est,
    Tc_est
)