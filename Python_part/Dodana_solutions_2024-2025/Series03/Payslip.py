random_number = int(input())

salaries = []
while True:
    salary = input().strip()
    if salary == "stop":
        break
    salaries.append(int(salary))

num_workers = len(salaries)

total = random_number
for i, salary in enumerate(salaries, 1):
    total += salary
    print(f"worker #{i} whispers €{total}")

average_salary = (total - random_number) / num_workers
print(f"average salary: €{average_salary:.2f}")

