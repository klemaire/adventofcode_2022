from solution import has_won, \
   ROCK, PAPER, SCISSORS, \
   WIN, DRAW, LOSE, \
   solution1, solution2, get_your_play

# Tests used for solution1
def test_equal_game_with_rock():
   assert has_won(you=ROCK, opponent=ROCK) == 4

def test_equal_game_with_paper():
   assert has_won(you=PAPER, opponent=PAPER) == 5

def test_equal_game_with_scissor():
   assert has_won(you=SCISSORS, opponent=SCISSORS) == 6

def test_rock_wins_from_scissor():
   assert has_won(you=ROCK, opponent=SCISSORS) == 7

def test_paper_wins_from_rock():
   assert has_won(you=PAPER, opponent=ROCK) == 8

def test_scissors_wins_from_paper():
    assert has_won(you=SCISSORS, opponent=PAPER) == 9

def test_rock_loses_from_paper():
   assert has_won(you=ROCK, opponent=PAPER) == 1

def test_paper_loses_from_scissors():
   assert has_won(you=PAPER, opponent=SCISSORS) == 2

def test_scissors_loses_from_rock():
   assert has_won(you=SCISSORS, opponent=ROCK) == 3

# Test used for Solution2
def test_what_wins_from_rock():
   assert get_your_play(ROCK, WIN) == PAPER

def test_what_wins_from_paper():
   assert get_your_play(PAPER, WIN) == SCISSORS

def test_what_wins_from_scissors():
   assert get_your_play(SCISSORS, WIN) == ROCK

def test_what_looses_from_rock():
   assert get_your_play(ROCK, LOSE) == SCISSORS

def test_what_looses_from_paper():
   assert get_your_play(PAPER, LOSE) == ROCK

def test_what_looses_from_scissors():
   assert get_your_play(SCISSORS, LOSE) == PAPER

def test_what_draws_rock():
   assert get_your_play(ROCK, DRAW) == ROCK

def test_what_draws_paper():
   assert get_your_play(PAPER, DRAW) == PAPER

def test_what_draws_scissors():
   assert get_your_play(SCISSORS, DRAW) == SCISSORS

# Global tests
def test_test_input_file_solution1():
   assert solution1("../../data/day2/test_input") == 15

def test_input_file_solution1():
   assert solution1("../../data/day2/input") == 13446

def test_test_input_file_solution2():
   assert solution2("../../data/day2/test_input") == 12

def test_input_file_solution2():
   assert solution2("../../data/day2/input") == 13509
