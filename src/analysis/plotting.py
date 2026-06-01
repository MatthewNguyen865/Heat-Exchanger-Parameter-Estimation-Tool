import matplotlib.pyplot as plt

def plot_results(time, Th, Tc):

    plt.plot(time, Th, label="Hot Fluid")
    plt.plot(time, Tc, label="Cold Fluid")

    plt.xlabel("Time (s)")
    plt.ylabel("Temperature (°C)")
    plt.title("Transient Heat Exchanger Response")

    plt.legend()
    plt.grid(True)

    plt.show()