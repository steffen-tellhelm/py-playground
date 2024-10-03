#!/usr/bin/env python3

from typing import Final
from collections import Counter

ALL_NUMBERS: Final = [
    [10, 20, 30, 44, 50, 60, 70],
    [100, 200, 300, 400, 505, 600, 700],
    [0, 2, 3, 4, 5, 6, 7],
    [1, 2, 3, 4, 5, 6, 8],  # FIXME: not correct, has to be last index with none default diff
]


def find_wrong_number(numbers):
    diffs = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]
    print(diffs)
    diff_counts = Counter(diffs)
    default_diff = diff_counts.most_common(1)[0][0]

    bad_indices = [x for x, diff in enumerate(diffs) if diff != default_diff]
    print(bad_indices)

    bad_index = max(bad_indices)
    wrong_number = numbers[bad_index]

    return (default_diff, wrong_number, bad_index + 1)


if __name__ == "__main__":
    for numbers in ALL_NUMBERS:
        default_diff, wrong_number, wrong_pos = find_wrong_number(numbers)
        print(f"numbers are: {numbers}")
        print(f"default difference is: {default_diff}")
        print(f"wrong number is {wrong_number} at position {wrong_pos}\n")
