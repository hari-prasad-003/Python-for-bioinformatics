def motif_finder(dna_sequence, motif):
    """
    Finds all positions of a given motif in a DNA sequence.

    Parameters:
        dna_sequence (str): Input DNA sequence containing only A, T, G, and C.
        motif (str): DNA motif to search for.

    Returns:
        list: A list of 0-based indices where the motif starts in the DNA sequence.
    Raises:
        ValueError: If the DNA sequence contains invalid characters.
    """
    # Convert to uppercase
    dna_sequence = dna_sequence.upper()
    motif = motif.upper()

    # Validate the sequence
    valid_nucleotides = {"A","T","G","C"}
    for i, char in enumerate(dna_sequence):
        if char not in valid_nucleotides:
            raise ValueError(f"Invalid nucleotide found in dna sequence at position {i+1}: {char}")
    for i, char in enumerate(motif):
        if char not in valid_nucleotides:
            raise ValueError(f"Invalid nucleotide found in motif at position {i+1}: {char}")
    
    # find and store starting positions of motif matches
    motif_position =[]
    for i in range(len(dna_sequence)-len(motif)+1):
        if dna_sequence[i:i+len(motif)] == motif:
            motif_position.append(i)
    return motif_position

if __name__ == "__main__":
    dna = input("Enter the dna sequence: ")
    motif = input("Enter the dna motif: ")
    try:
        result = motif_finder(dna,motif)
        if result:
            for i in result:
                print(f"The motif position in dna sequence is: {i+1}")
        else:
            print("Motif is not present in Dna sequence")
    except ValueError as e:
        print("Error",e)


