def gc_content(dna_sequence):
    """
    Calculate the count of Guanine (G), Cytosine (C), and GC content percentage in a DNA sequence.

    Parameters:
        dna_sequence (str): The DNA sequence containing characters A, T, G, and C.

    Returns:
        tuple: A tuple containing:
            - g_count (int): Number of Guanine (G) nucleotides
            - c_count (int): Number of Cytosine (C) nucleotides
            - gc_percentage (float): GC content as a percentage of total sequence length

    Raises:
        ValueError: If any invalid character (not A, T, G, or C) is found in the sequence.
    """
        
    # Convert to upper case 
    dna_sequence = dna_sequence.upper()

    # Validate the sequence
    valid_nucleotides = {"A","T","G","C"}
    for i, char in enumerate(dna_sequence):
        if char not in valid_nucleotides:
            raise ValueError(f"Invalid nucleotides found in dna sequence at position {i+1}: {char}")
    
    # Count G and C
    g_count = dna_sequence.count("G")  
    c_count = dna_sequence.count("C")

    # Calculate GC percentage
    gc = g_count + c_count
    gc_percentage = (gc / len(dna_sequence))*100
    return g_count, c_count, gc_percentage       

if __name__ == "__main__":
    dna = input("Enter the dna sequence: ")
    try:
        g, c, gc_percent = gc_content(dna)              
        print(f"Guanine (G) count: {g}")
        print(f"Cytosine (C) count: {c}")
        print(f"GC Content: {gc_percent:.2f}%")
    except ValueError as e:
        print("Error",e)
