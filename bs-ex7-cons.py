# EX 7: CONS - 	Consensus and Profile

"""""
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, 
then you may return any one of them.)
"""""

# - I create the profile matrix as a list of lists
# - I calculate the consensus string by scrolling through the columns and finding the most frequent character

# Function to parse FASTA file and extract sequences
def FastaFile(filename):
    
    # I open the specified file
    with open(filename, "r") as file:
        
        # I collect the sequences in the ‘sequences’ list (and eventually return this list)
        sequences = []
        
        # Variable to build up a sequence
        current_sequence = ""

        # I scroll each line of the file
        for line in file:
            
            # I remove spaces and newline characters at the end of the line
            line = line.strip()
            
            # I check whether the line is a header (starts with ‘>’)
            if line.startswith(">"):  
                
                # If there is a sequence in build-up (it is not empty).. -->
                if current_sequence:
                    
                    # I add the sequence to the list
                    sequences.append(current_sequence)
                
                # I reset the sequence for the next block
                current_sequence = ""
            else:
                
                # I add the line (DNA sequence) to the current sequence
                current_sequence += line  

        
        # After reading everything, I check if there remains an unsaved sequence
        if current_sequence:
            
            # I add the last sequence to the list
            sequences.append(current_sequence)  

    # I return a list of sequences
    return sequences

# Function to compute consensus string (CS) and profile matrix (PM)
# It's a function that accepts a list of DNA sequences and returns: the consensus string, the profile matrix as a dictionary of lists (e.g.: {‘A’: [5, 1, 0, 5, 0, 0], ...}).
def CS_PM(sequences):
    
    # I assume all sequences have the same length
    length = len(sequences[0])  
    
    # I start a profile matrix as a list of 4 lists (one for ‘A’, ‘C’, ‘G’, ‘T’), each with a number of columns equal to the length of the sequences
    PM = [[0] * length for _ in range(4)]  # Profile matrix: 4 rows (A, C, G, T), each with 'length' columns
    
    # Map nucleotides to profile rows
    nucleotide_index = {"A": 0, "C": 1, "G": 2, "T": 3}  

    # I fill the profile matrix
    for seq in sequences:
        for i, nucleotide in enumerate(seq):
            
            # For each sequence and for each base in the sequence, I update the count in the row corresponding to that base using nucleotide_index
            PM[nucleotide_index[nucleotide]][i] += 1

    # I construct the consensus string:
    # - For each column of the profile matrix, I extract the values of the 4 rows and find the maximum using "max"
    # - I determine which base corresponds to the maximum using the string ‘ACGT’ (it corresponds to the order of the standard nitrogen bases in DNA)
    # ex: Row 0: Adenine (A), Row 1: Cytosine (C), Row 2: Guanine (G), Row 3: Thymine (T)
    CS = ""
    for i in range(length):
        
        # I extract the i-th column
        column = [PM[row][i] for row in range(4)]  
        
        # I find the index of the maximum value
        max_index = column.index(max(column))  
        
        # I map the index back to the nucleotide
        CS += "ACGT"[max_index]  

    # I print: the consensus string and the rows of the profile matrix in order: ‘A’, ‘C’, ‘G’, ‘T’
    return CS, PM


if __name__ == "__main__":
    
    # I read the DNA strings from the specified file in FASTA format
    sequences = FastaFile("./bs-datasets/rosalind_cons.txt")
    
    # I calculate the consensus string and the profile matrix from the DNA strings
    CS, PM = CS_PM(sequences)
    
    # I print the consensus string
    print(CS)
    
    # `i` is the numeric index to access `PM`, and `base` is the nucleotide
    # I have to do this because a list in Python only accepts numeric indices (integers) to access its elements
    for i, base in enumerate("ACGT"): 
    
        # I print the profile matrix, where each base is followed by counts in the columns
        print(f"{base}: {' '.join(map(str, PM[i]))}")