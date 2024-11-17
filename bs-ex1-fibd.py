# EX 1: FIBD - Mortal Fibonacci Rabbits 

"""""
Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.
"""""

# The exercise asks to calculate the number of pairs of rabbits remaining after n months, if each pair lives for m months
# It's a variation of the Fibonacci sequence, but with a lifetime limit for each pair of rabbits --> Each pair becomes fertile after 
# one month and starts to generate new pairs, but dies after m months.

# 1. Every month each fertile pair of rabbits generates a new pair, and each pair lives exactly m months
# 2. Since each pair lives only m months, old rabbits die as the months go by
# 3. After n months, the number of couples still alive has to be calculated

# To solve the problem:
# - I use an array where each element represents the number of pairs of rabbits of different ages.
# - I update the array month by month, keeping track of new births and the death of old rabbits

def mortal_fibo_rabbits(n, m):
    
    # I create an array of length m, where the first element is 1 (initial pair of young rabbits - 1 month old) 
    # and the other elements are 0 (no other pair)
    rabbits = [1] + [0] * (m - 1)

    # Iteration through months 1 to n - 1 to calculate the rabbit pairs alive
    for month in range(1, n):
        
        # I calculate the number of new born rabbits, which corresponds to the sum of all fertile couples
        # Fertile pairs are all those that are not in the first index, because newborn rabbits cannot yet reproduce
        new_born = sum(rabbits[1:])

        # The elements in the array are shifted (by 1 month) to the right to simulate the ageing of rabbits
        # The last group is eliminated (death of rabbits that have reached age m) - they will "die" as they exit the list
        # And the number of newborns is added to the first index
        rabbits = [new_born] + rabbits[:-1]

    # The sum of all elements in rabbits represents the total number of pairs still alive after n months
    return sum(rabbits)


if __name__ == "__main__":
    
    # I open the input file in read mode
    with open("./bs-datasets/rosalind_fibd.txt", "r") as file:
        
        # I read the file line, remove the spaces and separate the values, assigning the two numbers to n and m
        n, m = map(int, file.readline().strip().split())

    # I calculate the total number of pairs of rabbits after n months with a life cycle of m months
    result = mortal_fibo_rabbits(n, m)

    # I print the final result, representing the number of pairs of rabbits still alive after n months
    print(result)
