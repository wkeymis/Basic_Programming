class DNAManager:
    def __init__(self, filename):
        self.samples = {}
        current_sample = None

        with open(filename, "r") as file:
            for line in file:
                line = line.strip()

                if line.startswith("Sample"):
                    current_sample = line.split(":", 1)[1].strip()
                    self.samples[current_sample] = {}
                    continue

                if current_sample and ":" in line:
                    gene_name, sequence = line.split(":")
                    self.samples[current_sample][gene_name.strip()] = sequence.strip()

    def longest_sequence(self, sample_name):
        longest_gene = None
        max_length = 0

        for gene, seq in self.samples[sample_name].items():
            if len(seq) > max_length:
                max_length = len(seq)
                longest_gene = gene
        return longest_gene, max_length


    def total_bases(self, sample_name):
        total = 0
        for seq in self.samples[sample_name].values():
            total += len(seq)
        return total
    def gc_content(self, sample_name, gene_name):
        seq = self.samples[sample_name][gene_name]
        gc_count = seq.count("G") + seq.count("C")
        return (gc_count/len(seq)) * 100

class ReportGenerator:
    def __init__(self, manager):
        self.manager = manager

    def generate_report(self):
        print("===== DNA SEQUENCE REPORT =====")
        for sample_name, genes in self.manager.samples.items():
            print(f"Sample: {sample_name}")
            total = self.manager.total_bases(sample_name)
            print(f"  Total bases: {total}")

            longest_gene, length = self.manager.longest_sequence(sample_name)
            print(f"  Longest gene: {longest_gene} ({length} bases)")

            print(f"  Gene GC content:")
            for gene in genes:
                gc = self.manager.gc_content(sample_name, gene)
                print(f"    {gene}: {gc:.1f}%")
            print("")
        print("==============================")

if __name__ == "__main__":
    manager = DNAManager("sequences.txt")
    reporter = ReportGenerator(manager)
    reporter.generate_report()
