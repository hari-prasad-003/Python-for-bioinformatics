import pandas as pd

dna = "ATGATGACACAGTACAGT"
count = {nuc:dna.count(nuc) for nuc in dna}

# .items generate a dict_items which contains tuples and after using list fn it changes to list
# first element in each tuple will assigned to nucleotide and second element in each tupel assigned to count
df = pd.DataFrame((list(count.items())),columns=["Nucleotide","Count"])

# index false will give the output without indices
df.to_excel("output.xlsx", index=False)
print(df)