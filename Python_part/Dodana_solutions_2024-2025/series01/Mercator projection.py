import math


lambda_0 = float(input())
lambda_ = float(input())
phi = float(input())


x = ((lambda_ - lambda_0 + 180) % 360) - 180


phi_radians = math.radians(phi)
y = 15 * math.log((1 + math.sin(phi_radians)) / (1 - math.sin(phi_radians)))

print(f"x: {x}")
print(f"y: {y}")
