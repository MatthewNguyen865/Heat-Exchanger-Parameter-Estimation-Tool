from examples.one_parameter_estimation import run_one_parameter_estimation
from examples.two_parameter_estimation import run_two_parameter_estimation
from examples.three_parameter_estimation import run_three_parameter_estimation
from src.utils.data_export import save_table
from src.core.config import MODEL_COMPARISON_DATA, MODEL_COMPARISON_PLOT
from src.analysis.plotting import plot_model_comparison

def run_model_comparison():

    r1 = run_one_parameter_estimation()
    r2 = run_two_parameter_estimation()
    r3 = run_three_parameter_estimation()

    # Store Results
    results = [
    (
        "One Parameter",
        r1["SSE_hot"],
        r1["SSE_cold"],
        r1["SSE_total"]
    ),
    (
        "Two Parameter",
        r2["SSE_hot"],
        r2["SSE_cold"],
        r2["SSE_total"]
    ),
    (
        "Three Parameter",
        r3["SSE_hot"],
        r3["SSE_cold"],
        r3["SSE_total"]
    )
    ]

    # Save Results
    save_table(
        filename=MODEL_COMPARISON_DATA,
        headers=[
            "Study",
            "SSE_Hot",
            "SSE_Cold",
            "SSE_Total"
        ],
        rows=results
    )

    # Plot Total SSE
    plot_model_comparison(
        ["One Parameter", "Two Parameter", "Three Parameter"],
        [
            r1["SSE_total"],
            r2["SSE_total"],
            r3["SSE_total"]
        ],
        MODEL_COMPARISON_PLOT
    )

    # Print Results
    print("\nModel Comparison Study")
    print("=" * 50)

    print(
        f"One-Parameter SSE   : "
        f"{r1['SSE_total']:.4f}"
    )

    print(
        f"Two-Parameter SSE   : "
        f"{r2['SSE_total']:.4f}"
    )

    print(
        f"Three-Parameter SSE : "
        f"{r3['SSE_total']:.4f}"
    )

    improvement_12 = (
        (r1["SSE_total"] - r2["SSE_total"])
        / r1["SSE_total"]
        * 100
    )

    improvement_23 = (
        (r2["SSE_total"] - r3["SSE_total"])
        / r2["SSE_total"]
        * 100
    )

    print()
    print(
        f"Improvement (1→2 Parameters): "
        f"{improvement_12:.2f}%"
    )

    print(
        f"Improvement (2→3 Parameters): "
        f"{improvement_23:.2f}%"
    )

    # Possible Interpretation
    if improvement_23 < 0.01:
        print()
        print(
            "Three-parameter estimation provides "
            "negligible improvement over two-parameter "
            "estimation."
        )