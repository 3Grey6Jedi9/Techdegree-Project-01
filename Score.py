def Score(attempts, highest_score):
    player_score = 100 - attempts*10
    if player_score > highest_score:
        highest_score = player_score
        print("Wow {} points!! That's a new record!! You are lucky".format(player_score))
    elif player_score > 80:
        print("Your score is {}, that's pretty good".format(player_score))
    elif player_score > 50:
        print("Not bad...{} points".format(player_score))
    else:
        print("{} points... Did you see a black cat?? hahaha".format(player_score))
    return player_score
