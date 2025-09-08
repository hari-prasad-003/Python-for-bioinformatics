# Input DNA sequence
dna = input("Enter the DNA sequence: ").upper()

# Complement mapping
comp = {"A":"T", "T":"A", "G":"C", "C":"G"}

# Build reverse complement
rev_comp = ""
for nuc in reversed(dna):
    rev_comp += comp[nuc]

print(f"The reverse complementary of dna is: {rev_comp}")
