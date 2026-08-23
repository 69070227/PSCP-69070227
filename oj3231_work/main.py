"""เกมทายลูกเต๋า"""

og_dice = int(input())
player_dice = int(input())

if 6 < og_dice or 6 < player_dice:
    print("Invalid")
elif 1 > og_dice or 1 >  player_dice:
    print("Invalid")

elif player_dice == og_dice:
    print("Correct!")
elif player_dice != og_dice:
    print("Wrong!")
