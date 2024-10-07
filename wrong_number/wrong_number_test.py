from wrong_number import ALGORITHMS


def test_wrong_middle():
    for desc, frn in ALGORITHMS.items():
        def_diff, wrong_nr, wrong_pos, right_nr = frn([10, 20, 30, 44, 50, 60, 70])

        assert def_diff == 10, f"used alog: {desc}"
        assert wrong_nr == 44, f"used alog: {desc}"
        assert wrong_pos == 4, f"used alog: {desc}"
        assert right_nr == 40, f"used alog: {desc}"


def test_wrong_start():
    for desc, frn in ALGORITHMS.items():
        def_diff, wrong_nr, wrong_pos, right_nr = frn([0, 2, 3, 4, 5, 6, 7])

        assert def_diff == 1, f"used alog: {desc}"
        assert wrong_nr == 0, f"used alog: {desc}"
        assert wrong_pos == 1, f"used alog: {desc}"
        assert right_nr == 1, f"used alog: {desc}"


def test_wrong_second():
    for desc, frn in ALGORITHMS.items():
        def_diff, wrong_nr, wrong_pos, right_nr = frn([1, 2.5, 3, 4, 5, 6, 7])

        assert def_diff == 1, f"used alog: {desc}"
        assert wrong_nr == 2.5, f"used alog: {desc}"
        assert wrong_pos == 2, f"used alog: {desc}"
        assert right_nr == 2, f"used alog: {desc}"


def test_wrong_before_end():
    for desc, frn in ALGORITHMS.items():
        def_diff, wrong_nr, wrong_pos, right_nr = frn([1, 2, 3, 4, 5, 6.5, 7])

        assert def_diff == 1, f"used alog: {desc}"
        assert wrong_nr == 6.5, f"used alog: {desc}"
        assert wrong_pos == 6, f"used alog: {desc}"
        assert right_nr == 6, f"used alog: {desc}"


def test_wrong_end():
    for desc, frn in ALGORITHMS.items():
        def_diff, wrong_nr, wrong_pos, right_nr = frn([1, 2, 3, 4, 5, 6, 8])

        assert def_diff == 1, f"used alog: {desc}"
        assert wrong_nr == 8, f"used alog: {desc}"
        assert wrong_pos == 7, f"used alog: {desc}"
        assert right_nr == 7, f"used alog: {desc}"
