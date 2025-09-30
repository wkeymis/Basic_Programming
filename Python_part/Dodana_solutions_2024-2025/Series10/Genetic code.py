class GeneticCode:
    def __init__(self, table_location):
        self.codon_to_amino_acid = {}
        with open(table_location, 'r') as file:
            for line in file:
                codon, amino_acid = line.strip().split()
                self.codon_to_amino_acid[codon.upper().replace('U', 'T')] = amino_acid.upper()

    def amino_acid(self, codon):
        codon = codon.upper().replace('U', 'T')

        if len(codon) != 3 or not all(base in 'ACGT' for base in codon):
            raise AssertionError("invalid codon")

        try:
            return self.codon_to_amino_acid[codon]
        except KeyError:
            raise AssertionError("invalid codon")

    def protein(self, sequence):
        sequence = sequence.upper().replace('U', 'T')

        if not all(base in 'ACGT' for base in sequence):
            raise AssertionError("invalid sequence")

        protein_sequence = []
        for i in range(0, len(sequence) - 2, 3):
            codon = sequence[i:i + 3]
            if codon in self.codon_to_amino_acid:
                protein_sequence.append(self.codon_to_amino_acid[codon])

        return ''.join(protein_sequence)