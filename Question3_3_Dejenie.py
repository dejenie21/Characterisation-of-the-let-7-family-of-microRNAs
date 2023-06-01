'''
Created on May 24, 2023
@author: Dejenie Shiferaw
### Question 3b: Levenshtein Distance
What is the average levenshtein distance for the let-7 miRNAs for each species?

Python code to calculate the average Levenshtein distance for each species or species code with 'let-7' 
in miRNA sequence identifier or the average Levenshtein distance for the let-7 family of miRNAs for each species in mature.fa fasta file:
The code calculates the average Levenshtein distance for the let-7 family of miRNAs in the mature.fa file. 
It groups the miRNA sequences by species code, calculates the average distance for each species, and outputs the results with their frequency.
'''

import os
import Levenshtein

def average_levenshtein_distance(file_path):
    if not os.path.isfile(file_path):
        print("The specified file does not exist.")
        return

    species_sequences = {}
    species_frequency = {}

    with open(file_path, 'r') as file:
        species_code = ""
        sequence = ""
        for line in file:
            if line.startswith('>'):
                species_code = line[1:].strip().split("-let-7")[0]    #To extract the species code from a line in the file. It assumes that the species code is located after the ">" character and before the "-let-7" substring
                sequence = ""
            else:
                sequence = line.strip()

            if species_code and sequence:
                species_sequences.setdefault(species_code, []).append(sequence)
                species_frequency[species_code] = species_frequency.get(species_code, 0) + 1

    for species_code, sequences in species_sequences.items():
        total_distance = 0
        total_sequences = len(sequences)

        if total_sequences < 2:  #To ensure that a species has at least 2 sequences before calculating the average Levenshtein distance. If a species has fewer than 2 sequences, the code continues to the next species without performing any calculations.
            continue

        for i in range(total_sequences - 1):
            for j in range(i + 1, total_sequences):
                total_distance += Levenshtein.distance(sequences[i], sequences[j])

        average_distance = total_distance / (total_sequences * (total_sequences - 1) / 2)
        
        print(f"The average Levenshtein distance for the let-7 miRNA in the species code:'{species_code}': {average_distance:.2f} | Frequency: {species_frequency[species_code]}")
print("Note that 36 species that have only one miRNA sequence has not used in average Levenshtein distance calculation.")
print("The following output is the average Levenshtein distance for 80 species (80/116) containing more than two let-7 miRNA sequence:")

# File path
file_path = r"C:\Users\THIS-PC\eclipse-workspace2023\take_home_exam\mature.fa"
average_levenshtein_distance(file_path)

'''

The provided Python code calculates the average Levenshtein distance for the let-7 family of miRNAs in a 
fasta file containing miRNA sequences. It processes the file, identifies the species code and sequence for 
each miRNA entry, and groups the sequences by species. The code then calculate the average Levenshtein distance
for the let-7 miRNAs within each species. The Levenshtein distance measures the difference between two miRNA sequence, 
By calculating the distance between all pairs of sequences within a species, it determines an average distance.

The code handles cases if there is one sequence within a species for comparison. It skips such cases to ensure valid calculations.
That is, the code skips species codes that have one sequence. In the code, there is a check for total_sequences < 2 to 
ensure that a species has at least 2 sequences before calculating the average Levenshtein distance. 
If a species has fewer than 2 sequences, the code continues to the next species without performing any 
calculations. Hence, we have only 80 miRNA output for which the average Levenshtein distance is calculated 
for them. The remaining 36 let-7 family of miRNA sequences are not included in the output.
Finally, the average Levenshtein distance and the frequency of let-7 miRNAs within each species are printed 
as an output in console. For example:

    The average Levenshtein distance for the let-7 miRNA in the species code: 'cel': 15.00 | Frequency: 2
    The average Levenshtein distance for the let-7 miRNA in the species code: 'hsa': 9.78 | Frequency: 18
    The average Levenshtein distance for the let-7 miRNA in the species code: 'mmu': 9.90 | Frequency: 21

'''