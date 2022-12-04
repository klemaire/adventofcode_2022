import pytest
from solution import read_data, solution1, solution2, \
    Assignement, \
    TEST_FILE, INPUT_FILE


def test_read_data():
    data = read_data(TEST_FILE)

    assert data == [['2-4', '6-8'],
                    ['2-3', '4-5'],
                    ['5-7', '7-9'],
                    ['2-8', '3-7'],
                    ['6-6', '4-6'],
                    ['2-6', '4-8'],]

@pytest.mark.parametrize('assign1, assign2, result',
                         [['2-4', '6-8', False],
                          ['2-3', '4-5', False],
                          ['5-7', '7-9', False],
                          ['2-8', '3-7', True],
                          ['6-6', '4-6', True],
                          ['2-6', '4-8', False]])
def test_assignments_overlap(assign1, assign2, result):
    assert Assignement.is_overlap(Assignement(assign1), Assignement(assign2)) == result

# Global tests
def test_test_input_file_solution1():
    assert solution1(TEST_FILE) == 2

def test_input_file_solution1():
    assert solution1(INPUT_FILE) == 498

"""
def test_test_input_file_solution2():
    assert solution2(TEST_FILE) == 45000

def test_input_file_solution2():
    assert solution2(INPUT_FILE) == 204610
"""

