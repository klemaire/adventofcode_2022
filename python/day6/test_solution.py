import pytest
from solution import (
    TEST_FILE,
    TEST_FILE2,
    INPUT_FILE,
    get_location_of_unique_string,
    solution1,
    solution2,
)


@pytest.mark.parametrize(
    "input, expected_result",
    [
        ["bvwbjplbgvbhsrlpgdmjqwftvncz", 5],
        ["nppdvjthqldpwncqszvftbrmjlhg", 6],
        ["nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10],
        ["zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11],
    ],
)
def test_get_location_of_unique_string_solution1(input, expected_result):
    assert get_location_of_unique_string(input) == expected_result


@pytest.mark.parametrize(
    "input, expected_result",
    [
        ["mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19],
        ["bvwbjplbgvbhsrlpgdmjqwftvncz", 23],
        ["nppdvjthqldpwncqszvftbrmjlhg", 23],
        ["nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29],
        ["zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26],
    ],
)
def test_get_location_of_unique_string_solution2(input, expected_result):
    assert get_location_of_unique_string(input, length_marker=14) == expected_result


# Global tests
def test_test_input_file_solution1():
    assert solution1(TEST_FILE) == 10


def test_input_file_solution1():
    assert solution1(INPUT_FILE) == 1804


def test_test_input_file_solution2():
    assert solution2(TEST_FILE2) == 29


def test_input_file_solution2():
    assert solution2(INPUT_FILE) == 2508
