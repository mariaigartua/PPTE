# data_contamination_solution_simple.py

import json
import re
from collections import defaultdict, Counter
from random import shuffle
from typing import List, Dict

# Step 1: Load JSONL Files
def load_jsonl(file_path):
    """
    Load data from a JSONL file and return it as a list of dictionaries.
    """
    with open(file_path, 'r') as file:
        lines = [json.loads(line.strip()) for line in file]
    return lines

# Step 2: Consolidate Duplicate Entries
def consolidate_duplicates(data: List[Dict], key_field: str, label_field: str) -> List[Dict]:
    """
    Consolidate duplicate entries by a specified key, merging labels.
    """
    consolidated_data = {}
    for entry in data:
        key = entry[key_field]
        labels = set(entry[label_field])
        
        if key in consolidated_data:
            consolidated_data[key][label_field] = consolidated_data[key][label_field].union(labels)
        else:
            consolidated_data[key] = {k: v for k, v in entry.items()}
            consolidated_data[key][label_field] = labels
    
    return [{**entry, label_field: list(labels)} for entry in consolidated_data.values()]

# Step 3: Resolve Conflicting Labels
def resolve_conflicts(data: List[Dict], key_field: str, label_field: str) -> List[Dict]:
    """
    Resolve conflicting labels by consolidating all unique labels per key.
    """
    conflict_resolved_data = {}
    for entry in data:
        key = entry[key_field]
        labels = set(entry[label_field])
        
        if key in conflict_resolved_data:
            conflict_resolved_data[key][label_field] = conflict_resolved_data[key][label_field].union(labels)
        else:
            conflict_resolved_data[key] = {k: v for k, v in entry.items()}
            conflict_resolved_data[key][label_field] = labels
    
    return [{**entry, label_field: list(labels)} for entry in conflict_resolved_data.values()]

# Step 4: Normalize Text Data
def normalize_text(text: str) -> str:
    """
    Normalize text by converting to lowercase and removing special characters.
    """
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text

# Step 5: Remove Ambiguous or Overly Specific Labels
def standardize_labels(data: List[Dict], label_field: str, mapping: Dict[str, str]) -> List[Dict]:
    """
    Standardize labels by mapping specific labels to broader categories.
    """
    for entry in data:
        standardized_labels = {mapping.get(label, label) for label in entry[label_field]}
        entry[label_field] = list(standardized_labels)
    return data

# Example label mapping
label_mapping = {
    'Behavioral Advertising': 'Advertising',
    'Email Sharing': 'Data Sharing',
    # Add other mappings as needed
}

# Step 6: Partition Data Manually
def partition_data(data: List[Dict], unique_field: str, test_size: float = 0.2) -> (List[Dict], List[Dict]): # type: ignore
    """
    Partition data into training and testing sets based on unique values.
    """
    unique_values = list({entry[unique_field] for entry in data})
    shuffle(unique_values)
    split_idx = int(len(unique_values) * (1 - test_size))
    train_values = set(unique_values[:split_idx])
    test_values = set(unique_values[split_idx:])

    train_data = [entry for entry in data if entry[unique_field] in train_values]
    test_data = [entry for entry in data if entry[unique_field] in test_values]

    return train_data, test_data

# Step 7: Simple Frequency-Based Model
def train_and_evaluate_simple_model(train_data: List[Dict], test_data: List[Dict], text_field: str, label_field: str):
    """
    Train a simple frequency-based model using the most common label as prediction baseline.
    """
    # Get the most common label in training data
    all_labels = [label for entry in train_data for label in entry[label_field]]
    most_common_label = Counter(all_labels).most_common(1)[0][0]

    # Evaluate on test data by always predicting the most common label
    correct_predictions = sum(1 for entry in test_data if most_common_label in entry[label_field])
    accuracy = correct_predictions / len(test_data)

    print("Simple Model Accuracy:", accuracy)
    print("Most common label used for prediction:", most_common_label)

# Main function to execute all steps
def main():
    # Load and combine JSONL files
    train_set1 = load_jsonl('category_data/train_set1.jsonl')
    train_set2 = load_jsonl('category_data/train_set2.jsonl')
    train_set3 = load_jsonl('category_data/train_set3.jsonl')
    test_set = load_jsonl('category_data/test_set.jsonl')

    # Combine all data
    data = train_set1 + train_set2 + train_set3 + test_set

    # Step 2: Consolidate duplicates by "Policy Url"
    consolidated_data = consolidate_duplicates(data, "Policy Url", "Labels")

    # Step 3: Resolve conflicts by "Opt Out Url" and "Hyperlink Text"
    resolved_opt_out_data = resolve_conflicts(consolidated_data, "Opt Out Url", "Labels")
    resolved_data = resolve_conflicts(resolved_opt_out_data, "Hyperlink Text", "Labels")

    # Step 4: Normalize text fields
    for entry in resolved_data:
        entry['Sentence Text'] = normalize_text(entry['Sentence Text'])
        entry['Hyperlink Text'] = normalize_text(entry['Hyperlink Text'])

    # Step 5: Standardize labels
    standardized_data = standardize_labels(resolved_data, "Labels", label_mapping)

    # Step 6: Partition data
    train_data, test_data = partition_data(standardized_data, "Policy Url")

    # Step 7: Train and evaluate simple model
    train_and_evaluate_simple_model(train_data, test_data, "Sentence Text", "Labels")

# Run the main function
if __name__ == "__main__":
    main()
