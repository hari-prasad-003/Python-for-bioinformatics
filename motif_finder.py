# Input sequences
dna = input("Enter DNA sequence: ").upper()
motif = input("Enter motif sequence: ").upper()

# Initialize a list to store positions
positions = []

# Search for motif positions
for i in range(len(dna) - len(motif) + 1):
    if dna[i:i + len(motif)] == motif:
        positions.append(i + 1)  # 1-based position

# Count occurrences
count = len(positions)

# Output results
if count > 0:
    print(f"Motif appears {count} times in the DNA sequence.")
    print(f"Positions : {positions}")
else:
    print("Motif is not found in the DNA sequence.")
