TEST_FILE = "../../data/day3/test_input"
INPUT_FILE = "../../data/day3/input"

def read_data(file):
    with open(file) as fp:
        return [(l[:int(len(l)/2)], l[int(len(l)/2):]) for l in [ l.strip() for l in fp ]]

def read_data2(file):
    out = []
    with open(file) as fp:
        for line in fp:
            out.append(line.strip())
            if len(out) == 3:
                yield out
                out = []

def get_letter_from_both_compartments(part1, part2):
    return [l for l in part1 if l in part2][0]

def get_letter_from_rucksacks(rucksacks):
    sorted_rucksacks = sorted(rucksacks, key=len, reverse=True)
    return [l for l in sorted_rucksacks[0] if l in sorted_rucksacks[1] and l in sorted_rucksacks[2]][0]

def get_priority(letter):
    code_point = ord(letter)
    # a -> z : 97 -> 122 should return 1 - 26
    # A -> Z : 65 -> 90 should return 27 - 52
    if code_point >= ord('a'):
        return code_point - ord('a') + 1
    else:
        return code_point - ord('A') + 27

def solution1(file):
    result = 0
    for compartments1, compartments2 in read_data(file):
        result += get_priority(
            get_letter_from_both_compartments(compartments1, compartments2)
        )
    return result

def solution2(file):
    result = 0
    for rucksacks in read_data2(file):
        result += get_priority(
            get_letter_from_rucksacks(rucksacks)
        )
    return result

if __name__ == '__main__':
    print("test = ", solution1(TEST_FILE))
    print("test_input = ", solution1(INPUT_FILE))

    print("test = ", solution2(TEST_FILE))
    print("test_input = ", solution2(INPUT_FILE))
