# EX 3: LIA - 	Independent Alleles

"""""
Given: Two positive integers k (k≤7) and N (N≤2^k). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. 
Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism always mates with an organism having 
genotype Aa Bb.

Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree 
(don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors.
"""""

# I have to calculate the probability that at least N organisms with the genotype Aa Bb are present in the k-th generation of Tom's family, 
# (given Mendel's law of factor independence)

# Family tree: Tom (generation 0) has genotype Aa Bb; Each individual in a generation has 2 offspring with genotype Aa Bb due to 
# Mendel's law (crossing between two Aa Bb);
# In each generation, the number of individuals doubles: at generation k, there are 2^k individuals.

# Probability of genotype Aa Bb: by crossing Aa Bb with Aa Bb, the probability of having a child with the same genotype is 1/4.
# I have to find the probability that there are at least N individuals with the genotype Aa Bb among these 2^k individuals.

# This function calculates the factorial of a positive integer n, which is the product of all the integers from 1 to n
def factorial(n):
    
    # By definition, the factorial of 0 and 1 is 1, so the function checks whether n is 0 or 1, in which case it returns 1
    if n == 0 or n == 1:
        return 1
    result = 1
    
    # If n is greater than 1, a cycle starts from 2 up to n (included)
    for i in range(2, n + 1):
        
        # At each iteration, the current value of result is multiplied by i, "accumulating" the product of all integers up to n.
        result *= i
    
    # In the end, the function returns the factorial of n
    return result

# This function calculates the binomial coefficient, which represents the number of ways in which k elements can be chosen from a set 
# of n elements without considering the order --> (kn)= n!/k!(n-k)!
def binomial_coefficient(n, k):
    
    # I the factorial function to calculate the factorial of n, k, and (n-k)
    # and thus divide the factorial of n by the product of the factorials of k and (n-k).
    # The result is an integer, since we are using integer division //
    return factorial(n) // (factorial(k) * factorial(n - k))

# This function calculates the probability that at least N organisms with genotype Aa Bb will be present in generation k
def AaBb_probability(k, m):
    
    # I calculate the total number of organisms in generation k
    # Each generation doubles the number of organisms of the previous generation. Thus, in generation k, the total number of organisms is 2^k
    total_organisms = 2 ** k 
    
    # This variable "accumulates" the total probability of having at least "m" organisms Aa Bb in generation k
    probability = 0

    # For loop to sum up the probabilities:
    # - This cycle considers all possible numbers of organisms Aa Bb from "m" up to "total_organisms"
    # For each value of i, I calculate the probability that exactly "i" organisms Aa Bb are present and add this probability to "probability"
    for i in range(m, total_organisms + 1):
        
        # Calculation of probability for exactly "i" organisms Aa Bb:
        # (0.25 ** i)--> each organism Aa Bb has a probability of 0.25 to appear. So if I have exactly ‘i’ organisms Aa Bb, I multiply 0.25 by itself i times
        # (0.75 ** (total_organisms - i))--> each organism that is NOT Aa Bb has a 0.75 probability of appearing. For "total_organisms - i“ 
        # (non Aa Bb organisms), I multiply 0.75 by itself ”total_organisms - i" times.
        # Finally, I multiply all these terms to obtain the probability of having exactly "i" organisms Aa Bb.
        prob_i = binomial_coefficient(total_organisms, i) * (0.25 ** i) * (0.75 ** (total_organisms - i))
        
        # The probability calculated for each value of "i" is added to ”probability", which will eventually contain the sum of 
        # the probabilities of having at least "m" organisms Aa Bb in generation k
        probability += prob_i

    # The function returns the total probability of having at least "m" organisms Aa Bb
    return probability



if __name__ == "__main__":
    
    with open("./bs-datasets/rosalind_lia.txt", "r") as file:
        
        # I read k and m values from the file
        k, m = map(int, file.readline().strip().split())
    
    # I calculate the probability of having at least "m" Aa Bb in generation k
    result = AaBb_probability(k, m)
    
    # I print the result to 3 decimal places
    print(f"{result:.3f}")