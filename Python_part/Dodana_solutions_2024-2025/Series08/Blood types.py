from itertools import product

def bloodgroup_child(parent1, parent2):
    def get_abo_combinations(abo1, abo2):
        abo_genes = {
            'A': ['A', 'O'],
            'B': ['B', 'O'],
            'AB': ['A', 'B'],
            'O': ['O']
        }
        return {abo_to_group.get(a1 + a2, a1 + a2) for a1, a2 in product(abo_genes[abo1], abo_genes[abo2])}

    def get_rhesus_combinations(rhesus1, rhesus2):
        rhesus_genes = {
            '+': ['+', '-'],
            '-': ['-']
        }
        return {'+' if '+' in combo else '-' for combo in product(rhesus_genes[rhesus1], rhesus_genes[rhesus2])}

    abo_to_group = {
        'AA': 'A', 'AO': 'A', 'OA': 'A',
        'BB': 'B', 'BO': 'B', 'OB': 'B',
        'AB': 'AB', 'BA': 'AB',
        'OO': 'O'
    }

    abo1, rhesus1 = parent1[:-1], parent1[-1]
    abo2, rhesus2 = parent2[:-1], parent2[-1]

    possible_abo = get_abo_combinations(abo1, abo2)
    possible_rhesus = get_rhesus_combinations(rhesus1, rhesus2)

    return {abo + rhesus for abo, rhesus in product(possible_abo, possible_rhesus)}

def bloodgroup_parent(known_parent, child):
    all_groups = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    possible_parents = set()

    for group in all_groups:
        possible_children = bloodgroup_child(known_parent, group)
        if child in possible_children:
            possible_parents.add(group)

    return possible_parents
