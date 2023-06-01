import os
import Levenshtein
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def extract_let7_code(header):
    if 'let-7' in header:
        code = header.split('let-7')[1].strip()[0]
        return f"let-7{code}"
    return ""

def average_levenshtein_distance(file_path):
    if not os.path.isfile(file_path):
        print("The specified file does not exist.")
        return

    let7_sequences = {}
    let7_frequency = {}

    with open(file_path, 'r') as file:
        let7_code = ""
        sequence = ""
        for line in file:
            if line.startswith('>'):
                header = line[1:].strip()
                let7_code = extract_let7_code(header)
                sequence = ""
            else:
                sequence = line.strip()

            if let7_code and sequence:
                let7_sequences.setdefault(let7_code, []).append(sequence)
                let7_frequency[let7_code] = let7_frequency.get(let7_code, 0) + 1

    total_sequences_count = 0
    avg_distances = []
    frequencies = []

    for let7_code, sequences in let7_sequences.items():
        total_distance = 0
        total_pairs = 0

        if len(sequences) < 2:
            continue

        for i in range(len(sequences) - 1):
            for j in range(i + 1, len(sequences)):
                total_distance += Levenshtein.distance(sequences[i], sequences[j])
                total_pairs += 1

        average_distance = total_distance / total_pairs
        frequency = let7_frequency.get(let7_code, 0)
        avg_distances.append(average_distance)
        frequencies.append(frequency)
        total_sequences_count += frequency

        print(f"The average Levenshtein distance among all pairs for the miRNA family {let7_code} is {average_distance:.2f} | Frequency: {frequency}")

    print(f"Total sequences count: {total_sequences_count}")
    
        # Violin Plot
    data = [avg_distances] * len(frequencies)
    plt.figure()
    sns.violinplot(data=data, inner="points")
    plt.xlabel('miRNA Family')
    plt.ylabel('Average Levenshtein Distance')
    plt.xticks(range(len(let7_sequences)), let7_sequences.keys())
    plt.title('Distribution of Average Levenshtein Distances for miRNA Families')
    plt.show()


    # Set the positions of the bars on the x-axis
    x = np.arange(len(let7_sequences))

    # Set the width of the bars
    bar_width = 0.35

    # Create the figure and axes
    fig, ax = plt.subplots()

    # Create the bars for frequencies
    bars1 = ax.bar(x, frequencies, bar_width, label='Frequency')

    # Create the bars for average Levenshtein distances
    bars2 = ax.bar(x + bar_width, avg_distances, bar_width, label='Avg. Distance')

    # Add labels and title
    ax.set_xlabel('The 14 let-7 family of miRNA')
    ax.set_ylabel('Count')
    ax.set_title('Average Levenshtein Distance and Frequency for the 14 let-7 family of miRNA')
    ax.set_xticks(x + bar_width / 2)
    ax.set_xticklabels(let7_sequences.keys(), rotation=45)

    # Add values above the bars
    for bar1, bar2 in zip(bars1, bars2):
        height1 = bar1.get_height()
        height2 = bar2.get_height()
        ax.annotate(f'{height1}', xy=(bar1.get_x() + bar1.get_width() / 2, height1),
                    xytext=(0, 3), textcoords='offset points',
                    ha='center', va='bottom')
        ax.annotate(f'{height2:.2f}', xy=(bar2.get_x() + bar2.get_width() / 2, height2),
                    xytext=(0, 3), textcoords='offset points',
                    ha='center', va='bottom')

    # Add a legend
    ax.legend()

    # Display the plot
    plt.tight_layout()
    plt.show()

# File path
file_path = r"C:\Users\THIS-PC\eclipse-workspace2023\take_home_exam\mature.fa"
average_levenshtein_distance(file_path)
