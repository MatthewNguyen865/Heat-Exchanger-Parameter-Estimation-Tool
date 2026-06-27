import argparse
from src.experiment_runner import run_experiment

def main():

    parser = argparse.ArgumentParser(
        description=(
            "Heat Exchanger Parameter "
            "Estimation Framework"
        )
    )

    parser.add_argument(
        "experiment",
        type=str,
        help=(
            "Experiment to run"
        )
    )

    args = parser.parse_args()

    run_experiment(
        args.experiment
    )

if __name__ == "__main__":
    main()