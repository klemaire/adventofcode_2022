TEST_FILE = "../../data/day1/test_input"
INPUT_FILE = "../../data/day1/input"

def read_data(file):
    with open(file) as fp:
        line = fp.read()
        return [list(map(int, block.split())) for block in line.split("\n\n")]

def solution1(file):
    elves = read_data(file)
    max = sorted([sum(elf_data) for elf_data in elves])[-1]
    return max


def solution2(file):
    elves = read_data(file)
    max = sorted([sum(elf_data) for elf_data in elves])[-3:]
    return sum(max)

if __name__ == '__main__':
    print("test = ", solution1(TEST_FILE))
    print("test_input = ", solution1(INPUT_FILE))

    print("test = ", solution2(TEST_FILE))
    print("test_input = ", solution2(INPUT_FILE))