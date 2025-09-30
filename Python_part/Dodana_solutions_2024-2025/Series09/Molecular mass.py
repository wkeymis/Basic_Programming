import re

def atomicmass(file_path):
    elements = {}
    with open(file_path, 'r') as file:
        next(file)  # Skip the header line
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) < 5:
                continue  # Skip malformed lines
            symbol = parts[1]
            atomic_mass = float(parts[4])
            elements[symbol] = atomic_mass
    return elements

def molecularmass(formula, element_masses):
    pattern = r'([A-Z][a-z]*)(\d*)'
    components = formula.split('-')
    total_mass = 0.0

    for component in components:
        matches = re.findall(pattern, component)
        for symbol, count in matches:
            if symbol not in element_masses:
                return -1
            atomic_mass = element_masses[symbol]
            count = int(count) if count else 1
            total_mass += atomic_mass * count

    return total_mass

