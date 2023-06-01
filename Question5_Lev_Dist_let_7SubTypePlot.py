import matplotlib.pyplot as plt
import numpy as np
import os
import Levenshtein

def extract_let7_code(header):
    if 'let-7' in header:
        code = header.split('let-7')[1].split()[0]
        return f"let-7{code}"
    return ""

def average_levenshtein_distance(file_path):
    if not os.path.isfile(file_path):
        print("The specified file does not exist.")
        return

    let7_sequences = {}

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

    let7_codes = []
    frequencies = []
    avg_distances = []

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
        let7_codes.append(let7_code)
        frequencies.append(len(sequences))
        avg_distances.append(average_distance)

    # Set the positions of the bars on the x-axis
    x = np.arange(len(let7_codes))

    # Set the width of the bars
    bar_width = 0.35

    # Create the figure and axes
    fig, ax = plt.subplots()

    # Create the bars for frequencies
    bars1 = ax.bar(x, frequencies, bar_width, label='Frequency')

    # Create the bars for average Levenshtein distances
    bars2 = ax.bar(x + bar_width, avg_distances, bar_width, label='Avg. Distance')

    # Add labels and title
    ax.set_xlabel('let-7 sub family Codes or let-7 sub family miRNA')
    ax.set_ylabel('Count')
    ax.set_title('Comparison of Frequency and Average Levenshtein Distance for let-7 sub family miRNA')
    ax.set_xticks(x + bar_width / 2)
    ax.set_xticklabels(let7_codes, rotation=45)

    # Add a legend
    ax.legend()

    # Display the plot
    plt.tight_layout()
    plt.show()

# File path
file_path = r"C:\Users\THIS-PC\eclipse-workspace2023\take_home_exam\mature.fa"
average_levenshtein_distance(file_path)
