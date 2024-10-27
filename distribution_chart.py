import json
from collections import Counter
import plotly.express as px

# Load JSONL data from the category_data folder
data = []
with open('category_data/test_set.jsonl', 'r') as file:  # Replace with other file names if needed
    for line in file:
        data.append(json.loads(line.strip()))

# Assuming each entry in data has a "Labels" field, count all labels
all_labels = [label for entry in data for label in entry['Labels']]

# Count occurrences of each label
label_counts = Counter(all_labels)

# Prepare data for Plotly
labels = list(label_counts.keys())
counts = list(label_counts.values())

# Plot with Plotly
fig = px.bar(x=labels, y=counts, title="Label Distribution", labels={'x': 'Labels', 'y': 'Frequency'})
fig.show()
