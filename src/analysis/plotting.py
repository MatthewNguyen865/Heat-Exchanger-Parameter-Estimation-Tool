import os
import matplotlib.pyplot as plt

def set_plotting_style():
    """
    Apply a consistent plotting style
    across the project.
    """

    plt.style.use("default")

    plt.rcParams["figure.figsize"] = (8, 5)

    plt.rcParams["axes.grid"] = True

    plt.rcParams["font.size"] = 11

    plt.rcParams["axes.titlesize"] = 14

    plt.rcParams["axes.labelsize"] = 12

    plt.rcParams["legend.fontsize"] = 10


def plot_estimation_results(
    time,
    Th_true,
    Tc_true,
    Th_meas,
    Tc_meas,
    Th_est,
    Tc_est,
    filename=None
    ):
    
    set_plotting_style()
    plt.figure(figsize=(10, 6))

    # True temperature profiles
    plt.plot(time, Th_true, linewidth=2, label="True Hot Temperature")
    plt.plot(time, Tc_true, linewidth=2, label="True Cold Temperature")

    # Measured temperatures
    plt.scatter(time, Th_meas, s=20, label="Measured Hot Temperature")
    plt.scatter(time, Tc_meas, s=20, label="Measured Cold Temperature")

    # Estimated model
    plt.plot(time, Th_est, "--", linewidth=2, label="Estimated Hot Temperature")
    plt.plot(time, Tc_est, "--", linewidth=2, label="Estimated Cold Temperature")

    # Formatting
    plt.xlabel("Time (s)")
    plt.ylabel("Temperature (°C)")
    plt.title("Heat Exchanger Parameter Estimation")

    plt.legend()
    plt.grid(True)

    # Save figure
    if filename is not None:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        plt.savefig(filename, dpi=300, bbox_inches="tight")

    plt.show()


def plot_noise_sensitivity(
    noise_levels,
    percent_errors,
    filename=None
):
    """
    Plot noise level vs parameter estimation error.
    """

    set_plotting_style()
    plt.figure()

    plt.plot(
        noise_levels,
        percent_errors,
        marker="o"
    )

    plt.xlabel("Noise Standard Deviation (°C)")
    plt.ylabel("Percent Error (%)")
    plt.title("Noise Sensitivity Study")

    plt.grid(True)

    if filename is not None:
        os.makedirs(
            os.path.dirname(filename),
            exist_ok=True
        )
        plt.savefig(filename)

    plt.show()


def plot_monte_carlo_histogram(
    UA_estimates,
    UA_true,
    filename=None
):
    """
    Plot histogram of Monte Carlo UA estimates.
    """

    set_plotting_style()

    plt.figure()

    plt.hist(
        UA_estimates,
        bins=15
    )

    plt.axvline(
        UA_true,
        linestyle="--",
        label=f"True UA = {UA_true:.2f}"
    )

    plt.xlabel("Estimated UA (W/K)")
    plt.ylabel("Frequency")
    plt.title("Monte Carlo Parameter Estimation")

    plt.legend()

    if filename is not None:

        os.makedirs(
            os.path.dirname(filename),
            exist_ok=True
        )

        plt.savefig(filename)

    plt.show()


def plot_initial_guess_sensitivity(
    initial_guesses,
    estimated_values,
    UA_true,
    filename=None
    ):
    """
    Plot optimizer sensitivity to initial UA guesses.
    """

    set_plotting_style()

    plt.figure()

    plt.plot(
        initial_guesses,
        estimated_values,
        marker="o",
        label="Estimated UA"
    )

    plt.axhline(
        UA_true,
        linestyle="--",
        label=f"True UA = {UA_true:.2f} W/K"
    )

    plt.ylim(UA_true - 10, UA_true + 10)

    plt.xlabel("Initial UA Guess (W/K)")
    plt.ylabel("Estimated UA (W/K)")
    plt.title("Initial Guess Sensitivity Study")

    plt.legend()
    plt.grid(True)

    if filename is not None:

        os.makedirs(
            os.path.dirname(filename),
            exist_ok=True
        )

        plt.savefig(filename)

    plt.show()


def plot_residuals(
    time,
    hot_residuals,
    cold_residuals,
    filename=None
    ):
    """
    Plot residuals versus time.
    """

    set_plotting_style()

    plt.figure(figsize=(8, 5))

    plt.scatter(
        time,
        hot_residuals,
        label="Hot Side Residuals",
        s=20
    )
    plt.scatter(
        time,
        cold_residuals,
        label="Cold Side Residuals",
        s=20
    )

    plt.axhline(
        y=0,
        linestyle="--",
        linewidth=1
    )

    plt.xlabel("Time (s)")
    plt.ylabel("Residual (°C)")
    plt.title("Residual Analysis")

    plt.legend()
    plt.grid(True)

    if filename is not None:

        os.makedirs(
            os.path.dirname(filename),
            exist_ok=True
        )

        plt.savefig(filename)

    plt.show()

def plot_two_parameter_estimation(
    time,
    Th_true,
    Tc_true,
    Th_meas,
    Tc_meas,
    Th_est,
    Tc_est,
    UA_est,
    mh_est,
    filename
    ):
    """
    Plot measured, true, and estimated
    temperature trajectories for
    two-parameter estimation.
    """
    set_plotting_style()

    plt.figure(figsize=(10, 6))

    # True trajectories
    plt.plot(
        time,
        Th_true,
        label="True Hot Temperature"
    )

    plt.plot(
        time,
        Tc_true,
        label="True Cold Temperature"
    )

    # Noisy measurements
    plt.scatter(
        time,
        Th_meas,
        s=15,
        alpha=0.7,
        label="Measured Hot Temperature"
    )

    plt.scatter(
        time,
        Tc_meas,
        s=15,
        alpha=0.7,
        label="Measured Cold Temperature"
    )

    # Estimated trajectories
    plt.plot(
        time,
        Th_est,
        "--",
        linewidth=2,
        label="Estimated Hot Temperature"
    )

    plt.plot(
        time,
        Tc_est,
        "--",
        linewidth=2,
        label="Estimated Cold Temperature"
    )

    plt.xlabel("Time (s)")
    plt.ylabel("Temperature (°C)")

    plt.title(
        "Two-Parameter Estimation\n"
        f"Estimated UA = {UA_est:.2f} W/K, "
        f"Estimated mh = {mh_est:.2f} kg"
    )

    plt.legend()
    plt.grid(True)

    if filename is not None:
        os.makedirs(
            os.path.dirname(filename),
            exist_ok=True
        )
        
        plt.savefig(filename)

    plt.show()

def plot_parameter_correlation(
    UA_estimates,
    mh_estimates,
    correlation,
    filename=None
    ):
    """
    Plot estimated UA versus estimated mh.
    """

    set_plotting_style()

    plt.figure(figsize=(8, 5))

    plt.scatter(
        UA_estimates,
        mh_estimates,
        s=20
    )

    plt.xlabel("Estimated UA (W/K)")
    plt.ylabel("Estimated mh (kg)")

    plt.title(
        "Parameter Correlation Study\n"
        f"Correlation = {correlation:.3f}"
    )

    plt.grid(True)

    if filename is not None:

        os.makedirs(
            os.path.dirname(filename),
            exist_ok=True
        )

        plt.savefig(filename)

    plt.show()

def plot_three_parameter_estimation(
    time,
    Th_true,
    Tc_true,
    Th_meas,
    Tc_meas,
    Th_est,
    Tc_est,
    filename=None
):
    """
    Plot three-parameter estimation results.
    """

    set_plotting_style()

    plt.figure(figsize=(8, 5))

    plt.plot(
        time,
        Th_true,
        label="True Hot Temperature"
    )

    plt.plot(
        time,
        Tc_true,
        label="True Cold Temperature"
    )

    plt.scatter(
        time,
        Th_meas,
        s=20,
        label="Measured Hot Temperature"
    )

    plt.scatter(
        time,
        Tc_meas,
        s=20,
        label="Measured Cold Temperature"
    )

    plt.plot(
        time,
        Th_est,
        linestyle="--",
        label="Estimated Hot Temperature"
    )

    plt.plot(
        time,
        Tc_est,
        linestyle="--",
        label="Estimated Cold Temperature"
    )

    plt.xlabel("Time (s)")
    plt.ylabel("Temperature (°C)")
    plt.title("Three-Parameter Estimation")

    plt.legend()
    plt.grid(True)

    if filename is not None:

        os.makedirs(
            os.path.dirname(filename),
            exist_ok=True
        )

        plt.savefig(filename)

    plt.show()