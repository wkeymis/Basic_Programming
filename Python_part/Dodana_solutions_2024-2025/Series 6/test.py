from typing import List, Optional

def emergency_plan(zones, jump):
    plan = []
    visited = set()
    current = 1

    for _ in range(zones):
        plan.append(current)
        visited.add(current)
        count = 0

        while count < jump:
            current = current % zones + 1
            if current not in visited:
                count += 1

    return plan

def valid_jump(zones):
    for jump in range(1, zones):
        plan = emergency_plan(zones, jump)
        if plan[-1] == 13:
            return jump
    return None
