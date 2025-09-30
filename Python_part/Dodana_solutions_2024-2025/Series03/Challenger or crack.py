n = int(input())

crack_score = 0
challenger_score = 0


for _ in range(n):
    correct_answer = input().strip()
    challenger_answer = input().strip()
    crack_assessment = input().strip()

    if challenger_answer == correct_answer:
        challenger_score += 1

    if crack_assessment == "correct" and challenger_answer == correct_answer:
        crack_score += 1
    if crack_assessment == "wrong" and challenger_answer != correct_answer:
        crack_score += 1

if crack_score < n / 2:

    print(f"challenger wins {challenger_score} points against {crack_score}")
elif crack_score > challenger_score:

    print(f"crack wins {crack_score} points against {challenger_score}")
elif challenger_score > crack_score:
    print(f"challenger wins {challenger_score} points against {crack_score}")
else:
    print(f"ex aequo: both contestants score {challenger_score} points")

