import pandas as pd

df = pd.read_excel("input.xlsx")

# apply method applies a fn to each element in a series(1D)
df["length"] = df["DNA"].apply(len)

def count_bases(seq):
    return pd.Series({nuc:seq.count(nuc) for nuc in seq})

# It will create a table
nucleotide_count = df["DNA"].apply(count_bases)

# concatenate two tables vertically
df =pd.concat([df, nucleotide_count],axis =1)

df["GC%"] = ((df["G"]+df["C"]) / df["length"])*100

# boolean indexing. 1st df returns boolean and 2nd df return the row wher the boolean series is true
high_gc = df[df["GC%"]>50]

print("High gc concentration: \n",high_gc)
df.to_excel("output.xlsx",index=False)