import os
import csv

def save_results(
    filename,
    UA_true,
    UA_est,
    percent_error
    ):
    """
    Save parameter estimation results to CSV.
    """

    os.makedirs(
        os.path.dirname(filename),
        exist_ok=True
    )

    with open(
        filename,
        mode="w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "UA_true",
            "UA_est",
            "percent_error"
        ])

        writer.writerow([
            UA_true,
            UA_est,
            percent_error
        ])

def save_study_results(
    filename,
    results
):
    """
    Save a parameter study to CSV.
    """

    os.makedirs(
        os.path.dirname(filename),
        exist_ok=True
    )

    with open(
        filename,
        mode="w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "noise_std",
            "UA_true",
            "UA_est",
            "percent_error"
        ])

        writer.writerows(results)