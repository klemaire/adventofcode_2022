import pytest
from solution import (
    read_data,
    solution1,
    solution2,
    extract_actions,
    extract_stacks,
    TEST_FILE,
    INPUT_FILE,
)


@pytest.fixture()
def expected_stacks_string():
    return "    [D]    \n" "[N] [C]    \n" "[Z] [M] [P]\n" " 1   2   3 "


@pytest.fixture()
def expected_actions_string():
    return (
        "move 1 from 2 to 1\n"
        "move 3 from 1 to 3\n"
        "move 2 from 2 to 1\n"
        "move 1 from 1 to 2\n"
    )


@pytest.fixture()
def expected_actions():
    return [
        {"cnt": 1, "from": 2, "to": 1},
        {"cnt": 3, "from": 1, "to": 3},
        {"cnt": 2, "from": 2, "to": 1},
        {"cnt": 1, "from": 1, "to": 2},
    ]


@pytest.fixture()
def expected_stacks():
    return {
        1: ["Z", "N"],
        2: ["M", "C", "D"],
        3: ["P"],
    }


def test_read_data(expected_stacks_string, expected_actions_string):
    stacks, actions = read_data(TEST_FILE)
    assert actions == expected_actions_string
    assert stacks == expected_stacks_string


def test_extract_actions(expected_actions_string, expected_actions):
    assert extract_actions(expected_actions_string) == expected_actions


def test_extract_stacks(expected_stacks_string, expected_stacks):
    assert extract_stacks(expected_stacks_string) == expected_stacks


# Global tests
def test_test_input_file_solution1():
    assert solution1(TEST_FILE) == "CMZ"


def test_input_file_solution1():
    assert solution1(INPUT_FILE) == "VQZNJMWTR"


def test_test_input_file_solution2():
    assert solution2(TEST_FILE) == "MCD"


def test_input_file_solution2():
    assert solution2(INPUT_FILE) == "NLCDCLVMQ"
