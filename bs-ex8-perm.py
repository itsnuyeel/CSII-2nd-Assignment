# EX 8: PERM - 	Enumerating Gene Orders

"""""
Given: A positive integer n≤7.

Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).
"""""

# The exercise requires you to calculate all permutations of length n of a set of positive numbers from 1 to n, then print them out 
# and indicate the total number of permutations.
# - A permutation is a possible ordering of the elements of a set.
# - ex: for n=3, the set is [1,2,3]. The permutations are: [1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]
# - The total number of permutations of a set of n elements is given by n! (factorial of n) --> ex: for n=3, 3!=6.

# In Python, the itertools library has a function called permutations that generates all permutations of a given set. So:
# 1. I import permutations from itertools
# 2. I generate the set of numbers from 1 to n using range(1, n+1)
# 3. I calculate all permutations of this set with itertools.permutations
# 4. I count the total number of permutations
# 5. I print the total number of permutation and each permutation.

# I use this built-in phython library to generate permutations
from itertools import permutations  

# Function to generate and display permutations
def permutations_generation(n):
    
    # I create a list of numbers from 1 to n
    numbers = list(range(1, n + 1)) 
    
    # I generate all permutations using itertools
    perms = list(permutations(numbers))  
    
    # I print the total number of permutations
    print(len(perms))  
    
    # I loop through each permutation
    for perm in perms: 
        
        #  I print each permutation as a space-separated string
        print(" ".join(map(str, perm)))  



if __name__ == "__main__":
    
    # I read the integer 'n' from the specified file
    with open("./bs-datasets/rosalind_perm.txt", "r") as file:
        n = int(file.read().strip())
    
    # I generate all permutations of length 'n' and prints the results
    permutations_generation(n)
