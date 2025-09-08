# Input DNA sequence
dna = input("Enter the DNA sequence: ").upper()

# Complement mapping
comp_base = {"A":"T", "T":"A", "G":"C", "C":"G"}

# Build a complement
comp = ""
for nuc in dna:
    comp += comp_base[nuc]

print(f"The complementary sequence of dna is: {comp}")
