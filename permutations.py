import math
import itertools

# Enter the input
num = int(input("Enter the number: "))

# print factorial of the number
print(math.factorial(num))

# Getting the order in tuple format
for perm in itertools.permutations(range(1,num+1)):

# unpack the tuple and print the elements
    print(*perm)

print()
alphabets = input("Enter the alphabet: ").upper()
for perm in itertools.product(alphabets,repeat=3):
    print("".join(map(str,perm)))
   
