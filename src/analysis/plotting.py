import os
import matplotlib.pyplot as plt


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