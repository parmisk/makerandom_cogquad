#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 13:46:09 2024

@author: khosravip2
"""
import csv
import random

# Defining the task pairs
pair1 = ['AXCPT', 'FLANKER']
pair2 = ['AS', 'STOP']

# Generate all possible combinations for each pair
# ['AXCPT', 'FLANKER'] and ['FLANKER', 'AXCPT']
combinations_pair1 = [pair1, pair1[::-1]]
combinations_pair2 = [pair2, pair2[::-1]]  # ['AS', 'STOP'] and ['STOP', 'AS']

# Generate all possible session sequences (Pair 1 first or Pair 2 first)
all_possible_sequences = []
for combo1 in combinations_pair1:
    for combo2 in combinations_pair2:
        all_possible_sequences.append(combo1 + combo2)
        all_possible_sequences.append(combo2 + combo1)

# Number of subjects
num_subjects = 100

# Ensure each sequence occurs an equal number of times
# Each sequence should occur num_subjects/len(all_possible_sequences) times
sequence_repetition = num_subjects // len(all_possible_sequences)

# Create the final list with equal representation of each sequence
final_sequences = all_possible_sequences * sequence_repetition

# Randomize the order
random.shuffle(final_sequences)

# Check if we have the correct number of sequences
final_sequences = final_sequences[:num_subjects]

# Showing the first 10 sequences as an example
final_sequences[:10]

# Define file path
file_path = '/Users/khosravip2/Downloads/Randomized_Task_Sequences2.csv'

# Create and write to a CSV file
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Writing the header
    writer.writerow(['Subject', 'Task 1', 'Task 2', 'Task 3', 'Task 4'])
    # Writing the sequences
    for i, sequence in enumerate(final_sequences, 1):
        writer.writerow([f"Subject {i}"] + sequence)

file_path
