from typing import List, Optional


def emergency_plan(zones, jump):
    plan = []
    unvisited = set(range(1, zones + 1))
    current = 1

    while unvisited:
        plan.append(current)
        unvisited.remove(current)

        if not unvisited:
            break

        remaining_jump = jump
        while remaining_jump > 0:
            current = current % zones + 1
            if current in unvisited:
                remaining_jump -= 1

    return plan


def valid_jump(zones):
    if zones < 13:
        return None

    for jump in range(1, zones):
        plan = emergency_plan(zones, jump)
        if plan[-1] == 13:
            return jump

    return None
