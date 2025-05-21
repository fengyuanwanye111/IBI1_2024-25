import os
import pandas as pd

os.chdir("Practical-13") # Determine my path

blosum62_df = pd.read_csv("blosum62.txt", delim_whitespace=True, comment='#') # Here, I thought of pandas which we learned in Practical-10. However, at that time, our delimiter was a comma, but here the delimiter is a space. So, I used `delim_whitespace=True` to define my delimiter.  

# Here, I need to read all the sequences. Then, I created a function like `read_fasta` to assist me in reading them.
def read_fasta(filepath):
    sequence = ""
    with open(filepath, "r")as file:
        for line in file:
            if line.startswith(">"):
                continue
            else:
                sequence += line.strip()
    return sequence

human_seq = read_fasta("P04179.fasta")
mouse_seq = read_fasta("P09671.fasta")
random_seq = read_fasta("random_sod2.fasta")

# Here, the task is to create a tool to compare two sequences. Once again, I'll create a function to accomplish this.
def comparetwo(seq1, seq2):
    score = 0
    count = 0
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            count += 1
        score += blosum62_df.loc[seq1[i], seq2[i]]
    percentage_identity = (count/len(seq1))*100
    print(f"unchanged amino acid percentage:{percentage_identity:2f}%")
    print(f"total BLOSUM score:{score}")

comparetwo(human_seq, mouse_seq)
comparetwo(human_seq, random_seq)
comparetwo(mouse_seq, random_seq)


















# # alignment.py

# # --- File Paths ---
# # Define the names of your input files.
# # Ensure these files are in the same directory as this script.
# human_fasta_file = "P04179.fasta"
# mouse_fasta_file = "P09671.fasta"
# random_fasta_file = "random_sod2.fasta"
# blosum_file = "blosum62.txt"

# # --- Function to Read FASTA Files ---
# # Reads a simple FASTA file and returns the sequence string.
# # Assumes a single sequence per file.
# def read_fasta(filepath):
#     """Reads a FASTA file and returns the protein sequence."""
#     sequence = ""
#     try:
#         with open(filepath, 'r') as f:
#             for line in f:
#                 line = line.strip() # Remove leading/trailing whitespace
#                 if not line: # Skip empty lines
#                     continue
#                 if line.startswith('>'): # Skip header line
#                     continue
#                 # Append sequence lines, converting to uppercase for consistency with BLOSUM
#                 sequence += line.upper()
#     except FileNotFoundError:
#         print(f"Error: File not found at {filepath}")
#         return None
#     except Exception as e:
#         print(f"Error reading file {filepath}: {e}")
#         return None
#     return sequence

# # --- Function to Read BLOSUM Matrix ---
# # Reads the BLOSUM62 matrix from a text file and stores it in a dictionary of dictionaries.
# # Assumes the file format is similar to the NCBI one (header row, then rows starting with AA).
# def read_blosum(filepath):
#     """Reads a BLOSUM matrix file and returns it as a dict of dicts."""
#     blosum_matrix = {}
#     amino_acids = [] # To store the order of amino acids from the header

#     try:
#         with open(filepath, 'r') as f:
#             # Read header line to get amino acid order
#             # Skip potential comment lines at the start
#             header_line = ""
#             while True:
#                 line = f.readline().strip()
#                 if not line or line.startswith('#'):
#                     continue
#                 header_line = line # Found the first non-comment non-empty line
#                 break

#             if not header_line:
#                  print(f"Error: Could not find header line in BLOSUM file {filepath}")
#                  return None

#             # Split header line by whitespace to get list of amino acids
#             amino_acids = header_line.split()
#             # The NCBI format might have the first char as #, let's make sure we only get AAs
#             # A more robust way might involve checking if each split element is a single character AA code
#             if amino_acids and amino_acids[0].startswith('#'): # Handle common comment character if it was part of header
#                  amino_acids = [aa.lstrip('#') for aa in amino_acids] # Remove # from any AA

#             # Read the rest of the matrix rows
#             for line in f:
#                 line = line.strip()
#                 if not line or line.startswith('#'): # Skip empty or comment lines
#                     continue

#                 values = line.split()
#                 if not values: continue # Skip potentially empty lines after split

#                 row_aa = values[0].upper() # The first element is the amino acid for this row
#                 # The rest are scores, convert to integers. Ensure there are enough scores.
#                 scores_str = values[1:]

#                 if len(scores_str) != len(amino_acids):
#                     print(f"Warning: Mismatch in number of scores ({len(scores_str)}) and header AAs ({len(amino_acids)}) in BLOSUM file line: {line}")
#                     # Depending on strictness, you might return None or try to proceed
#                     continue # Skip this potentially malformed row

#                 scores = [int(x) for x in scores_str]

#                 # Store scores in the dictionary of dictionaries
#                 blosum_matrix[row_aa] = {}
#                 for i in range(len(amino_acids)):
#                      col_aa = amino_acids[i].upper()
#                      blosum_matrix[row_aa][col_aa] = scores[i]

#         # Basic check: Ensure all amino acids listed in the header also have a corresponding row
#         # And that the matrix is somewhat complete (optional but good practice)
#         # print(f"Successfully read matrix with AAs: {list(blosum_matrix.keys())}") # Debug print

#     except FileNotFoundError:
#         print(f"Error: BLOSUM file not found at {filepath}")
#         return None
#     except ValueError:
#          print(f"Error: Could not parse score as integer in BLOSUM file line: {line}")
#          return None
#     except Exception as e:
#         print(f"Error reading BLOSUM file {filepath}: {e}")
#         return None

#     return blosum_matrix


# # --- Function to Perform Non-Gapped Global Alignment ---
# # Calculates total BLOSUM score and percentage identity for two sequences.
# def perform_alignment(seq1_name, seq1, seq2_name, seq2, blosum_matrix):
#     """
#     Performs non-gapped global alignment score calculation
#     and returns the total score and percentage identity.
#     """
#     if len(seq1) != len(seq2):
#         print(f"Error: Sequences '{seq1_name}' and '{seq2_name}' have different lengths ({len(seq1)} vs {len(seq2)}). Cannot perform non-gapped alignment.")
#         return None, None, None # Indicate failure

#     if not seq1: # Handle empty sequences
#         print(f"Warning: One or both sequences are empty for '{seq1_name}' vs '{seq2_name}'.")
#         return 0, 0.0, 0

#     total_score = 0
#     identity_count = 0
#     sequence_length = len(seq1)

#     # Perform the alignment position by position
#     for i in range(sequence_length):
#         aa1 = seq1[i]
#         aa2 = seq2[i]

#         # Get score from BLOSUM matrix
#         score = 0 # Default score if AA pair not found (e.g., 'X' vs something)
#         # Look up score in the matrix (order matters if matrix wasn't symmetric,
#         # but BLOSUM is symmetric, checking aa1 then aa2 is usually sufficient)
#         # Ensure amino acids exist in the matrix keys before lookup
#         if aa1 in blosum_matrix and aa2 in blosum_matrix[aa1]:
#              score = blosum_matrix[aa1][aa2]
#         elif aa2 in blosum_matrix and aa1 in blosum_matrix[aa2]: # Redundant for BLOSUM, but safe check
#              score = blosum_matrix[aa2][aa1]
#         else:
#              # Handle cases like 'X' or other non-standard AAs not explicitly in matrix
#              # print(f"Warning: Amino acid pair '{aa1}-{aa2}' not explicitly found in BLOSUM matrix at position {i}. Assigning score 0.")
#              # BLOSUM62 matrix from NCBI typically includes B, Z, X, *
#              # If your file is different, you might need a more robust check or default penalty
#              pass # score remains 0


#         total_score += score

#         # Check for identity (exact match)
#         if aa1 == aa2:
#             identity_count += 1

#     # Calculate percentage identity
#     percentage_identity = (identity_count / sequence_length) * 100

#     return total_score, percentage_identity, sequence_length

# # --- Main Execution Block ---
# # This is where the script starts running.

# if __name__ == "__main__": # This standard Python construct ensures the code runs when the script is executed directly

#     print("--- Starting Sequence Alignment ---")

#     # Step 1: Read the BLOSUM matrix
#     print(f"Reading BLOSUM matrix from {blosum_file}...")
#     blosum_matrix = read_blosum(blosum_file)

#     if blosum_matrix is None:
#         print("Failed to load BLOSUM matrix. Exiting.")
#     else:
#         print("BLOSUM matrix loaded successfully.")
#         # Optional: Print a part of the matrix to verify
#         # print("Sample BLOSUM matrix entry (A vs R):", blosum_matrix.get('A', {}).get('R', 'Not found'))


#         # Step 2: Read the sequences
#         print("\nReading sequences...")
#         seq_human = read_fasta(human_fasta_file)
#         seq_mouse = read_fasta(mouse_fasta_file)
#         seq_random = read_fasta(random_fasta_file)

#         if seq_human is None or seq_mouse is None or seq_random is None:
#             print("Failed to read one or more sequence files. Exiting.")
#         else:
#             print("Sequences loaded successfully.")
#             # Optional: Print sequence lengths to confirm they are the same
#             # print(f"Human length: {len(seq_human)}, Mouse length: {len(seq_mouse)}, Random length: {len(seq_random)}")
#             if not (len(seq_human) == len(seq_mouse) == len(seq_random)):
#                  print("Warning: Sequence lengths are not all equal. Non-gapped alignment requires equal lengths.")


#             # Step 3: Perform and print alignments for the three pairs
#             print("\n--- Performing Alignments ---")

#             # Human vs Mouse
#             print("\nAlignment: Human vs Mouse")
#             score_hm, identity_hm, length_hm = perform_alignment("Human SOD2", seq_human, "Mouse SOD2", seq_mouse, blosum_matrix)
#             if score_hm is not None:
#                 print(f"  Sequence Length: {length_hm}")
#                 print(f"  Total BLOSUM Score: {score_hm}")
#                 print(f"  Percentage Identity: {identity_hm:.2f}%") # Format to 2 decimal places

#             # Human vs Random
#             print("\nAlignment: Human vs Random")
#             score_hr, identity_hr, length_hr = perform_alignment("Human SOD2", seq_human, "Random Sequence", seq_random, blosum_matrix)
#             if score_hr is not None:
#                 print(f"  Sequence Length: {length_hr}")
#                 print(f"  Total BLOSUM Score: {score_hr}")
#                 print(f"  Percentage Identity: {identity_hr:.2f}%")

#             # Mouse vs Random
#             print("\nAlignment: Mouse vs Random")
#             score_mr, identity_mr, length_mr = perform_alignment("Mouse SOD2", seq_mouse, "Random Sequence", seq_random, blosum_matrix)
#             if score_mr is not None:
#                 print(f"  Sequence Length: {length_mr}")
#                 print(f"  Total BLOSUM Score: {score_mr}")
#                 print(f"  Percentage Identity: {identity_mr:.2f}%")

#             print("\n--- Alignment Complete ---")

