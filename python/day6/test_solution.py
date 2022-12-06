import pytest
from solution import (
    solution1,
    solution2
)

@pytest.mark.parametrize('input, expected_result',
    [
        ["bvwbjplbgvbhsrlpgdmjqwftvncz", 5],
        ["nppdvjthqldpwncqszvftbrmjlhg", 6],
        ["nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10],
        ["zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11],
    ]
)
def test_solution1(input, expected_result):
    assert solution1('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10

