def reverse_complement(dna_sequence):
    """
    Generate the reverse complement of a given DNA sequence.

    This function takes a DNA sequence (string), validates that it contains only
    the nucleotides A, T, G, and C, and returns its reverse complement.

    Parameters:
    dna_sequence(str) : The DNA sequence to process. It can be in lowercase or uppercase.

    Return(str) : The reverse complement of the given DNA sequence.

    Raises:
        ValueError: If the DNA sequence contains characters other than A, T, G, or C.
    """
    # Convert to uppercase
    dna_sequence = dna_sequence.upper()

    # Validate the sequence
    valid_nucleotides = ["A","T","G","C"]
    for i, char in enumerate(dna_sequence):
        if char not in valid_nucleotides:
            raise ValueError(f"Invalid nucleotides found in dna sequence at position {i+1}: {char}")
    
    # Complement base pairs
    complement_pairs = {"A":"T","T":"A","G":"C","C":"G"}

    # Reverse complement
    reverse_complement = "".join(complement_pairs[nucleotide] for nucleotide in reversed(dna_sequence))
    return reverse_complement

if __name__ == "__main__":
    dna = input("Enter the dna sequence: ")
    try:
        result = reverse_complement(dna)
        print(f"The reverse complement of dna is : {result}")
    except ValueError as e:
        print("Error",e)


