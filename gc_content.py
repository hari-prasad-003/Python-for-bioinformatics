# Input the DNA sequence
dna = input("Enter the DNA sequence: ").upper()

# Count G and C nucleotides
g_count = dna.count("G")
c_count = dna.count("C")

# Calculate GC content percentage
gc_percent = ((g_count + c_count) / len(dna)) * 100

# Round to two decimal places
gc_percent = round(gc_percent, 2)

# Print the result
print(f"The GC content of the DNA sequence is: {gc_percent}%")