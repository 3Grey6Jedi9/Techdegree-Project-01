import random
import Score


puntuations=[]
player_score = 0

def start_game(player_score):
    print("Are you ready to play this super cool game?!...Alright let's begin!")
    correct_answer = random.randrange(1,11)
    puntuations.append(player_score)
    highest_score = max(puntuations)
    try:
        player_number = input("Please enter a number between 1 and 10: ")
        if player_number % 1 != 0:
            raise ValueError("Only integers between 1 and 10, please")
        elif player_number not in range(1,11):
            raise ValueError("Only integers between 1 and 10, please")
        else:
            attempts = 1
    except ValueError as err:
        print(err)
        start_game(player_score)
    except TypeError:
        print("Only integer numbers please, thanks")
        start_game(player_score)
    else:
        while correct_answer != player_number:
            attempts += 1
            if player_number < correct_answer:
                print("It's higher")
            else:
                print("It's lower")
            try:
                player_number = input("Please enter a number between 1 and 10: ")
                if player_number % 1 != 0:
                    raise ValueError("Only integers between 1 and 10, please")
                elif player_number not in range(1,11):
                    raise ValueError("Only integers between 1 and 10, please")
            except ValueError as err:
                print(err)
                start_game(player_score)
            except TypeError:
                print("Only integer numbers please, thanks")
                start_game(player_score)
            else:
                continue
        print("Well done!!!, You got it!!!... You just needed {} attempts!".format(attempts))
        player_score = int(Score.Score(attempts, highest_score))
        again = str(input("would you like to play again?"))
        while again != 'yes' and again != 'no':
            print("You must answer yes or not")
            again = str(input("would you like to play again?"))
        if again.lower() == 'yes':
            start_game(player_score)
        elif again.lower() == 'no':
            print("alright, as you wish the game is over")





start_game(player_score)
