# EX 5: LCSM - Finding a Shared Motif

"""""
Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
"""""

# I need to find the ‘longest common substring’ of a collection of DNA sequences, all in FASTA format
# - I consider the shortest string of them all, because a common substring cannot be longer than the shortest string
# - I start with the maximum substring length (the length of the shortest string) and gradually reduce the length until a common 
# substring is found.

# This function reads a file in FASTA format and returns a list of DNA sequences:
# - It reads the file line by line
# - It recognises sequence titles thanks to >
# - It combines all DNA lines belonging to the same sequence into a single string
# - It returns a list with all DNA sequences
def FastaFile(filename):
    
    # List to contain extracted sequences
    sequences = []
    
    # I open the specified file
    with open(filename, "r") as file:
        
        # Variable to build up a sequence
        current_sequence = ""
        
        # I scrolls each line of the file
        for line in file:
            
            # I remove spaces and newline characters at the end of the line
            line = line.strip()
            
            # I check whether the line is a header (starts with ‘>’)
            if line.startswith(">"):
                
                # If there is a sequence in build-up (it is not empty)
                if current_sequence:
                    
                    # I add the sequence to the list
                    sequences.append(current_sequence)
                    
                    # I reset the sequence for the next block
                    current_sequence = ""
            
            else:
                
                # I add the line (DNA sequence) to the current sequence
                current_sequence += line
        
        # After reading everything, I checks if there remains an unsaved sequence
        if current_sequence:
            
            # I add the last sequence to the list
            sequences.append(current_sequence)
    
    # Return a list of sequences
    return sequences

# This function finds the longest common substring among all the sequences
def CommonSubstring(sequences):
    
    # I select the shortest string among all the sequences in sequences
    # (because a common substring cannot be longer than this string)
    
    # I find the shortest string in the list "sequences" (minimum length)
    # - min(): is a built-in Python function that returns the smallest value from a collection
    # - key=len: specifies that the criteria for determining the ‘smallest’ is the length of the elements.
    shortest = min(sequences, key=len)
    
    # Shortest string length
    shortest_len = len(shortest)
    
    # For loop that starts with the maximum possible length and gradually reduces it.
    # (Iteration on possible lengths, from maximum to minimum)
    
    # This loop allows you to explore all possible substring lengths, starting from the maximum length (that of the shortest string) up to 1
    # - It generates the numbers from shortest_len up to 1, going backwards
    # - shortest_len is the length of "shortest"
    # - At each iteration, I decrease the length of the "common" substring
    for length in range(shortest_len, 0, -1):
        
        # For each length in "length", I generate all substrings of the shortest string
        # and I check whether each substring is present in all the other strings.
        
        # This loop runs all possible substrings of length "length" in the string "shortest"
        # - shortest_len - length + 1: is the number of possible substrings of length "length" we can extract from the string
        # - If the string is shortest_len long, a substring of length "length" may start at all positions from 0 up to "shortest_len - length"
        for start in range(shortest_len - length + 1): 
            
            # I extract the "common" substring from the shortest string.
            common = shortest[start:start + length]
            
            # The first substring found that is common to all strings is returned as the result.
            # (I check whether the "common" substring is present in all other sequences --> all() checks that the "common" result in seq
            # is true for all seq in sequences)
            if all(common in seq for seq in sequences):
                
                # As soon as I find a substring that is common to all sequences, I return it and stops the search
                return common
    
    # If the loop terminates without finding a common substring, I return an empty string
    return ""



if __name__ == "__main__":
    
    # I read the sequences from the specified file
    sequences = FastaFile("./bs-datasets/rosalind_lcsm.txt")
    
    # I use the list of sequences to find the longest common substring
    result = CommonSubstring(sequences)
    
    print(result)
