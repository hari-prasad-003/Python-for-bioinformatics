def protein_mass(protein_sequence):
    monoisotopic_mass = {
        'A': 71.03711,   # Alanine
        'R': 156.10111,  # Arginine
        'N': 114.04293,  # Asparagine
        'D': 115.02694,  # Aspartic Acid
        'C': 103.00919,  # Cysteine
        'E': 129.04259,  # Glutamic Acid
        'Q': 128.05858,  # Glutamine
        'G': 57.02146,   # Glycine
        'H': 137.05891,  # Histidine
        'I': 113.08406,  # Isoleucine
        'L': 113.08406,  # Leucine
        'K': 128.09496,  # Lysine
        'M': 131.04049,  # Methionine
        'F': 147.06841,  # Phenylalanine
        'P': 97.05276,   # Proline
        'S': 87.03203,   # Serine
        'T': 101.04768,  # Threonine
        'W': 186.07931,  # Tryptophan
        'Y': 163.06333,  # Tyrosine
        'V': 99.06841    # Valine
    }

    # Convert to upper case
    protein_sequence  = protein_sequence.upper()

    # Validate the sequence
    valid_aa = {'C', 'K', 'Y', 'D', 'P', 'M', 'I', 'V', 'E', 'S', 'A', 'L', 'H', 'W', 'T', 'N', 'F', 'Q', 'G', 'R'}
    for i, aa in enumerate(protein_sequence):
        if aa not in valid_aa:
            raise ValueError(f"Invalid amino acid is found at position {i+1} : {aa}")
    
    # Calculating the protein molecular weight
    molecular_weight = 0
    for aa in protein_sequence:
        molecular_weight += monoisotopic_mass[aa]

    return molecular_weight

if __name__ == "__main__":
    dna = input("Enter the protein sequence: ")
    try:
        result = protein_mass(dna)
        print(f"MOlecular mass is :{round(result,3)}")
    except ValueError as e:
        print("Error",e)

