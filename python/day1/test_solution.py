from solution import read_data, solution1, solution2, \
    TEST_FILE, INPUT_FILE


def test_read_data():
    data = read_data(TEST_FILE)

    assert data == [[1000, 2000, 3000],
                    [4000],
                    [5000, 6000],
                    [7000, 8000, 9000],
                    [10000]
                    ]

# Global tests
def test_test_input_file_solution1():
    assert solution1(TEST_FILE) == 24000

def test_input_file_solution1():
    assert solution1(INPUT_FILE) == 70374

def test_test_input_file_solution2():
    assert solution2(TEST_FILE) == 45000

def test_input_file_solution2():
    assert solution2(INPUT_FILE) == 204610

