TEST_FILE = "../../data/day6/test_input"
INPUT_FILE = "../../data/day6/input"

def read_data(file):
    return open(file).read().strip()

def solution1(input):
    for i in range(len(input) - 3):
        section = input[i:i+4]
        if len({letter:'' for letter in section}) == 4:
            return i + 4
    return -1


def solution2(input):
    None

if __name__ == '__main__':
    print("test = ", solution1(read_data(TEST_FILE)))
    print("test_input = ", solution1(read_data(INPUT_FILE)))
