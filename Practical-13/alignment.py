# BEGIN Pseudocode
#   1. Import necessary libraries:
#      - os: For changing the working directory.
#      - pandas: For reading and handling the BLOSUM62 matrix from a text file.
#
#   2. Change the current working directory to "Practical-13".
#      - This is where the script expects to find its input files (blosum62.txt, FASTA files).
#
#   3. Load the BLOSUM62 scoring matrix:
#      - Read "blosum62.txt" into a pandas DataFrame.
#      - Specify that the delimiter is whitespace (using delim_whitespace=True).
#      - Specify that lines starting with '#' are comments and should be ignored.
#
#   4. Define a function `read_fasta` to read sequences from FASTA files:
#      - Input: filepath (string, path to the FASTA file).
#      - Output: sequence (string, the concatenated protein sequence).
#      - Steps:
#        a. Initialize an empty string `sequence`.
#        b. Open the file specified by `filepath` in read mode.
#        c. Iterate through each line in the file:
#           i. If the line starts with ">" (header line), skip it (continue to the next line).
#           ii. Else (sequence line), remove leading/trailing whitespace from the line and append it to `sequence`.
#        d. Return the `sequence` string.
#
#   5. Read protein sequences from their respective FASTA files using the `read_fasta` function:
#      - Read "P04179.fasta" into `human_seq`.
#      - Read "P09671.fasta" into `mouse_seq`.
#      - Read "random_sod2.fasta" into `random_seq`.
#
#   6. Define a function `comparetwo` to compare two protein sequences:
#      - Input: seq1 (string, first protein sequence), seq2 (string, second protein sequence).
#      - Output: None (prints the results directly).
#      - Precondition: Assumes seq1 and seq2 are of the same length for pairwise comparison.
#      - Steps:
#        a. Initialize `score` (for BLOSUM62 score) to 0.
#        b. Initialize `count` (for identical amino acids) to 0.
#        c. Iterate from `i` = 0 to length of `seq1` - 1 (assuming len(seq1) == len(seq2)):
#           i. If the amino acid at `seq1[i]` is the same as at `seq2[i]`:
#              Increment `count`.
#           ii. Get the BLOSUM62 score for the amino acid pair (`seq1[i]`, `seq2[i]`) from the `blosum62_df` DataFrame.
#               (Assumes amino acids in sequences are valid keys/indices in blosum62_df).
#           iii. Add this score to the total `score`.
#        d. Calculate `percentage_identity` = (`count` / length of `seq1`) * 100.
#        e. Print the `percentage_identity`.
#        f. Print the total `score`.
#
#   7. Perform sequence comparisons using the `comparetwo` function:
#      - Compare `human_seq` with `mouse_seq`.
#      - Compare `human_seq` with `random_seq`.
#      - Compare `mouse_seq` with `random_seq`.
# END Pseudocode

# Import necessary libraries
import os               # Used for operating system dependent functionalities like changing directory
import pandas as pd     # Used for data manipulation and analysis, particularly for reading the BLOSUM matrix

# Change the current working directory to "Practical-13"
# This helps in locating the input files if they are in this specific subdirectory
os.chdir("Practical-13") # Determine my path

# Load the BLOSUM62 scoring matrix from a text file into a pandas DataFrame
# delim_whitespace=True treats any whitespace (spaces, tabs) as a delimiter.
# comment='#' ignores lines starting with '#' (often used for comments in data files).
blosum62_df = pd.read_csv("blosum62.txt", delim_whitespace=True, comment='#')
# Your comment: Here, I thought of pandas which we learned in Practical-10.
# However, at that time, our delimiter was a comma, but here the delimiter is a space.
# So, I used `delim_whitespace=True` to define my delimiter.

# Define a function to read protein sequences from FASTA formatted files
# Your comment: Here, I need to read all the sequences. Then, I created a function like `read_fasta` to assist me in reading them.
def read_fasta(filepath):
    """
    Reads a protein sequence from a FASTA file.
    It skips header lines (starting with '>') and concatenates sequence lines.
    Args:
        filepath (str): The path to the FASTA file.
    Returns:
        str: The protein sequence as a single string.
    """
    sequence = ""  # Initialize an empty string to store the sequence
    with open(filepath, "r") as file:  # Open the file in read mode ('r')
        for line in file:  # Iterate over each line in the file
            if line.startswith(">"):  # Check if the line is a header line
                continue  # If it's a header, skip to the next line
            else:
                # If it's a sequence line, remove leading/trailing whitespace (like newlines)
                # and append it to the sequence string
                sequence += line.strip()
    return sequence  # Return the complete sequence

# Read the sequences from the FASTA files
human_seq = read_fasta("P04179.fasta")    # Read human SOD2 sequence
mouse_seq = read_fasta("P09671.fasta")    # Read mouse SOD2 sequence
random_seq = read_fasta("random_sod2.fasta") # Read a random sequence (presumably of similar length)

# Define a function to compare two sequences, calculate identity and BLOSUM score
# Your comment: Here, the task is to create a tool to compare two sequences. Once again, I'll create a function to accomplish this.
def comparetwo(seq1, seq2):
    """
    Compares two protein sequences of the same length.
    Calculates the percentage of identical amino acids and the total BLOSUM62 score.
    Prints these results.
    Args:
        seq1 (str): The first protein sequence.
        seq2 (str): The second protein sequence.
    """
    score = 0  # Initialize the total BLOSUM62 score
    count = 0  # Initialize the count of identical amino acids
    # Iterate through the sequences, comparing amino acids at each position
    # This assumes seq1 and seq2 are of the same length.
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:  # Check if amino acids at the current position are identical
            count += 1  # Increment count if they are identical
        # Retrieve the BLOSUM62 score for the pair of amino acids (seq1[i], seq2[i])
        # .loc[row_label, column_label] is used to access values in the DataFrame
        score += blosum62_df.loc[seq1[i], seq2[i]]

    # Calculate the percentage of identical amino acids
    percentage_identity = (count / len(seq1)) * 100
    # Print the results. :.2f formats the float to 2 decimal places.
    # Note: your original format string was :2f, typically it's :.2f for two decimal places.
    # If you meant 2 characters wide, that's different. I'll use :.2f for precision.
    print(f"Unchanged amino acid percentage: {percentage_identity:.2f}%")
    print(f"Total BLOSUM score: {score}")

# Perform the comparisons between the loaded sequences
comparetwo(human_seq, mouse_seq)      # Compare human sequence with mouse sequence
comparetwo(human_seq, random_seq)     # Compare human sequence with the random sequence
comparetwo(mouse_seq, random_seq)     # Compare mouse sequence with the random sequence