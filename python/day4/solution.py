TEST_FILE = "../../data/day4/test_input"
INPUT_FILE = "../../data/day4/input"

def read_data(file):
    with open(file) as fp:
        line = fp.read()
        return [line.split(",") for line in line.split("\n")]


class Assignement:

    def __init__(self, assigned_section):
        self.min, self.max = list(map(int, assigned_section.split('-')))

    def is_full_overlap(assignement1, assignement2):
        if ( assignement1.min <= assignement2.min and assignement1.max >= assignement2.max
                or assignement2.min <= assignement1.min and assignement2.max >= assignement1.max):
            return True
        return False

    def is_no_partial_overlap(assignement1, assignement2):
        # a1 : .234..... a1.max < a2.min
        # a2 : .....678.
        # a1 : .....678. a1.min > a2.max
        # a2 : .234.....
        if ( assignement1.max < assignement2.min or assignement1.min > assignement2.max ):
            return True
        return False

    def is_partial_overlap(assignement1, assignement2):
        return not Assignement.is_no_partial_overlap(assignement1, assignement2)


def solution1(file):
    result = 0

    for assign1, assign2 in read_data(file):
        is_full_overlap = Assignement.is_full_overlap(
            Assignement(assign1),
            Assignement(assign2)
        )
        if is_full_overlap:
            result += 1

    return result


def solution2(file):
    result = 0

    for assign1, assign2 in read_data(file):
        is_partial_overlap = Assignement.is_partial_overlap(
            Assignement(assign1),
            Assignement(assign2)
        )
        if is_partial_overlap:
            result += 1

    return result


if __name__ == '__main__':
    print("test = ", solution1(TEST_FILE))
    print("test_input = ", solution1(INPUT_FILE))

    print("test = ", solution2(TEST_FILE))
    print("test_input = ", solution2(INPUT_FILE))
