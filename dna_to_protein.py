# Standard genetic code table
CODON_TABLE = {
    'AUG': 'M', 'UGG': 'W', 
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'GUU': 'V',
    'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'UCU': 'S',
    'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'CCU': 'P',
    'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'ACU': 'T',
    'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'GCU': 'A',
    'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'UAU': 'Y',
    'UAC': 'Y', 'CAU': 'H', 'CAC': 'H', 'CAA': 'Q',
    'CAG': 'Q', 'AAU': 'N', 'AAC': 'N', 'AAA': 'K',
    'AAG': 'K', 'GAU': 'D', 'GAC': 'D', 'GAA': 'E',
    'GAG': 'E', 'UGU': 'C', 'UGC': 'C', 'CGU': 'R',
    'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGU': 'S',
    'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GGU': 'G',
    'GGC': 'G', 'GGA': 'G', 'GGG': 'G', 'UAA': '*',
    'UAG': '*', 'UGA': '*'
}

def dna_to_protein(dna_sequence):
    """
    Converts a DNA sequence into its corresponding RNA and protein sequence.

    This function performs three steps:
    1. Validates the DNA sequence to ensure it contains only A, T, G, and C.
    2. Converts the DNA sequence to RNA by replacing thymine (T) with uracil (U).
    3. Translates the RNA sequence into a protein sequence using the standard codon table.
       Translation stops at the first stop codon ('UAA', 'UAG', or 'UGA').

    Parameters:
        dna_sequence (str): The input DNA sequence (can be lowercase or uppercase).

    Returns:
        tuple: A tuple containing:
            - rna_sequence (str): The RNA sequence derived from the DNA.
            - protein_sequence (str): The translated protein sequence.

    Raises:
        ValueError: If the DNA sequence contains characters other than A, T, G, or C.
    """
    
    # Convert to uppercase 
    dna_sequence = dna_sequence.upper()

    # Validate the sequence
    valid_nucleotides = ["A","T","G","C"]
    for i, char in enumerate(dna_sequence):
        if char not in valid_nucleotides:
            raise ValueError(f"Invalid nucleotide found in dna sequence at position {i+1}: {char}")
    
    # dna to rna conversion
    rna_sequence = dna_sequence.replace("T","U")

    # Translation: Read rna codons in triplets
    protein_sequence = ""
    for i in range(0,len(rna_sequence)-2,3):
        codon = rna_sequence[i:i+3]
        amino_acid = CODON_TABLE.get(codon,"X")  # X for invalid codons
        if amino_acid == "*":
            break
        protein_sequence += amino_acid
    return rna_sequence, protein_sequence

    
if __name__ == "__main__":
    dna = input("Enter the dna sequence: ")
    try:
        rna, protein = dna_to_protein(dna)
        print("Rna sequence is: ",rna)
        print("Protein sequence is: ",protein)
    except ValueError as e:
        print("Error",e)
        


