'''
Question 4.2 Levenshtein distance among all pairs of let-7 miRNA sequences for all species and plot
By Dejenie

'''

import os
import Levenshtein
import seaborn as sns
import matplotlib.pyplot as plt

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

    distances = []
    species_codes = []

    for species_code, sequences in species_sequences.items():
        total_distance = 0
        total_sequences = len(sequences)

        if total_sequences < 2:
            continue

        for i in range(total_sequences - 1):
            for j in range(i + 1, total_sequences):
                total_distance += Levenshtein.distance(sequences[i], sequences[j])

        average_distance = total_distance / (total_sequences * (total_sequences - 1) / 2)
        distances.append(average_distance)
        species_codes.append(species_code)

        print(f"The average Levenshtein distance for the let-7 miRNA in the species code: '{species_code}': {average_distance:.2f} | Frequency: {species_frequency[species_code]}")

    # Plotting bar plot using Seaborn
    plt.figure(figsize=(12, 6))
    ax = sns.barplot(x=species_codes, y=distances)
    plt.xlabel('Species Code')
    plt.ylabel('Avg. Levenshtein Distance and Top of Bar:Species Freq')
    plt.title('Average Levenshtein Distance for the let-7 miRNA in 80 Species')

    for p, freq in zip(ax.patches, species_codes):
        height = p.get_height()
        ax.text(p.get_x() + p.get_width() / 2, height + 0.02, f'{species_frequency[freq]}', ha='center')
# I use ax.text to display the frequency value above each bar in the plot. The ha='center' argument is used to center the frequency text above each bar.
    plt.xticks(rotation=90)
    plt.show()

print("Note that 36 species that have only one miRNA sequence has not used in average Levenshtein distance calculation.")
print("The following output is the average Levenshtein distance for 80 species (80/116) containing more than two let-7 miRNA sequence:")

# File path
file_path = r"C:\Users\THIS-PC\eclipse-workspace2023\take_home_exam\mature.fa"
average_levenshtein_distance(file_path)
