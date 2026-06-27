from examples.one_parameter_estimation import run_one_parameter_estimation
from examples.two_parameter_estimation import run_two_parameter_estimation
from examples.three_parameter_estimation import run_three_parameter_estimation
from examples.noise_sensitivity_study import run_noise_sensitivity_study
from examples.initial_guess_sensitivity_study import run_initial_guess_sensitivity_study
from examples.monte_carlo_estimation import run_monte_carlo_estimation
from examples.residual_analysis import run_residual_analysis
from examples.parameter_correlation_study import run_parameter_correlation_study
from examples.model_comparison_study import run_model_comparison


EXPERIMENTS = {
    "one_parameter": run_one_parameter_estimation,
    "two_parameter": run_two_parameter_estimation,
    "three_parameter": run_three_parameter_estimation,
    "noise_sensitivity": run_noise_sensitivity_study,
    "initial_guess_sensitivity": run_initial_guess_sensitivity_study,
    "monte_carlo": run_monte_carlo_estimation,
    "residual_analysis": run_residual_analysis,
    "parameter_correlation": run_parameter_correlation_study,
    "model_comparison": run_model_comparison,
}

def run_experiment(experiment_name):
    """
    Run a selected experiment.
    """

    if experiment_name not in EXPERIMENTS:

        print("\nUnknown experiment.\n")

        print("Available experiments:")

        for name in EXPERIMENTS:
            print(f"  - {name}")

        return None

    print(f"\nRunning: {experiment_name}\n")

    return EXPERIMENTS[experiment_name]()