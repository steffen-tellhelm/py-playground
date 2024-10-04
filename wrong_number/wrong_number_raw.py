#!/usr/bin/env python3

from collections import Counter


def find_wrong_number(numbers):
    diffs = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]
    diff_counts = Counter(diffs)
    default_diff = diff_counts.most_common(1)[0][0]

    bad_indices = [x for x, diff in enumerate(diffs) if diff != default_diff]

    bad_index = find_bad_index(bad_indices)
    wrong_number = numbers[bad_index]

    return (default_diff, wrong_number, bad_index + 1)


def find_bad_index(bad_indices):
    if len(bad_indices) > 1:
        return max(bad_indices)

    bad_index = bad_indices[0]

    if bad_index == 0:
        return bad_index
    else:
        return bad_index+1
