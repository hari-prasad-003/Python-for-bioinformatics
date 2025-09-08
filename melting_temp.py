# Input DNA sequence
dna = input("Enter DNA sequence: ").upper()

# Count nucleotides
a_count = dna.count('A')
t_count = dna.count('T')
g_count = dna.count('G')
c_count = dna.count('C')

# Calculate melting temperature (Tm) using Wallace Rule
tm = 2 * (a_count + t_count) + 4 * (g_count + c_count)

print(f"Nucleotide counts -> A: {a_count}, T: {t_count}, G: {g_count}, C: {c_count}")
print(f"Melting Temperature (Tm) of the DNA sequence: {tm} °C")
