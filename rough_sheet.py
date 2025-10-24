import Dna_to_protein as dtp

with open("sequence.fasta","r") as f:
    dna, *introns = [line.strip() for line in f]
    for intron in introns:
        dna = dna.replace(intron,"")

rna_sequence, protein_sequence = dtp.dna_to_protein(dna)
print(protein_sequence)
