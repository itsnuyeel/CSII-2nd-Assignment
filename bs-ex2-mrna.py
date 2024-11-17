# EX 2: MRNA - Inferring mRNA from Protein

"""""
Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. 
(Don't neglect the importance of the stop codon in protein translation.)
"""""

# I have to determine the total number of possible RNA strings that can encode a given protein sequence, 
# (considering that each amino acid can be encoded by several RNA codons)
# And I must return the result in the form 1,000,000, as the number of combinations can become very large

# 1. I have to calculate the total number of codon combinations that can generate the given protein sequence:
# - Each amino acid is encoded by one or more codons (sequences of 3 nucleotides) - ex: "Methionine" (M) has only 1 possible codon, 
# whereas "Leucine" (L) has 6 codons

# 2. Each protein ends with a stop codon, which is not specified in the given protein sequence (so I have to add it)
# - There are 3 possible stop codons (UGA, UAA, UAG), so I have to multiply the total number of combinations by 3 to include the stop codon

# 3. I iterate on each amino acid in the protein sequence and multiply the number of codons that can encode it
# 4. At the end of the calculation, the result must be reduced to module 1,000,000

# Dictionary containing each amino acid as a key and the number of associated codons as a value
AAtoCodons = {
    'A': 4, 'C': 2, 'D': 2, 'E': 2, 'F': 2,
    'G': 4, 'H': 2, 'I': 3, 'K': 2, 'L': 6,
    'M': 1, 'N': 2, 'P': 4, 'Q': 2, 'R': 6,
    'S': 6, 'T': 4, 'V': 4, 'W': 1, 'Y': 2
}

# Function that calculates the total number of RNA strings that can code for this protein
def RNA_strings(protein):
    
    # I set "combinations" to 1 since it's a multiplier
    combinations = 1
    
    # I set "modulo" as 1,000,000 as per the problem statement
    modulo = 1000000
    
    # For each amino acid in the protein sequence:
    for aa in protein:
        
        # I multiply combinations by the number of codons encoding that amino acid
        combinations *= AAtoCodons[aa]
        
        # After each multiplication, I apply the modulo 1,000,000 to keep the numbers manageable
        combinations %= modulo
    
    
    # I multiply by 3 (for the 3 stop codons - to account for the stop codon possibilities) 
    combinations *= 3
    
    # I apply the modulo again
    combinations %= modulo
    
    return combinations


if __name__ == "__main__":
    
    # I open the input file in read mode
    with open("./bs-datasets/rosalind_mrna.txt", "r") as file:
        
        # I read the protein string from the file and I strip any extra whitespace
        protein = file.readline().strip()

    
    result = RNA_strings(protein)

    
    print(result)
