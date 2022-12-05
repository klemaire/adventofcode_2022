import re

TEST_FILE = "../../data/day5/test_input"
INPUT_FILE = "../../data/day5/input"


def extract_actions(actions_string):
    actions = []
    for line in actions_string.split("\n"):
        result = re.search("^move (\d+) from (\d+) to (\d+)$", line)
        if result:
            actions.append(
                {
                    "cnt": int(result.group(1)),
                    "from": int(result.group(2)),
                    "to": int(result.group(3)),
                }
            )
    return actions


def extract_stacks(stacks_string):
    stack_lines = stacks_string.split("\n")
    stack_names = stack_lines.pop()  # pop the name on the last line
    stack_lines.reverse()  # we'll process the entries from bottom to top

    stacks = {int(n): [] for n in stack_names.split()}
    pattern = re.sub(" \d ", ".(.).", stack_names)
    for line in stack_lines:
        result = re.search(pattern, line)
        if result:
            for k in stacks.keys():
                if result.group(k) != " ":
                    stacks[k].append(result.group(k))

    return stacks


def read_data(file):
    with open(file) as fp:
        stacks_string, actions_string = fp.read().split("\n\n")
    return stacks_string, actions_string


def solution1(file):
    stacks_string, actions_string = read_data(file)
    stacks = extract_stacks(stacks_string)
    actions = extract_actions(actions_string)
    for action in actions:
        for i in range(action["cnt"]):
            stacks[action["to"]].append(stacks[action["from"]].pop())
    return "".join([v[-1] for k, v in stacks.items()])


def solution2(file):
    stacks_string, actions_string = read_data(file)
    stacks = extract_stacks(stacks_string)
    actions = extract_actions(actions_string)
    for action in actions:
        containers = []
        for i in range(action["cnt"]):
            containers.append(stacks[action["from"]].pop())
        containers.reverse()
        for container in containers:
            stacks[action["to"]].append(container)
    return "".join([v[-1] for k, v in stacks.items()])


if __name__ == "__main__":
    print("test = ", solution1(TEST_FILE))
    print("test_input = ", solution1(INPUT_FILE))

    print("test = ", solution2(TEST_FILE))
    print("test_input = ", solution2(INPUT_FILE))
