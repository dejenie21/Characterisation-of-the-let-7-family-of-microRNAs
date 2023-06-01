import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict

def count_species_frequency_from_mirna(file_path):
    species_frequency = defaultdict(int)

    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('>'):
                # Extract the species code from the header line
                species_code = line[1:4]
                species_frequency[species_code] += 1

    return species_frequency


# Provide the path to your mature.fa file
file_path = r"C:\Users\THIS-PC\eclipse-workspace2023\take_home_exam\mature.fa"

species_frequency = count_species_frequency_from_mirna(file_path)

# Filter species with frequency less than 100
filtered_species_frequency = {species: freq for species, freq in species_frequency.items() if freq >= 150}

sorted_species_frequency = sorted(filtered_species_frequency.items(), key=lambda x: x[1])

species = [species for species, _ in sorted_species_frequency]
frequency = [freq for _, freq in sorted_species_frequency]

# Set the seaborn style
sns.set(style="whitegrid")

# Create a bar plot using seaborn
plt.figure(figsize=(12, 6))
sns.barplot(x=species, y=frequency)

# Add labels and title
plt.xlabel('Species')
plt.ylabel('Frequency')
plt.title('Frequency of miRNA per Species (Ordered, Frequency >= 150)')

# Rotate x-axis labels for better visibility
plt.xticks(rotation=90)

# Show the plot
plt.tight_layout()
plt.show()
