'''
Created on May 24, 2023
@Author Dejenie Shiferaw
Question 2: how many let-7 miRNAs are there in the current release of miRBase

The following code is used to obtain the total number of let-7 miRNAs and 
the total number of species codes with let-7 miRNAs.
'''

import os
def number_of_let7(file_path):
    if not os.path.isfile(file_path):
        print("The specified file does not exist.")
        return

    species_codes = []
    species_frequency = {}

    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('>'):
                miRNA_identifier = line[1:].strip()
                if 'let-7' in miRNA_identifier:
                    species_code = miRNA_identifier.split("-")[0]
                    species_codes.append(species_code)
                    species_frequency[species_code] = species_frequency.get(species_code, 0) + 1

    total_let7miRNA = len(species_codes)
    total_let7species = len(species_frequency)

    print("Total number of let-7 family of miRNAs in the current release of miRBase (mature.fa) is:", total_let7miRNA)
    print("Total number of species codes with let-7 family of miRNA is :", total_let7species)
    
    
# File path: The number_of_let7 function is called with the file_path as an argument to perform the miRNA analysis
file_path = r"C:\Users\THIS-PC\eclipse-workspace2023\take_home_exam\mature.fa"
number_of_let7(file_path)

'''
The above Python script calculates the number of occurrences of the let-7 family of miRNAs 
in mature.fa file. It also counts the number of species codes that have let-7 miRNAs. 
Output result:
Total number of let-7 family of miRNAs in the current release of miRBase (mature.fa) is: 740
Total number of species codes with let-7 family of miRNA is : 116
'''
