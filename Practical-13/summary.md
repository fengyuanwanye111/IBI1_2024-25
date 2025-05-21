222AA，from58.1%to100%
unchanged amino acid percentage:90.090090%
total BLOSUM score:1097
unchanged amino acid percentage:3.603604%
total BLOSUM score:-266
unchanged amino acid percentage:3.153153%
total BLOSUM score:-273
Listed above are my answers,and I use AI help me making summary of today's my work


# Practical 13: Sequence Comparisons Summary

This document summarizes the findings from Practical 13, involving online BLAST and a simple Python implementation for non-gapped global sequence alignment.

## 1. Human SOD2 Protein Information

*   **Length:** [Insert the length of the human SOD2 protein in amino acids that you found on UniProt, which your script also confirmed] amino acids.
*   **Subcellular Localisation:** [Insert the subcellular location of the human SOD2 protein that you found on UniProt].

## 2. Online BLAST Results Overview

*   **Total hits found:** [Insert the total number of hits reported by UniProt BLAST, which was 250 based on your screenshot].
*   **Range of percentage identities among hits:** [Insert the range of percentage identities from the BLAST results overview, which was 58.1% - 100% based on your screenshot].
*   **Percentage identity of Human vs Mouse (P09671) BLAST alignment:** [Insert the specific percentage identity for the P09671 hit from the BLAST results, which was 90.1% based on your screenshot].
    *   *Note: In the detailed alignment view, **grey** highlighted residues indicated **Identity** (amino acids are the same), and **blue** highlighted residues indicated **Similarity** (amino acids are different but have a positive BLOSUM score).*

## 3. Python Alignment Results

The following results were obtained from the non-gapped global alignment performed using the Python script `alignment.py` and the BLOSUM62 matrix:

*   **Human vs Mouse Alignment:**
    *   Sequence Length: [Insert the sequence length, which was 222]
    *   Total BLOSUM Score: [Insert the score from your Python script output for Human vs Mouse, which was 1097]
    *   Percentage Identity: [Insert the percentage identity from your Python script output for Human vs Mouse, which was 90.09%]

*   **Human vs Random Alignment:**
    *   Sequence Length: [Insert the sequence length, which was 222]
    *   Total BLOSUM Score: [Insert the score from your Python script output for Human vs Random, which was -266]
    *   Percentage Identity: [Insert the percentage identity from your Python script output for Human vs Random, which was 3.60%]

*   **Mouse vs Random Alignment:**
    *   Sequence Length: [Insert the sequence length, which was 222]
    *   Total BLOSUM Score: [Insert the score from your Python script output for Mouse vs Random, which was -273]
    *   Percentage Identity: [Insert the percentage identity from your Python script output for Mouse vs Random, which was 3.15%]

## 4. Conclusion on Relatedness

Based on the significantly higher total BLOSUM score and percentage identity observed in the Python alignment results, the **Human and Mouse SOD2 protein sequences are the most closely related** among the three pairs compared. Their alignment score and identity percentage are substantially higher than those observed when comparing either Human or Mouse SOD2 to a random sequence of the same length.

