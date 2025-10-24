def count_nucleotides (dna_sequence):
    """
    Counts the number of each nucleotide (A, T, G, C) in a given DNA sequence.

    Parameters:
        dna_sequence (str): A string containing DNA characters.

    Returns:
        dict: A dictionary with counts of 'A', 'T', 'G', and 'C'.

    Raises:
        ValueError: If the sequence contains invalid characters.
    """

    # Convert to upper case
    dna_sequence = dna_sequence.upper()

    # Validate the sequence
    valid_nucleotides ={"A","T","G","C"}
    for i, char in enumerate(dna_sequence):
        if char not in valid_nucleotides:
            raise ValueError(f"Invalid nucleotides found in dna sequence at position {i+1}: {char}")
    
    # Count nucleotides
    count = {nuc:dna_sequence.count(nuc) for nuc in ["A","T","G","C"]}
    return count

if __name__ == "__main__" :
    dna = input("Enter the dna sequence: ")
    try:
        result = count_nucleotides(dna)
        print("Nucleotides count: ",result)
        print("Total nucleotides: ",len(dna))
    except ValueError as e:
        print("Error",e)

