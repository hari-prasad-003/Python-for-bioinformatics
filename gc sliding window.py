def gc_window(dna_sequence,sliding_window):
    """
    Calculate GC content in each sliding window of a DNA sequence.

    Parameters:
        dna_sequence (str): Input DNA sequence (e.g., "ATGC").
        sliding_window (int): Length of the sliding window.

    Returns:
        list of float: GC content percentages for each window.

    Raises:
        ValueError: If the sequence contains invalid nucleotides.
    """
    
    # Convert to uppercase 
    dna_sequence = dna_sequence.upper()
    
    # Validate the sequence
    valid_nucleotides ={"A","T","G","C"}
    for i, char in enumerate(dna_sequence):
        if char not in valid_nucleotides:
            raise ValueError(f"Invalid nucleotides is found in the dna sequence at position {i+1} : {char}")
    
    # Validate the window size
    if sliding_window > len(dna_sequence):
        raise ValueError("Sliding window is larger than dna length")
    
    # gc window calculation
    gc_contents = []
    for i in range(0,len(dna_sequence)-sliding_window+1):
        window = dna_sequence[i:i+sliding_window]
        gc_content = window.count("G") + window.count("C")
        gc_percent = (gc_content/len(window))*100
        gc_contents.append(gc_percent)
    return gc_contents

if __name__ == "__main__":
    dna = input("Enter the dna sequence: ")
    sliding_window = int(input("Enter the sliding window: "))
    try:
        result = gc_window(dna,sliding_window)
        print("GC content on each windows are")
        for i,gc in enumerate(result):
            print(f"Window {i+1}-{i+sliding_window}:  {gc:.2f}% ")
    except ValueError as e:
        print("Error",e)

