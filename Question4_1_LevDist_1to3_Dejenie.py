'''
Created on May 27, 2023
@author: Dejenie Shiferaw
'''

import os
import Levenshtein

def filter_species_codes(file_path):
    species_identifiers = set()

    with open(file_path, "r") as file:
        for line in file:
            if line.startswith(">"):
                species = line.split()[0][1:]
                if species.startswith("hsa") and "-let-7" in species:
                    species_identifiers.add(species)
                    
    print(f"The total number of let-7 family miRNA among human species is: {len(species_identifiers)}")
    print("The list of let-7 family of miRNA in human (Species Identifiers with 'hsa' and -let-7) are:")
    for i, species_identifier in enumerate(species_identifiers, start=1):
        print(f"{i}. {species_identifier}")    
          

def calculate_levenshtein_distance(file_path):
    if not os.path.isfile(file_path):
        print("The specified file does not exist.")
        return

    sequences = []
    total_distance = 0
    pair_count = 0
    levenshtein_pairs = []

    with open(file_path, 'r') as file:
        species_code = ""
        sequence = ""
        for line in file:
            if line.startswith('>'):
                species_code = line[1:].strip().split("-let-7")[0]
                if species_code == 'hsa':  # Consider only sequences from human species
                    sequence = ""
            else:
                sequence = line.strip()

            if species_code == 'hsa' and sequence:
                sequences.append(sequence)
    
    # Calculate the average Levenshtein distance
    for i in range(len(sequences)):
        for j in range(i + 1, len(sequences)):
            distance = Levenshtein.distance(sequences[i], sequences[j])
            total_distance += distance
            pair_count += 1
            if 1 <= distance <= 3:
                levenshtein_pairs.append((i, j, sequences[i], sequences[j], distance))

    average_distance = total_distance / pair_count
    print("Average Levenshtein distance for these let-7 family of miRNAs in Homo sapiens is:", average_distance)
    print("The following outputs are the Levenshtein distance for all pairs of 'let-7' miRNA sequences within the human species ('hsa') and print each pair in the console:")
    
    for i, (pair_index, sequence_index, seq1, seq2, distance) in enumerate(levenshtein_pairs, start=1):
        print(f"Sequence pair {pair_index + 1} - {sequence_index + 1}: {seq1} | {seq2}, Levenshtein distance: {distance}")
        print("------------------------")
    
    print(f"Total number of sequence pairs with Levenshtein distance between 1 and 3: {len(levenshtein_pairs)}")
    print(f"The total Levenshtein distance among all pairs ({pair_count} pairs) of human ('hsa') let-7 sequences is {total_distance}.")

    
# File path
file_path = r"C:\Users\THIS-PC\eclipse-workspace2023\take_home_exam\mature.fa"
calculate_levenshtein_distance(file_path)
filter_species_codes(file_path)
