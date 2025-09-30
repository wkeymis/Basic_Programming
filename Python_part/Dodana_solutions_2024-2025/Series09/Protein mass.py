def mass_table(file_location):
    mass_dict = {}
    with open(file_location, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) == 2:
                amino_acid, mass = parts[0], float(parts[1])
                mass_dict[amino_acid] = mass
    return mass_dict


def protein_mass(protein_sequence, mass_table, peptide=False):
    water_mass = 18.01056
    total_mass = sum(mass_table[aa] for aa in protein_sequence)

    if peptide:
        return total_mass
    return total_mass + water_mass
