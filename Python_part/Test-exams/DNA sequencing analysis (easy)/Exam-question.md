# Question

### DNA Sequence Analysis

You are given a text file containing DNA sequences for multiple biological samples.  
Each sample starts with a line `"Sample: <sample_name>"`, followed by lines of the format:


For example, the file `sequences.txt`


---

## Your Task

Design two Python classes:

### 1. `DNAManager`
This class should:
- Read the sequences from the input file.  
- Store the data in a structured format for easy access.  
- Provide the following methods:
  - `longest_sequence(sample_name)`: Returns the gene with the longest sequence and its length.  
  - `total_bases(sample_name)`: Returns the total number of bases across all genes for a given sample.  
  - `gc_content(sample_name, gene_name)`: Returns the GC content (percentage of G and C bases) for the specified gene in the specified sample.  

### 2. `ReportGenerator`
This class should:
- Be initialized with a `DNAManager` object.  
- Provide a method `generate_report()` that prints, for each sample:
  - The total number of bases.  
  - The gene with the longest sequence.  
  - The GC content of each gene.  

---

## Tasks

1. Implement the two classes described above.  
2. Demonstrate your code using the provided `sequences.txt`.  


---

