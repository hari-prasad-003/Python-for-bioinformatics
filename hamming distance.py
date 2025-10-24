def hamming_distance(sequence1, sequence2):
    """
    Calculate the Hamming distance between two DNA sequences.

    Hamming distance is the number of differing characters at the same positions in two strings of equal length.

    Parameters:
        seq1 (str): First DNA sequence.
        seq2 (str): Second DNA sequence.

    Returns:
        int: The Hamming distance between the two sequences.
    """
    # convert to upper case
    sequence1 = sequence1.upper()
    sequence2 = sequence2.upper()

    # validate the sequence
    valid_nucleotides = {"A","T","G","C"}
    for i, char in enumerate(sequence1):
        if char not in valid_nucleotides:
            raise ValueError(f"Invalid nucleotide found in dna1 at position {i+1}: {char}")
    for i, char in enumerate(sequence2):
        if char not in valid_nucleotides:
            raise ValueError(f"Invalid nucleotide found in dna2 at position {i+1}: {char}")

    # hamming distance calculation
    hamming_distance = 0
    for i,j in zip(sequence1, sequence2):
        if i != j:
            hamming_distance += 1
    return hamming_distance

if __name__ == "__main__":
    dna1 = input("Enter the dna sequence1: ")
    dna2 = input("Enter the dna sequence2: ")
    try:
        result = hamming_distance(dna1,dna2)
        print(f"The hamming distance is: {result}")
    except ValueError as e:
        print("Error",e)























            



    
    

