import math
import pandas as pd

def validate_sequence(dna_sequence):
    valid_nucleotides ={"A","T","G","C"}
    for i, char in enumerate(dna_sequence):
        if char not in valid_nucleotides:
            raise ValueError(f"Invalid nucleotides found in dna sequence at position {i+1}: {char}")
        
def count_nucleotides(dna_sequence):
    count = {nuc:dna_sequence.count(nuc) for nuc in "ATGC"}
    return (count)
    
def gc_content(dna_sequence):
    counts = count_nucleotides(dna_sequence)
    gc_percent = (( counts["G"] + counts["C"]) / len(dna_sequence))*100
    return (round(gc_percent,2))

def at_content(dna_sequence):
    return 100-gc_content(dna_sequence)

def gc_skew(dna_sequence):
    counts = count_nucleotides(dna_sequence)
    g = counts["G"]
    c = counts["C"]
    return round((g-c)/ (g+c),2)

def at_skew(dna_sequence):
    counts = count_nucleotides(dna_sequence)
    a = counts["A"]
    t = counts["T"]
    return round((a-t)/(a+t),2)

def shannon_entropy(dna_sequence):
    entropy = 0.0
    for base in "ATGC":
        count = dna_sequence.count(base)
        if count > 0:
            p = count / len(dna_sequence)
            entropy += -p*math.log2(p)
    return round(entropy,4)

def parse_fasta(file_name):
    with open(file_name,"r") as file:
        accession = None
        seq_parts = []
        sequences = {}
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if accession:
                    sequences[accession] = "".join(seq_parts)
                accession = line.split()[0][1:] 
                seq_parts = []
            else:
                seq_parts.append(line.upper())           # .append() modifies the list in place and returns None.So by doing sequence_lines = sequence_lines.append(...), you overwrite sequence_lines with None.
        
        if accession:
            sequences[accession] = "".join(seq_parts)
        
    return sequences

if __name__ == "__main__":
    file_name = "sequence.fasta"
    try:
        seq_dict = parse_fasta("sequence.fasta")
        with open("output.txt","w") as out_file:
            result = []
            for acc, seq in seq_dict.items():
                validate_sequence(seq)
                counts = count_nucleotides(seq)
                result.append({
                    "Accession no": acc,
                    "Total nucleotides" : len(seq),
                    "A" : counts["A"],
                    "G" : counts["G"],
                    "C" : counts["C"],
                    "T" : counts["T"],
                    "GC%" : gc_content(seq),
                    "AT%" : at_content(seq),
                    "GC skew": gc_skew(seq),
                    "AT skew" : at_skew(seq),
                    "Shannon entropy" : shannon_entropy(seq)     
                })
            df = pd.DataFrame(result)
            df.to_csv("output.csv", index=False)

            """out_file.write(f"\tAccession No: {acc}\n")
            out_file.write(f"nucleotides: {len(seq)}\n")
            out_file.write(f"Nucleotide count: {count_nucleotides(seq)}\n")
            out_file.write(f"GC% : {gc_content(seq)}\n")
            out_file.write(f"AT% : {at_content(seq)}\n")
            out_file.write(f"GC skew: {gc_skew(seq)}\n")
            out_file.write(f"AT skew: {at_skew(seq)}\n")
            out_file.write(f"Shannon entropy: {shannon_entropy(seq)}\n")
            out_file.write("\n")"""
    except ValueError as e:
        print("Error", e)
    


    

    


