pos1 = str(input())
pos2 = str(input())

if pos1 == "balance":
    if pos2 == "left":
        counterfeit_coin = 8
    elif pos2 == "right":
        counterfeit_coin = 7
    else:
        counterfeit_coin = 9
elif pos1 == "left":
    if pos2 == "left":
        counterfeit_coin = 5
    elif pos2 == "right":
        counterfeit_coin = 4
    else:  # balance
        counterfeit_coin = 6
else:
    if pos2 == "left":
        counterfeit_coin = 2
    elif pos2 == "right":
        counterfeit_coin = 1
    else:  # balance
        counterfeit_coin = 3

print(f"coin #{counterfeit_coin} is counterfeit")

