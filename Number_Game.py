import random
import Score



def start_game():
    print("""    ---------------------------------------------------------------------
    Are you ready to play this super cool game?!... Alright let's begin!
    ---------------------------------------------------------------------""")
    correct_answer = random.randrange(1,11)
    player_score = 0
    puntuations =[]
    puntuations.append(player_score)
    highest_score = max(puntuations)
    again = 'yes'
    attempts = 0
    while ValueError or again == 'yes':
        player_number = input("Please enter a number between 1 and 10: ")
        try:
            player_number = float(player_number)
            if float(player_number) % 1 != 0:
                raise ValueError
            elif int(player_number) not in range(1,11):
                raise ValueError
            else:
                player_number = int(player_number)
                if player_number < correct_answer:
                    print("It's higher")
                    attempts += 1
                elif player_number > correct_answer:
                    print("It's lower")
                    attempts += 1
                else:
                    attempts += 1
                    print("Well done!!!, You got it!!!... You just needed {} attempts!".format(attempts))
                    player_score = int(Score.Score(attempts, highest_score))
                    again = input("That was fun! \nWould you like to play again?").lower()
                    puntuations.append(player_score)
                    highest_score = max(puntuations)
                    if again != 'yes' and again != 'no':
                        print("Sorry, you must answer yes or no")
                    elif again == 'no':
                        print("Ooh we were having so much fun... As you wish")
                        break
                    else:
                        attempts = 0
                        print("""Cooool!! let's play again!!...Let's see if you can beat the highest score,
                                now is {}""".format(highest_score))
        except ValueError:
            print("Only integers please and they must be inside the given range")
            attempts += 1















start_game()
