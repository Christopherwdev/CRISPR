import pandas as pd

def calculate_gc_content(sequence):
    """Calculates GC content of a nucleotide sequence."""
    return (sequence.count('G') + sequence.count('C')) / len(sequence)

def engineer_features(data):
    """Engineers features from gRNA and target sequences."""
    data["gRNA_GC"] = data["gRNA_sequence"].apply(calculate_gc_content)
    data["target_GC"] = data["target_sequence"].apply(calculate_gc_content)
    # Add more feature engineering functions here...
    return data
