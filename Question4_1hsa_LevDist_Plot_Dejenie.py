'''
Question 4_1: What is the Levenshtein distance among all pairs of human (species code:'hsa') let-7 sequences? and plot
By Dejenie
'''

import os
import Levenshtein
import matplotlib.pyplot as plt


def calculate_levenshtein_distance(file_path):
    if not os.path.isfile(file_path):
        print("The specified file does not exist.")
        return

    sequences = []
    distances = []  # New list to store the distances
    total_distance = 0
    pair_count = 0
    species_identifiers = set()

    with open(file_path, 'r') as file:
        species_code = ""
        sequence = ""
        for line in file:
            if line.startswith(">"):
                species = line.split()[0][1:]
                if species.startswith("hsa") and "-let-7" in species:
                    species_identifiers.add(species)
                species_code = species.split("-let-7")[0]
                if species_code == 'hsa':  # Consider only sequences from human species
                    sequence = ""
            else:
                sequence = line.strip()

            if species_code == 'hsa' and sequence:
                sequences.append((species, sequence))

    print("The following outputs are the Levenshtein distances for all pairs of 'let-7' miRNA sequences within the human species ('hsa').")

    # Calculate the average Levenshtein distance
    for i in range(len(sequences) - 1):
        for j in range(i + 1, len(sequences)):
            species_i, sequence_i = sequences[i]
            species_j, sequence_j = sequences[j]
            distance = Levenshtein.distance(sequence_i, sequence_j)
            distances.append(distance)

            total_distance += distance
            pair_count += 1
            print(f"Species pair {species_i} - {species_j}: {sequence_i} | {sequence_j}, Lev.dist: {distance}")

    average_distance = total_distance / pair_count
    print(f"The total Levenshtein distance among all pairs ({pair_count} pairs) of human ('hsa') let-7 sequences is {total_distance}.")
    print("Average Levenshtein distance for these let-7 family of miRNAs in Homo sapiens is:", average_distance)
    print(f"The total number of let-7 family miRNA among human species is: {len(species_identifiers)}")    
    # print("The list of let-7 family of miRNA in human (Species Identifiers with 'hsa' and -let-7) are:")
    # for i, species_identifier in enumerate(species_identifiers, start=1):
    #     print(f"{i}. {species_identifier}")

    # Plotting the histogram
    plt.hist(distances, bins=range(min(distances), max(distances)+2), edgecolor='black')
    plt.xlabel('Levenshtein Distance')
    plt.ylabel('Frequency of lev. Dist between let-7 miRNA pairs')
    plt.title('Distribution of Levenshtein Distances for human let-7 miRNA Sequences')

    # Display the plot
    plt.show()
   
    

# File path
file_path = r"C:\Users\THIS-PC\eclipse-workspace2023\take_home_exam\mature.fa"
calculate_levenshtein_distance(file_path)

'''
hsa-let-7a-5p - hsa-let-7a-3p: 14
hsa-let-7a-5p - hsa-let-7a-2-3p: 15
hsa-let-7a-5p - hsa-let-7b-5p: 2
hsa-let-7a-5p - hsa-let-7b-3p: 16
hsa-let-7a-5p - hsa-let-7c-5p: 1
hsa-let-7a-5p - hsa-let-7c-3p: 14
hsa-let-7a-5p - hsa-let-7d-5p: 2
hsa-let-7a-5p - hsa-let-7d-3p: 15
hsa-let-7a-5p - hsa-let-7e-5p: 1
hsa-let-7a-5p - hsa-let-7e-3p: 16
hsa-let-7a-5p - hsa-let-7f-5p: 1
hsa-let-7a-5p - hsa-let-7f-1-3p: 15
hsa-let-7a-5p - hsa-let-7f-2-3p: 14
hsa-let-7a-5p - hsa-let-7g-5p: 2
hsa-let-7a-5p - hsa-let-7g-3p: 15
hsa-let-7a-5p - hsa-let-7i-5p: 4
hsa-let-7a-5p - hsa-let-7i-3p: 12
hsa-let-7a-3p - hsa-let-7a-2-3p: 7
hsa-let-7a-3p - hsa-let-7b-5p: 13
hsa-let-7a-3p - hsa-let-7b-3p: 4
hsa-let-7a-3p - hsa-let-7c-5p: 14
hsa-let-7a-3p - hsa-let-7c-3p: 6
hsa-let-7a-3p - hsa-let-7d-5p: 15
hsa-let-7a-3p - hsa-let-7d-3p: 5
hsa-let-7a-3p - hsa-let-7e-5p: 14
hsa-let-7a-3p - hsa-let-7e-3p: 7
hsa-let-7a-3p - hsa-let-7f-5p: 13

'''
