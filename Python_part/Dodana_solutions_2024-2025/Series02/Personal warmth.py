body_temp = float(input())

e = float(100/36.8)

if (100/body_temp) < e - 0.1:
    print("you have a fever")
elif (100/body_temp) > e + 0.1:
    print("you have hypothermia")
else:
    print("you have a normal body temperature")

