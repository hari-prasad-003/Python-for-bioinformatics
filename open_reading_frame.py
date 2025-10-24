def reverse_complement(dna_sequence):
    comp = {"A":"T","T":"A","C":"G","G":"C"}
    return "".join(comp[nuc] for nuc in dna_sequence[::-1])