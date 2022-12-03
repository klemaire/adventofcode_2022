import pytest
from solution import read_data, read_data2,\
    get_letter_from_both_compartments, get_letter_from_rucksacks, get_priority, \
    solution1, solution2, TEST_FILE, INPUT_FILE

def test_read_data():
    rucksacks = read_data(TEST_FILE)

    assert rucksacks[0] == ('vJrwpWtwJgWr', 'hcsFMMfFFhFp')
    assert rucksacks[1] == ('jqHRNqRjqzjGDLGL', 'rsFMfFZSrLrFZsSL')

def test_read_data2():
    group = (['vJrwpWtwJgWrhcsFMMfFFhFp',
             'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
             'PmmdzqPrVvPwwTWBwg'],
             ['wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
             'ttgJtRGJQctTZtZT',
             'CrZsJsPPZsGzwwsLwLmpwMDw'])

    i = 0
    for list in read_data2(TEST_FILE):
        assert list == group[i]
        i += 1

def test_should_return_dubble_letter():
    assert get_letter_from_both_compartments('vJrwpWtwJgWr', 'hcsFMMfFFhFp') == 'p'

def test_should_return_only_one_dubble_letter():
    assert get_letter_from_both_compartments('jqHRNqRjqzjGDLGL', 'rsFMfFZSrLrFZsSL') == 'L'

@pytest.mark.parametrize('letter, value',
                         [("p", 16),
                          ("L", 38),
                          ("P", 42),
                          ("v", 22),
                          ])
def test_get_priority(letter, value):
    assert get_priority(letter) == value

# Test for
def test_get_letter_from_rucksacks():
    assert get_letter_from_rucksacks(('vJrwpWtwJgWrhcsFMMfFFhFp',
                                      'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
                                      'PmmdzqPrVvPwwTWBwg')) == 'r'

# Global tests
def test_test_input_file_solution1():
    assert solution1(TEST_FILE) == 157

def test_input_file_solution1():
    assert solution1(INPUT_FILE) == 8088

def test_test_input_file_solution2():
    assert solution2(TEST_FILE) == 70

def test_input_file_solution2():
    assert solution2(INPUT_FILE) == 2522

