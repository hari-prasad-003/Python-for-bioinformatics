def palidrome_finder(dna_sequence):
    
    #Convert the dna to uppercase
    dna_sequence = dna_sequence.upper()

    #Validate the sequence
    valid_nucleotides = {"A","T","G","C"}
    for i, char in enumerate(dna_sequence):
        if char not in valid_nucleotides:
            raise ValueError (f"Invalid nucleotides found at position {i} : {char}")
    
    