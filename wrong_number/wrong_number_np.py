import numpy as np


def find_wrong_number(numbers):
    diffs = np.diff(numbers)

    unique_diffs, counts = np.unique(diffs, return_counts=True)

    # y = mx + n
    m = unique_diffs[counts.argmax()]
    n = numbers[0] if numbers[1] - numbers[0] == m else numbers[2] - 2*m  # you cannot use 2nd index instead, because it interfere with index 0

    bad_index = next(x for x in range(len(numbers)) if m * x + n != numbers[x])
    wrong_number = numbers[bad_index]

    return (m, wrong_number, bad_index + 1)
