# Input the DNA sequence
dna = input("Enter the DNA sequence: ")

# Create an empty dictionary to store nucleotide counts
nuc_count = {}

# Loop through each nucleotide in the DNA string
for nuc in dna:
    nuc_count[nuc] = dna.count(nuc)

# Print the dictionary
print(nuc_count)