from Bio import AlignIO
import pandas as pd

# load the aligned fasta file
alignment = AlignIO.read("clustalo-I20251023-082852-0654-29093500-p1m.fa","fasta") # Now it is a MultipleSeqAlignment object means its like a 2D table where rows: sequence and columns: nucleotide position

# print the no of sequences and alignment length
print("No of sequences: ",len(alignment))
print("Alignment length: ",alignment.get_alignment_length())

# creation of mutation table
mutation =[]

for i in range(alignment.get_alignment_length()):
    column = alignment[:,i]     # get nucleotide at position i
    unique_bases = set(column)  # remove the duplicates
    unique_bases.discard("-")   # removes "-" gap from the set
    if len(unique_bases) > 1:   # mutation exists
        mutation.append({"position":i+1,
                         "Bases":column,
                         "Unique bases":"".join(sorted(unique_bases))})

# show first 10 mutations
for m in mutation[:10]:
    print(m)

# Save all mutation to csv file
df =  pd.DataFrame(mutation)
#df.to_csv("Mutation_table.csv",index=False)
print("Total number of mutations: ",len(df))


# Import -> Load biopython and pandas
# Read   -> Open aligned fasta file as MSA object
# Iterate -> loop through each alignment colum
# Extract -> Collect nucleotides at each position
# Filter -> Remove duplicates and gaps
# Detect -> Identification of mutation (if >1)
# Store -> Save mutation in list of dictionaries
# Convert -> Make pandas dataframe
# Export -> Save the file
# Review -> Open CSV to view mutation position