from random import randint


# function which returns rock, paper or scissors according to the number passed
# NOTE There are better ways to do this without using functions, like using lists as we will see later
def computer_move(random_no):
    if random_no == 1:
        return "Rock"
    elif random_no == 2:
        return "Paper"
    else:
        return "Scissors"

# This indicates that player wants to play
is_playing = True

print("ROCK, PAPER OR SCISSORS GAME\nPress q to exit anytime")

while is_playing:
    # take input from the player
    player_move = input("\nRock, Paper or Scissors? ")

    # Generate a random number
    random_no = randint(1, 3)

    # get Computer move by calling computer_move function
    comp_move = computer_move(random_no)

    if player_move == comp_move:
        print("There is a Tie!!")
    elif player_move == "Rock":
        if comp_move == "Paper":
            print("You lost! Your", player_move, "got covered by", comp_move)
        else:
            print("You won! Your", player_move, "smashed that", comp_move)
    elif player_move == "Paper":
        if comp_move == "Rock":
            print("You won! Your", player_move, "covered that", comp_move)
        else:
            print("You lost! Your", player_move, "got cut by", comp_move)
    elif player_move == "Scissors":
        if comp_move == "Paper":
            print("You won! Your", player_move, "cut that", comp_move)
        else:
            print("You lost! Your", player_move, "got smashed by", comp_move)
    elif player_move.lower() == 'q':
        # if player presses 'q', then set is_playing to False, so the program breaks out of while loop and
        # game stops
        is_playing = False
    else:
        print("Please check your spellings and try again")
