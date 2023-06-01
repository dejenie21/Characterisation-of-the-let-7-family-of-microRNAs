import os
from Levenshtein import distance
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def calculate_levenshtein_distance(file_path):
    if not os.path.isfile(file_path):
        print("The specified file does not exist.")
        return

    let7j_sequences = []
    total_let7j_miRNA = 0
    distances = []

    with open(file_path, 'r') as file:
        species = ""
        sequence = ""
        for line in file:
            if line.startswith('>'):
                header = line[1:].strip()
                species = extract_species(header)
                sequence = ""
            else:
                sequence = line.strip()

            if 'let-7a' in header and species and sequence:
                let7j_sequences.append((species, sequence))
                total_let7j_miRNA += 1

    for i in range(len(let7j_sequences) - 1):
        for j in range(i + 1, len(let7j_sequences)):
            species1, seq1 = let7j_sequences[i]
            species2, seq2 = let7j_sequences[j]
            levenshtein_distance = distance(seq1, seq2)
            distances.append(levenshtein_distance)
            print(f"Species: {species1} - {species2} | Levenshtein Distance: {levenshtein_distance}")

    if len(distances) > 0:
        average_distance = sum(distances) / len(distances)
        print(f"Total 'let-7a' miRNAs: {total_let7j_miRNA}")
        print(f"Average Levenshtein Distance of 'let-7a' miRNAs: {average_distance:.2f}")

        # Bar plot
        df = pd.DataFrame({'Distances': distances})
        sns.countplot(x='Distances', data=df)
        plt.xlabel('Levenshtein Distance between different let-7a miRNA pairs')
        plt.ylabel('Frequency of Lev.Dist let-7a miRNA pairs')
        plt.title('Distribution of Levenshtein Distances among let-7a miRNA pairs across all species')
        plt.show()

        # Calculate total Levenshtein distance and pair count
        total_distance = sum(distances)
        pair_count = len(distances)

        print(f"Total Levenshtein Distance is: {total_distance}, and total Pair Count is: {pair_count}")


def extract_species(header):
    species = header.split(' ')[0]
    return species

# File path
file_path = r"C:\Users\THIS-PC\eclipse-workspace2023\take_home_exam\mature.fa"
calculate_levenshtein_distance(file_path)
