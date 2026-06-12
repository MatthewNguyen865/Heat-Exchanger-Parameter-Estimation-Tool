import os
import numpy as np

# Physical Parameters
mh = 10.0
mc = 10.0

Cph = 4180.0
Cpc = 4180.0

UA_true = 500.0

# Initial Conditions
Th0 = 80.0
Tc0 = 20.0

y0 = [Th0, Tc0]

# Simulation Settings
t_start = 0
t_end = 2000
n_points = 100

t_span = (t_start, t_end)
t_eval = np.linspace(t_start, t_end, n_points)

# Synthetic Data Settings
noise_std = 0.5
random_seed = 42

# Monte Carlo Settings
MONTE_CARLO_TRIALS = 100
MONTE_CARLO_NOISE_STD = 1.0
MONTE_CARLO_SEED = 42


# Initial Guess Sensitivity Settings
initial_guesses = [
    50,
    100,
    200,
    300,
    500,
    1000,
    2000
    ]

# Estimation Settings
UA_initial = 300.0

UA_lower_bound = 1.0
UA_upper_bound = 5000.0

# Output Directories
PLOTS_DIR = "results/plots"
DATA_DIR = "results/data"

os.makedirs(PLOTS_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)

# Output Files
ESTIMATION_PLOT = (
    f"{PLOTS_DIR}/parameter_estimation.png"
)

ESTIMATION_DATA = (
    f"{DATA_DIR}/parameter_estimation_results.csv"
)

NOISE_SENSITIVITY_PLOT = (
    f"{PLOTS_DIR}/noise_sensitivity_study.png"
)

NOISE_SENSITIVITY_DATA = (
    f"{DATA_DIR}/noise_sensitivity_study.csv"
)

MONTE_CARLO_PLOT = (
    f"{PLOTS_DIR}/monte_carlo_histogram.png"
)

MONTE_CARLO_DATA = (
    f"{DATA_DIR}/monte_carlo_estimation.csv"
)

INITIAL_GUESS_PLOT = (
    f"{PLOTS_DIR}/initial_guess_sensitivity_study.png"
)

INITIAL_GUESS_DATA = (
    f"{DATA_DIR}/initial_guess_sensitivity_study.csv"
)

RESIDUAL_ANALYSIS_PLOT = (
    f"{PLOTS_DIR}/residual_analysis.png"
)

RESIDUAL_ANALYSIS_DATA = (
    f"{DATA_DIR}/residual_analysis.csv"
)