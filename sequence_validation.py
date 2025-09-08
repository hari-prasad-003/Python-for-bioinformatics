# Enter the DNA sequence
dna = input("Enter the DNA sequence: ").upper()

# Define valid nucleotides
valid_nucleotides = {"A", "T", "G", "C"}

for nuc in dna:
    if nuc not in valid_nucleotides:
        raise ValueError("Invalid nucleotides present in dna")
