# EX 9: REVP - 	Locating Restriction Sites

"""""
Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12. 
You may return these pairs in any order.
"""""

# The exercise asks you to identify all the positions and lengths of reverse palindromes present in a DNA string provided in FASTA format. 
# A reverse palindrome is a DNA sequence that coincides with its reverse complement.

# 1. I read the DNA --> I extract the DNA sequence from the FASTA file
# 2. I find reverse palindromes --> I scan the string for each position; I examine substrings between 4 and 12 in length;
# For each substring, I calculate its inverse complement and check whether it coincides with the original substring.
# 3. I return the results --> For each reverse palindrome, I provide the start position (indexed by 1) and the length.


# I define a function to find the reverse complement of a DNA sequence
def ReverseComplement(sequence):
    
    # I use a dictionary to map each base (A, T, C, G) to its complement
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    
    # I calculate the reverse complement by translating and reversing the input sequence:
    # reversed(sequence): Reverses the string; complement[base]: Replaces each base with its complement; .join(..): Combines bases into a new string
    return "".join(complement[base] for base in reversed(sequence))


# I define the main function to find all reverse palindromes
def ReversePalindromes(dna):
    
    # I initialize an empty list to store the positions and lengths of palindromes
    results = []
    
    # I iterate through each possible starting position in the DNA sequence
    for i in range(len(dna)):
        
        # I check substrings with lengths between 4 and 12
        for length in range(4, 13):
            
            # I ensure the substring is within bounds
            if i + length <= len(dna):
                
                # I extract the substring
                substring = dna[i:i+length]
                
                # I check if the substring is equal to its reverse complement
                if substring == ReverseComplement(substring):
                    
                    # I store the 1-based position and length of the reverse palindrome found
                    results.append((i + 1, length))
    
    return results



if __name__ == "__main__":
    
    # I read the DNA sequence from the specified file
    with open("./bs-datasets/rosalind_revp.txt", "r") as file:
        
        # I parse the FASTA format and extract the sequence
        lines = file.readlines()
        dna_sequence = "".join(line.strip() for line in lines if not line.startswith(">"))
    
    # I find all reverse palindromes in the DNA sequence
    palindrome_results = ReversePalindromes(dna_sequence)
    
    # I print the results in the required format
    for position, length in palindrome_results:
        print(position, length)
