# EX 6: TRAN - Transitions and Transversions

"""""
Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).

Return: The transition/transversion ratio R(s1,s2).
"""""

# The problem asks you to: 1. Read two DNA sequences of equal length; 2. Calculate the number of transitions and transversions;
# 3. Return their ratio

# Transitions are mutations between: A <--> G (purines); C <--> T (pyrimidines)
# Transversions are mutations between: A/G <--> C/T (purines <--> pyrimidines)


def read_fasta(filename):
    
    # I read the FASTA file and return a dictionary with sequences
    sequences = {}
    current_sequence = ""
    
    # I open the file in read mode (‘r’) using a with context. This ensures that the file is automatically closed when the execution 
    # of the with block ends
    with open(filename, 'r') as file:
        
        # I scroll each line of the file
        for line in file:
            line = line.strip()
            
            # I check if the line is a header
            if line.startswith('>'):
                
                # I store the sequence identifier
                current_sequence = line[1:]
                sequences[current_sequence] = ""
            else:
                # I append the sequence lines
                sequences[current_sequence] += line
                
    return sequences


# I calculate the transition/transversion ratio between two DNA sequences (s1 and s2)
def transition_transversion_ratio(s1, s2):
    
    # A dictionary of the possible transition pairs (purine-purine, pyrimidine-pyrimidine)
    transitions = {'A': 'G', 'G': 'A', 'C': 'T', 'T': 'C'}
    
    # I initialize counters for transitions and transversions
    transition_count = 0
    transversion_count = 0
    
    # I compare each position in both sequences
    for i in range(len(s1)):
        
        # If a difference (mutation) is found..
        if s1[i] != s2[i]:  
            
            # I check if it is a transition using the dictionary
            if s2[i] == transitions[s1[i]]:
                
                # I increase the appropriate counter
                
                transition_count += 1
            
            else:
                
                transversion_count += 1
    
    # I return the ratio between the counters
    return transition_count / transversion_count if transversion_count > 0 else 0



if __name__ == "__main__":
    
    # I read the sequences from the file
    sequences = read_fasta("./bs-datasets/rosalind_tran.txt")
    
    # I convert the dictionary values to a list to easily access the sequences
    seq_list = list(sequences.values())
    
    # I calculate and print the ratio
    ratio = transition_transversion_ratio(seq_list[0], seq_list[1])
    
    print(ratio)