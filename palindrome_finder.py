# Input DNA sequence
dna = input("Enter DNA sequence: ").upper()

# Length of palindromes to search
pal_len = int(input("Enter palindrome length: "))

# Complement dictionary
comp = {"A":"T","T":"A","G":"C","C":"G"}

# Function to check palindrome
def is_palindrome(seq):
    rev_comp = ''.join(comp[n] for n in reversed(seq))
    return seq == rev_comp

# Search for palindromes
palindromes = []
for i in range(len(dna) - pal_len + 1):
    fragment = dna[i:i+pal_len]
    if is_palindrome(fragment):
        palindromes.append((fragment, i+1))  # 1-based position

# Output results
if palindromes:
    print(f"Found {len(palindromes)} palindromic sequence(s):")
    for seq, pos in palindromes:
        print(f"{seq} at position {pos}")
else:
    print("No palindromic sequences found.")
