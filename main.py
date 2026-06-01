import numpy as np
from simulation import simulate_heat_exchanger
from plotting import plot_results

# Physical parameters
mh = 10.0
mc = 10.0
Cph = 4180.0
Cpc = 4180.0
UA = 500.0

# Initial conditions
Th0 = 80.0
Tc0 = 20.0
y0 = [Th0, Tc0]

# Time setup
t_span = (0, 2000)
t_eval = np.linspace(0, 2000, 100)

# Run simulation
solution = simulate_heat_exchanger(
    mh, mc, Cph, Cpc, UA,
    y0,
    t_span,
    t_eval
)

# Extract results
time = solution.t
Th = solution.y[0]
Tc = solution.y[1]

# Plot
plot_results(time, Th, Tc)