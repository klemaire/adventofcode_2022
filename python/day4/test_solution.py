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

# 'assign1, assign2, partial_overlap, full_overlap'
test_data = [['2-4', '6-8', False, False], # no overlap with place between
             ['6-8', '2-4', False, False],
             ['2-3', '4-5', False, False], # no overlap with no place between
             ['4-5', '2-3', False, False],
             ['5-7', '7-9', True, False],  # partial overlap with just 1 section
             ['7-9', '5-7', True, False],
             ['2-6', '4-8', True, False],  # partial overlap with multiple sections
             ['4-8', '2-6', True, False],
             ['2-8', '3-7', True, True],   # full overlap
             ['3-7', '2-8', True, True],
             ['6-6', '4-6', True, True],   # full overlap of section with a singleton
             ['4-4', '4-6', True, True],
             ['4-6', '6-6', True, True],
             ['4-6', '4-4', True, True],
             ['6-6', '6-6', True, True],  # Full overlap of 2 singletons 
             ['1-3', '1-3', True, True],  # Full overlap of 2 exact sections
             ]
@pytest.mark.parametrize('assign1, assign2, partial_overlap, full_overlap',
                         test_data)
def test_assignments_full_overlap(assign1, assign2, partial_overlap, full_overlap):
    assert Assignement.is_full_overlap(Assignement(assign1), Assignement(assign2)) == full_overlap

@pytest.mark.parametrize('assign1, assign2, partial_overlap, full_overlap',
                         test_data)
def test_assignments_partial_overlap(assign1, assign2, partial_overlap, full_overlap):
    assert Assignement.is_partial_overlap(Assignement(assign1), Assignement(assign2)) == partial_overlap

# Global tests
def test_test_input_file_solution1():
    assert solution1(TEST_FILE) == 2

def test_input_file_solution1():
    assert solution1(INPUT_FILE) == 498

def test_test_input_file_solution2():
    assert solution2(TEST_FILE) == 4

def test_input_file_solution2():
    assert solution2(INPUT_FILE) == 859

