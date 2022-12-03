TEST_FILE = "../../data/day2/test_input"
INPUT_FILE = "../../data/day2/input"

ROCK = 1
PAPER = 2
SCISSORS = 3

LOSE = -1
DRAW = 0
WIN = 1

MAPPING = {'A': ROCK, 'X': ROCK,
           'B': PAPER, 'Y': PAPER,
           'C': SCISSORS, 'Z': SCISSORS,
           }

OUTCOME_MAPPING = {'X': LOSE,
                   'Y': DRAW,
                   'Z': WIN}

WINS_FROM_MAPPING = {ROCK: SCISSORS,
                     PAPER: ROCK,
                     SCISSORS: PAPER}

LOOSES_FROM_MAPPING = {ROCK: PAPER,
                       PAPER: SCISSORS,
                       SCISSORS: ROCK}

def read_data(file):
    with open(file) as fp:
        return [f.strip().split() for f in fp]

def has_won(you, opponent):
    if (you == opponent):
        result = you + 3
    elif (opponent == WINS_FROM_MAPPING[you]):
        result = you + 6
    else :
        result = you + 0

    return result

def get_your_play(opponent, outcome):
    your_action = None

    if outcome == DRAW:
        your_action = opponent
    elif outcome == LOSE:  # return "(opponent=rock) wins from" -> (scissors)
        your_action = WINS_FROM_MAPPING[opponent]
    elif outcome == WIN:  # return "(opponent=rock) looses from" -> (paper)
        your_action = LOOSES_FROM_MAPPING[opponent]

    return your_action

def solution1(file):
    result = 0
    for opponent, you in read_data(file):
        result += has_won(opponent=MAPPING[opponent], you=MAPPING[you])
    return result

def solution2(file):
    result = 0
    for opponent, outcome in read_data(file):
        your_play = get_your_play(opponent=MAPPING[opponent], outcome=OUTCOME_MAPPING[outcome])
        result += has_won(opponent=MAPPING[opponent], you=your_play)
    return result

if __name__ == '__main__':
    print("test = ", solution1(TEST_FILE))
    print("test_input = ", solution1(INPUT_FILE))

    print("test = ", solution2(TEST_FILE))
    print("test_input = ", solution2(INPUT_FILE))
