# Pseudocode
# Function: Find restriction enzyme cut sites
# Input: DNA sequence (dna_sequence), recognition sequence (recognition_sequence)
# Output: List of cut site positions
# Steps:
# 1. Check if DNA sequence and recognition sequence contain only ACGT
#    If invalid, raise error
# 2. Iterate through DNA sequence to find all matches of recognition sequence
#    Match position is the position of the first nucleotide of the recognition sequence
# 3. Return list of match positions
# 4. Provide example call

def find_restriction_sites(dna_sequence, recognition_sequence):
    """
    Find restriction enzyme cut sites in a DNA sequence
    Parameters:
        dna_sequence (str): DNA sequence
        recognition_sequence (str): Restriction enzyme recognition sequence
    Returns:
        list: List of cut site positions (0-based indexing)
    """
    # Check 1: Ensure DNA sequence and recognition sequence contain only ACGT
    valid_nucleotides = set("ACGT")
    if not all(nucleotide in valid_nucleotides for nucleotide in dna_sequence.upper()):
        raise ValueError("Error: DNA sequence must contain only A, C, G, T!")
    if not all(nucleotide in valid_nucleotides for nucleotide in recognition_sequence.upper()):
        raise ValueError("Error: Recognition sequence must contain only A, C, G, T!")

    # Convert sequences to uppercase for consistency
    dna_sequence = dna_sequence.upper()
    recognition_sequence = recognition_sequence.upper()

    # Find all match positions
    cut_sites = []
    recognition_len = len(recognition_sequence)
    for i in range(len(dna_sequence) - recognition_len + 1):
        # Check if subsequence starting at position i matches recognition sequence
        if dna_sequence[i:i + recognition_len] == recognition_sequence:
            cut_sites.append(i)  # Record position of first nucleotide of match

    return cut_sites

# Example call
if __name__ == "__main__":
    try:
        # Example 1: Valid DNA sequence and recognition sequence
        dna = "GGAATTCCCGGAATTCCC"
        recognition = "GAATTC"  # EcoRI recognition sequence
        sites = find_restriction_sites(dna, recognition)
        print(f"DNA sequence: {dna}, Recognition sequence: {recognition}, Cut sites: {sites}")

        # Example 2: Test error case (invalid nucleotides)
        dna_invalid = "GGAATTXCC"
        sites = find_restriction_sites(dna_invalid, recognition)
    except ValueError as e:
        print(e)