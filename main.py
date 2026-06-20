from examples.one_parameter_estimation import run_one_parameter_estimation
from examples.initial_guess_sensitivity_study import run_initial_guess_sensitivity_study
from examples.residual_analysis import run_residual_analysis
from examples.two_parameter_estimation import run_two_parameter_estimation
from examples.noise_sensitivity_study import run_noise_sensitivity_study
from examples.monte_carlo_estimation import run_monte_carlo_estimation
from examples.parameter_correlation_study import run_parameter_correlation_study
from examples.three_parameter_estimation import run_three_parameter_estimation

def main():

    run_one_parameter_estimation()
    
    run_noise_sensitivity_study()

    run_monte_carlo_estimation()

    run_initial_guess_sensitivity_study()

    run_residual_analysis()
    
    run_two_parameter_estimation()
    
    run_parameter_correlation_study()
    
    run_three_parameter_estimation()

if __name__ == "__main__":
    main()