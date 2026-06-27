from examples.one_parameter_estimation import run_one_parameter_estimation
from examples.two_parameter_estimation import run_two_parameter_estimation
from examples.three_parameter_estimation import run_three_parameter_estimation
from src.utils.data_export import save_table
from src.core.config import MODEL_COMPARISON_DATA, MODEL_COMPARISON_PLOT
from src.analysis.plotting import plot_model_comparison

def run_model_comparison(save_results=True, create_plots=True, print_results=True):

    r1 = run_one_parameter_estimation(
        save_results=False,
        create_plots=False,
        print_results=False
    )
    r2 = run_two_parameter_estimation(
        save_results=False,
        create_plots=False,
        print_results=False
    )
    r3 = run_three_parameter_estimation(
        save_results=False,
        create_plots=False,
        print_results=False
    )

    sse_values = {
        "One Parameter": r1["SSE_total"],
        "Two Parameter": r2["SSE_total"],
        "Three Parameter": r3["SSE_total"]
    }
    best_model = min(
        sse_values,
        key=sse_values.get
    )

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
    headers = ["Study", "SSE_Hot", "SSE_Cold", "SSE_Total"]
    if save_results:
        save_table(
            filename=MODEL_COMPARISON_DATA,
            headers=headers,
            rows=results
        )

    # Plot Total SSE
    if create_plots:
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
    if print_results:
        print("\nModel Comparison Study")
        print("=" * 50)

        print(
            f"One-Parameter SSE: "
            f"{r1['SSE_total']:.4f}"
        )

        print(
            f"Two-Parameter SSE: "
            f"{r2['SSE_total']:.4f}"
        )

        print(
            f"Three-Parameter SSE: "
            f"{r3['SSE_total']:.4f}"
        )

        print(f"Best Model: {best_model}")

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

    if print_results:
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
        if print_results:
            print()
            print(
                "Three-parameter estimation provides "
                "negligible improvement over two-parameter "
                "estimation."
            )
    
    # Return Results
    return {
        "one_parameter_sse": r1["SSE_total"],
        "two_parameter_sse": r2["SSE_total"],
        "three_parameter_sse": r3["SSE_total"],
        "best_model": best_model,
        "improvement_12": improvement_12,
        "improvement_23": improvement_23,
        "results": results
    }