# Input the DNA sequence
dna = input("Enter the DNA sequence: ").upper()

# Input the window size
win_siz = int(input("Enter the window size: "))

# Sliding window calculation
for i in range(0, len(dna) - win_siz + 1):

    window = dna[i:i+win_siz]        # Extract substring (window)
    g_count = window.count("G")     
    c_count = window.count("C")     

    # Calculate GC content percentage
    gc_percent = ((g_count + c_count) / win_siz) * 100

    # Round to two decimal places
    gc_percent = round(gc_percent, 2)

    print(f"Window {i+1} ({window}): GC content = {gc_percent}%")