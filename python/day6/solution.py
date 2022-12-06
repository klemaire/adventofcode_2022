TEST_FILE = "../../data/day6/test_input"
TEST_FILE2 = "../../data/day6/test_input2"
INPUT_FILE = "../../data/day6/input"


def read_data(file):
    return open(file).read().strip()


def get_location_of_unique_string(data_stream, length_marker=4):
    for i in range(len(data_stream) - (length_marker - 1)):
        section = data_stream[i : i + length_marker]
        if len({letter: "" for letter in section}) == length_marker:
            return i + length_marker
    return -1


def solution1(file):
    return get_location_of_unique_string(read_data(file))


def solution2(file):
    return get_location_of_unique_string(read_data(file), length_marker=14)


if __name__ == "__main__":
    print("test = ", solution1(TEST_FILE))
    print("test_input = ", solution1(INPUT_FILE))

    print("test = ", solution2(TEST_FILE2))
    print("test_input = ", solution2(INPUT_FILE))
