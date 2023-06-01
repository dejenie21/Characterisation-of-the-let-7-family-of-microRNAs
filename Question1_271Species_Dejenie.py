'''
Created on May 24, 2023
@author: Dejenie Shiferaw
# Question 1: How many species are there in the current miRBase release?
## Task: generate an ordered plot (i.e. from lowest to highest) of number of miRNAs / species

The following code extracts the species code between ">" and "-" from the header line and counts the number 
total miRNA and the total unique species in the mature.fa file:
'''
import matplotlib.pyplot as plt
import seaborn as sns

def count_species_from_mirna(file_path):
    species_dict = {}
    total_miRNA = 0

    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('>'):
                species_code = line.split('>')[1].split('-')[0]
                species_dict[species_code] = species_dict.get(species_code, 0) + 1
                total_miRNA += 1

    sorted_species = sorted(species_dict.items(), key=lambda x: x[1])
    unique_species = len(species_dict)

    return sorted_species, unique_species, total_miRNA


# Provide the path to your mature.fa file
file_path = r"C:\Users\THIS-PC\eclipse-workspace2023\take_home_exam\mature.fa"

sorted_species, unique_species, total_miRNA = count_species_from_mirna(file_path)

print("Total Number of miRNA in mature.fa file:", total_miRNA)
print("Number of unique species found in the file:", unique_species)
print("Frequency of species codes from lowest to highest:")

for species, frequency in sorted_species:
    print(species, ":", frequency)

# Extract species codes and corresponding frequencies
species_codes = [species[0] for species in sorted_species]
frequencies = [species[1] for species in sorted_species]

# Plotting with Seaborn
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))
ax = sns.barplot(x=species_codes, y=frequencies)
ax.set_xlabel('Species Code')
ax.set_ylabel('Frequency')
ax.set_xticklabels(species_codes, rotation=90)
ax.set_title('Number of miRNA Sequences per Species')
plt.tight_layout()
plt.show()


'''
The above Python script utilizes the count_species_from_mirna function to read a fasta file containing miRNA 
data (mature.fa). It counts the total number of miRNAs and determines the number of unique species codes 
found in the file. It also calculates the frequency of each species code and prints them in ascending order of
 frequency. The output shows the total number of miRNA in the file is 48,885, and the total number of unique 
 species are 271, and a list of species codes along with their respective frequencies, ranging from species 
 codes with the lowest frequency (e.g., "ghb: 1") to those with the highest frequency (e.g., "hsa: 2656").
The script then generates an ordered bar plot using the Matplotlib library to visualize the frequencies of miRNA sequences for each species code. The x-axis of the plot represents the species codes, and the y-axis represents the frequency of miRNA sequences. The plot is displayed with appropriate labels and a title. This allows for a visual representation of the distribution of miRNA sequences across different species, helping to identify the species with the highest and lowest frequencies.

'''

