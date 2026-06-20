import os
import csv

def save_table(
    filename,
    headers,
    rows
    ):
    """
    Save tabular study results to CSV.
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

        writer.writerow(headers)

        writer.writerows(rows)