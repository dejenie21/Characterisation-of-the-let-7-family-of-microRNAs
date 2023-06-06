# Characterisation-of-the-let-7-family-of-microRNAs

## Analysis Report on Characterization of the let-7 Family of microRNAs

# Introduction

The let-7 family of microRNAs (miRNAs) is a group of conserved, short non-coding RNAs found in various species, including humans. These miRNAs play critical roles in regulating gene expression and are involved in multiple cellular processes such as cell proliferation, differentiation, apoptosis, and metabolism. Dysregulation of let-7 expression has been linked to various human diseases, including cancer, metabolic disorders, and neurodegenerative diseases. Understanding the characteristics and functions of the let-7 family is crucial for elucidating their roles in health and disease.

# Characterization of miRBase

miRBase is a central repository for miRNA sequence information and serves as a comprehensive resource for researchers. It provides standardized naming conventions for miRNA genes and assigns names to newly discovered miRNAs. The miRBase database contains published miRNA sequences, along with detailed annotations, literature references, and links to secondary databases. Users can explore the data through various search options and download the data from the miRBase FTP site.

## Question 1: How many species are there in the current miRBase release? 

To answer this question, we analyzed the mature.fa file from the miRBase release 22.1. The file contains a total of 48,885 miRNA sequences, representing 271 unique species or organisms. We used a Python script (Question1_271Species_Dejenie.py) to extract species codes from the header lines of each miRNA sequence and counted the occurrences of each species. The analysis revealed the frequency of miRNA sequences per species, ranging from species codes with the lowest frequency of one to those with the highest frequency of 2656. We visualized this information in an ordered bar plot, providing a clear representation of the distribution of miRNA sequences per species.

I use the script Question1__150SpeciesPlot_Dejenie.py to generate bar plot that allow us for a better visual representation of the distribution of miRNA sequences for species frequency >=150.

![image](https://github.com/dejenie21/Take-Home-Exam/assets/87564675/ce6a3e46-5017-49a6-a54e-8761f9eaaaca)

**Figure_Qn1.1: Bar plot that shows frequency of miRNAs sequences per species (Ordered, Frequency >= 150)**

## Question 2: How many let-7 miRNAs are there in the current release of miRBase? 

We analyzed the mature.fa file to determine the number of let-7 miRNAs in the current miRBase release. The script (Question2_Dejenie.py) counted the occurrences of the let-7 family of miRNAs and identified 740 instances of let-7 miRNAs associated with 116 unique species codes. This information provides insight into the prevalence and distribution of let-7 miRNAs across different species.

## Question 3: What is the current version of miRBase? 

To determine the current version of miRBase, we accessed the README file on the miRBase website using a the following Python script. The script sent an HTTP GET request to the URL where the README file is located, retrieved the text, and searched for the version information using regular expressions. The analysis revealed that the current version of miRBase is 22.1.

 ``` 
import requests
import re
def get_mirbase_version():
    url = "https://www.mirbase.org/ftp/CURRENT/README"
    response = requests.get(url)
    readme_text = response.text
    # Search for the version information in the README file
    version_match = re.search(r"Release (\d+\.\d+)", readme_text)
    if version_match:
        miRBase_version = version_match.group(1)
        return miRBase_version
    else:
        return None
# Call the function to retrieve the miRBase version
mirbase_version = get_mirbase_version()
if mirbase_version:
    print("Current version of miRBase:", mirbase_version)
else:
    print("Unable to retrieve the current version of miRBase.")
    
 ```
 
## Question3_2: Task: generate a plot to show which let miRNAs are present in each species.

The script in Question3_2_Dejenie.py analyzes the presence of the let-7 family of miRNAs in different species based on the given file containing miRNA sequences (mature.fa).  It then generates a stacked bar plot to visualize the presence of let-7 miRNAs in each species, considering only those species with a frequency count of 10 or more. The plot visualizes the presence of the let-7 family of miRNAs in different species. Each bar represents a species, and the different colors within each bar represent the individual let-7 codes. The height of each color segment corresponds to the count of that let-7 code within the species.

![Question3_2_Plot](https://github.com/dejenie21/Take-Home-Exam/assets/87564675/290f1cf4-5d4c-4764-ab36-e39bcd24af4a)

The stacked bar plot provides a visual summary of the let-7 miRNA distribution across different species, highlighting the variations in presence and abundance of these miRNAs. From the plot, we can observe that no species has all 14 let-7 miRNAs. Each species has a unique combination of let-7 miRNAs. Some let-7 miRNAs are present only in a few species, indicating a species-specific distribution of these miRNAs. For example, let-7l miRNA is only present in the species with the code 'gga' (Gallus gallus), specifically let-7g-5p and let-7g-3p. Other let-7 miRNAs may be present in multiple species but with varying abundance.

## Question3_3: Levenshtein Distance
## What is the average levenshtein distance for the let-7 miRNAs for each species?

The code in Question3_3_Dejenie.py calculates the average Levenshtein distance for the let-7 miRNA sequences within each species. It groups the sequences by species and calculates the pairwise Levenshtein distances among all pairs of sequences within that species. The code skips species codes that have only one sequence, ensuring that each species has at least two sequences before calculating the average Levenshtein distance. The output of the code includes the average Levenshtein distance and the frequency of let-7 miRNAs within each species.

After analyzing the let-7 miRNA sequences in different species, we can observe variations in their average Levenshtein distance and frequency. Some species exhibit higher average Levenshtein distances, indicating greater genetic diversity within their let-7 miRNA sequences, while others show lower average Levenshtein distances, suggesting a higher degree of similarity. These findings provide insights into the genetic diversity and complexity of let-7 miRNA sequences across different species, highlighting potential functional roles and evolutionary significance.

## Question 4: Analysis of let-7 miRNA presence, Levenshtein distance, and plot 

## Question 4_1: What is the Levenshtein distance among all pairs of human (species code:'hsa') let-7 sequences? and plot

The script in Question4_1_Dejenie.py calculates the Levenshtein distance for each pair of "let-7" miRNA sequences within the human species. This analysis revealed the pairwise distances between each let-7 sequence and provided a comprehensive understanding of the sequence variation within the human let-7 family. The script prints the total Levenshtein distance, average distance, and the Levenshtein distance for each pair of let-7 miRNA sequences.

The script (Question4_1hsa_LevDist_Plot_Dejenie) also generates the following histogram plot showing the distribution of Levenshtein distances for the 'let-7' miRNA sequences. The plot provides a visual representation of the distribution of distances among the pairs of sequences.

![image](https://github.com/dejenie21/Take-Home-Exam/assets/87564675/00166901-9ae6-4ac5-be9a-8b939d0ed2d2)


We can see from the above plot that the let-7 miRNA sequences exhibit varying levels of similarity. The Levenshtein distance among all pairs of human let-7 miRNA sequences ranges from one to 16 (use Question4_1_LevDist_1to3_Dejenie.py file). Although there is significant number of human let-7 miRNA pairs that have levenshtien Distance (48/153) between 4 to 9 there is a high number (about 81/153) of human let-7 miRNA pairs that have levenshtien Distance between 10 to 16.

## Question 4.2 Levenshtein distance among all pairs of let-7 miRNA sequences for all species and plot

To understand the presence and genetic diversity of let-7 miRNAs in different species, we performed a comprehensive analysis (Question4_2_AvLevDst_BarPlot_80Species_Dejenie.py). The script calculate the Levenshtein distance among all pairs of let-7 miRNA sequences within each species.  We then obtained the average Levenshtein distance for the let-7 miRNAs in each species, providing insights into the sequence variation within specific species.The analysis also involved identifying the let-7 miRNA sequences for each species and generating a stacked bar plot to visualize their distribution. The plot shows the presence of let-7 miRNAs in different species, with each bar representing a species and each segment within the bar representing an individual let-7 code. The height of each bar corresponds to the average distance, and the frequency of each species is displayed above the respective bar. The plot provides a visual comparison of the average distances for the 'let-7' miRNA sequences among different species.

![image](https://github.com/dejenie21/Take-Home-Exam/assets/87564675/e52c418e-1fc9-4251-b2db-784d02f1655b)

As we can see from the plot that species that have low number of let-7 miRNA have higher average Levenshtein distance (i.e >10) for the let-7 miRNA in that specific species code.

## Question 5.1 What is the Levenshtein distance for each let-7a family miRNA sequences among all pairs across all species and plot

The script in Question5_1let_7a_LevDist_Plot_Dejenie.py calculates the Levenshtein distance between pairs of 'let-7a' miRNA sequences found in the mature.fa file. After distances calculation, the script proceeds to calculate the average distance by dividing the sum of all distances by the number of pairs total (62412, and total Pair Count is: 7260). The total Levenshtein Distance total count of 'let-7a' miRNAs and the average Levenshtein distance are printed. To visualize the distribution of Levenshtein distances, the script also generates a bar plot using the Seaborn library. The x-axis represents the distances, and the y-axis represents the frequency of occurrence. The plot provides an overview of the distribution of Levenshtein distances among the 'let-7a' miRNA pairs across all species.

![image](https://github.com/dejenie21/Take-Home-Exam/assets/87564675/a4107ce4-c8f0-46ac-a1ab-3838c020f8a5)


The script calculated the Levenshtein distance for pairs of 'let-7a' miRNA sequences. The output shows some examples of species pairs and their corresponding Levenshtein distances. For example, "ami-let-7a-3p" and "chi-let-7a-3p" have a distance of 2, "ami-let-7a-3p" and "tch-let-7a-5p" have a distance of 12, and so on. The total count of 'let-7a' miRNAs is 121, and the average Levenshtein distance among these miRNAs is 8.60. This value represents the average dissimilarity between the 'let-7a' miRNA sequences across different species.

## Question 5.2 What is the average Levenshtein distance for each let-7 miRNA among all pairs across all species and plot

From 271 species miRNA sequences in mature.fa File, there are 116 species that have let-7 miRNA family. In the 116 species, there are a total of 740 let-7 family of miRNA. There are 14 let-7 miRNA family (13 of them are from let-7a up to let-7M and one is let-7-) in the mature.fa file. To calculate the average Levenshtein distance for each let-7 family miRNA sequence among all pairs across all species in the "mature.fa" file, we can use Question5_2_AvLevDist_AllLet7_Plot_Dejenie.py file. The code print the average Levenshtein distance for each let-7 family miRNA sequence.

The script in Question5_2_AvLevDist_AllLet7_Plot_Dejenie.py file calculates the average Levenshtein distance for each miRNA family within the 'let-7' family. It reads sequences from a file and groups them based on their miRNA family code. It then calculates the average distance among all pairs of sequences within each family. The output displays the average Levenshtein distance for each miRNA family along with its corresponding frequency.

The script also generates visualizations to represent the data. It includes a violin plot showing the distribution of average Levenshtein distances for each miRNA family. Additionally, a bar plot is created to compare the frequencies and average distances of the miRNA families within the 'let-7' family.


![image](https://github.com/dejenie21/Take-Home-Exam/assets/87564675/e3dc21d1-0a6d-444f-bb85-0649418ae098)


![image](https://github.com/dejenie21/Take-Home-Exam/assets/87564675/f3c4152a-e051-4909-a647-51b992c5b3b1)


## Conclusion 

The let-7 family of microRNAs is a conserved group with diverse functional roles in cellular processes. The analysis of the let-7 family of microRNAs provided valuable insights into their characteristics and distribution across species. The miRBase database serves as a valuable resource for researchers studying miRNAs and their roles in biological processes. Analysis of the let-7 family in miRBase revealed the number of species, let-7 miRNAs, and their distribution across species. Furthermore, the Levenshtein distance analysis provided insights into the genetic diversity and sequence variations within the let-7 miRNA family. The analysis of sequence variation and genetic diversity among let-7 miRNAs contributes to our understanding of their evolutionary significance and potential functional implications. These findings have implications for further research on miRNA regulation and their roles in disease diagnosis or pathogenesis and therapeutic interventions.

## By: Dejenie Shiferaw
