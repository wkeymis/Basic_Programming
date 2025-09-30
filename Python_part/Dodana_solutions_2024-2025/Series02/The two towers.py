tower1_flip = input()
tower2_flip = input()
same_strategy_scientist = input()

if same_strategy_scientist == "first":
    prisoner1_answer = tower1_flip
    if tower2_flip == "tails":
        prisoner2_answer = "heads"
    else:
        prisoner2_answer = "tails"

else:
    prisoner1_answer = "heads" if tower1_flip == "tails" else "tails"
    prisoner2_answer = tower2_flip


print(prisoner1_answer)
print(prisoner2_answer)