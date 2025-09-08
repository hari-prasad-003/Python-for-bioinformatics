# Input the DNA sequences
dna1 = input("Enter the first DNA sequence: ").upper()
dna2 = input("Enter the second DNA sequence: ").upper()

# Initialize Hamming distance
dis = 0

# Iterate and compare bases
for i, j in zip(dna1, dna2):
    if i != j:    # Count mismatches
        dis += 1

print(f"The Hamming distance between the two DNA sequences is {dis}")
