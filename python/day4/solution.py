TEST_FILE = "../../data/day4/test_input"
INPUT_FILE = "../../data/day4/input"

def read_data(file):
    with open(file) as fp:
        line = fp.read()
        return [line.split(",") for line in line.split("\n")]


class Assignement:

    def __init__(self, assigned_section):
        self.min, self.max = list(map(int, assigned_section.split('-')))

    def is_overlap(assignement1, assignement2):
        if ( assignement1.min <= assignement2.min and assignement1.max >= assignement2.max
         or assignement2.min <= assignement1.min and assignement2.max >= assignement1.max):
            return True
        return False


def solution1(file):
    result = 0

    for assign1, assign2 in read_data(file):
        is_overlap = Assignement.is_overlap(
            Assignement(assign1),
            Assignement(assign2)
        )
        if is_overlap:
            result += 1

    return result


def solution2(file):
    None


if __name__ == '__main__':
    print("test = ", solution1(TEST_FILE))
    print("test_input = ", solution1(INPUT_FILE))

    """ 
    print("test = ", solution2(TEST_FILE))
    print("test_input = ", solution2(INPUT_FILE))
    """