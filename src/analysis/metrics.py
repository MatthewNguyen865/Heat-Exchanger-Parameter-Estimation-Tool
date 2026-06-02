import numpy as np

def percent_error(true_value, estimated_value):
    """
    Calculate percent error between
    a true and estimated parameter.
    """

    return abs(
        (estimated_value - true_value)
        / true_value
    ) * 100

def sse(measured, predicted):
    """
    Sum of Squared Errors.
    """

    return np.sum(
        (measured - predicted) ** 2
    )

def rmse(measured, predicted):
    """
    Root Mean Squared Error.
    """

    return np.sqrt(
        np.mean(
            (measured - predicted) ** 2
        )
    )