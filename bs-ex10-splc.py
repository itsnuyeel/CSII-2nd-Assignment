# EX 10: SPLC - RNA Splicing

"""""
Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s. 
(Note: Only one solution will exist for the dataset provided.)
"""""

# I extract the main sequence (DNA) and introns from the file in FASTA format.
# This function reads the file FASTA and stores each sequence in a dictionary, with the header (ID) as the key and the sequence as the value
def ReadFasta(filename):
    
    # A dictionary is initialised to store the sequences read from the file. 
    # The key will be the sequence name and the value will be the DNA or RNA sequence.
    sequences = {}
    
    # I open the file in read mode (‘r’) using a with context. This ensures that the file is automatically closed when the execution 
    # of the with block ends
    with open(filename, "r") as file:

        # "name" is used to keep track of the name of the current sequence
        name = None
        
        # Empty string containing the DNA or RNA sequence.
        sequence = ""
        
        # I scroll each line of the file
        for line in file:
            
            # I check if the line is a header
            if line.startswith(">"):
                
                # I store the previous sequence if it exists
                # (If "name" is not "None", it means that a sequence name has been read before, so the previous sequence (stored in "sequence") 
                # is added to the dictionary "sequence" with the key "name")
                if name:  
                    sequences[name] = sequence
                
                # I get the name of the sequence (after ">" symbol)
                # ("name" is set to the value of the line (removing the > symbol with line[1:] and using strip() to remove any spaces at 
                # the beginning and at the end))
                name = line[1:].strip()  
                
                # I reset the sequence for the new entry
                sequence = ""  
            
            else:
                
                # If the line is not a header (i.e. does not start with >), I add the sequence part to the sequence variable
                sequence += line.strip()  
        
        # At the end of the cycle, the last sequence read (the one associated with the last name) is stored in the dictionary.
        if name:  
            
            sequences[name] = sequence
    
    # The function returns the sequences dictionary containing all the sequences read from the file, with the keys as the names of the 
    # sequences and the values as the sequences themselves
    return sequences


# I define a function to remove introns from the DNA sequence
# This function takes two arguments: dna (the main DNA sequence), and introns (a list of introns to be removed from the DNA sequence).
# (Introns are substrings that are replaced by an empty string)
def RemoveIntrons(dna, introns):
    
    # For each intron in the "introns" list, I use the "replace" method to remove it from the main DNA sequence ("dna"), 
    # replacing it with an empty string.
    for intron in introns:
        
        # I remove each intron from the DNA
        dna = dna.replace(intron, "")  
    
    # The function returns the resulting DNA sequence, free of introns.
    return dna


# I define a function to translate DNA to RNA by replacing T with U (because uracil U replaces thymine T in the RNA)
def DNAtoRNA(dna):
    
    # I convert all T's to U's to get RNA
    return dna.replace("T", "U")  


# This function translates the RNA sequence into a protein sequence using a codon table. It takes an RNA sequence as input and returns the corresponding protein sequence.
# Each sequence of 3 nucleotides (codon) is translated into the corresponding amino acid
def RNAtoPROTEIN(rna):
    
    # Translation table that maps each codon (3 nucleotides) to an amino acid or a special symbol to stop translation (* for stop codon).
    codon_table = {
        'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
        'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
        'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
        'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
        'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
        'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*',
        'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W',
        'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }
    
    # List for storing translated amino acids.
    protein = ""
    
    # The for loop iterates over the RNA sequence in steps of 3, to extract each codon (every 3 nucleotides)
    for i in range(0, len(rna), 3):
        
        # I extract a 3-nucleotide codon from the RNA sequence.
        codon = rna[i:i+3]  
        
        # If the codon length is 3 (and therefore valid), -->
        if len(codon) == 3:
            amino_acid = codon_table[codon]
            if amino_acid == '*':  # Stop when I hit a stop codon
                break
            protein += amino_acid
            
    return protein


def FinalResult(filename):
    
    # I read the FASTA file
    sequences = ReadFasta(filename)
    

    # I access the sequences by converting the dictionary values into a list:
    # - "sequences" is the dictionary created by the ReadFasta() function
    # - .values() is a dictionary method that only returns values, ignoring keys
    sequence_list = list(sequences.values())
    
    # First sequence is the DNA string, rest are introns
    # I access the sequences by using numeric indices: sequence_list[0] for the main DNA and sequence_list[1:] for introns
    # sequence_list is a list of all sequences from the FASTA file and index [0] takes the first element of the list
    dna = sequence_list[0]
    
    # [1:] is a slice notation in Python, meaning ‘take all elements from position 1 (second element) to the end’.
    # It creates a new list containing all introns
    introns = sequence_list[1:]
    
    # Remove introns and translate to protein
    dna_without_introns = RemoveIntrons(dna, introns)
    protein = RNAtoPROTEIN(dna_without_introns)
    
    return protein


if __name__ == "__main__":
    
    # I call the process_fasta function with the file containing the sequences
    protein_sequence = FinalResult("./bs-datasets/rosalind_splc.txt")
    
    # I print the protein sequence result
    print(protein_sequence)
