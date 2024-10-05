#!/usr/bin/env python3

from typing import Final
import wrong_number_raw as raw
import wrong_number_np as np

ALL_NUMBERS: Final = [
    [40610, 41721, 42832, 43943, 45054, 46156, 47276],
    [91350, 90500, 89650, 88800, 87000, 87100, 86250],
    [12345, 17350, 22355, 26360, 32365, 37370, 42375],
    [10, 20, 30, 44, 50, 60, 70],
    [100, 200, 300, 400, 505, 600, 700],
    [0, 2, 3, 4, 5, 6, 7],
    [1, 2, 3, 4, 5, 6, 8],
]

ALGORITHMS: Final = {
    "raw implementation": raw.find_wrong_number,
    "numpy implementation": np.find_wrong_number,
}


if __name__ == "__main__":
    for numbers in ALL_NUMBERS:
        print(f"numbers are: {numbers}")
        print("-" * 79)
        for desc, find_wrong_number_algo in ALGORITHMS.items():
            default_diff, wrong_number, wrong_pos, right_number = find_wrong_number_algo(numbers)
            print(f"{desc} >> default difference is: {default_diff}")
            print(f"{desc} >> wrong number is {wrong_number} at position {wrong_pos}")
            print(f"{desc} >> right number would be {right_number}\n")
