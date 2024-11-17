# EX 4: PRTM - Calculating Protein Mass

"""""
Given: A protein string P of length at most 1000 aa.

Return: The total weight of P. Consult the monoisotopic mass table.
"""""

# To solve this exercise, I need to calculate the total weight of a string of proteins. 
# Each amino acid in the string has a specific weight (called ‘monoisotopic mass’) that I must add together to obtain 
# the total weight of the string.

# - I create a dictionary to associate each amino acid to its monoisotopic weight
# Each amino acid is represented by a single letter (ex: A for Alanine) and has an associated weight

# - I create the string P which represents the amino acid sequence
# - (1) I must scroll through each character in the string, (2) retrieve the weight of the corresponding amino acid from the table, 
# (3) and sum these weights to obtain the total weight of the string
# - I print the final result rounded to 3 decimal places for accurate output

# Dictionary of monoisotopic masses for each amino acid
# Each amino acid has a key (ex: "A" for Alanine) and a value representing its weight
monoistopic_masses = {
    'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259,
    'F': 147.06841, 'G': 57.02146, 'H': 137.05891, 'I': 113.08406,
    'K': 128.09496, 'L': 113.08406, 'M': 131.04049, 'N': 114.04293,
    'P': 97.05276,  'Q': 128.05858, 'R': 156.10111, 'S': 87.03203,
    'T': 101.04768, 'V': 99.06841,  'W': 186.07931, 'Y': 163.06333
}

# "protein" is the function parameter, representing the amino acid sequence
# The function uses a list comprehension to sum the weights of all the amino acids in the string "protein"
def ProteinWeight(protein):
    
    # I calculate the total weight of the string by adding up the weights of each amino acid
    total_weight = sum(monoistopic_masses[aa] for aa in protein)
    
    # I round the final result to 3 decimal digits
    return round(total_weight, 3)



if __name__ == "__main__":
    
    # I read the protein string from the input file
    with open("./bs-datasets/rosalind_prtm.txt", "r") as file:
        protein = file.readline().strip()

    # I calculate the total weight of the protein string
    result = ProteinWeight(protein)
    
    # I print the result rounded to 3 decimal places
    print(result)
