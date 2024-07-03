
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
knowledge_data = {
    "knowledge_level": [
        1, 2, 3, 2, 4, 5, 3, 4, 5, 6, 7, 3, 4, 5, 6, 8, 9, 10, 4, 3, 2, 1, 2, 4, 5, 6, 7, 8, 9, 10,
        7, 6, 5, 4, 3, 2, 1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 5, 6, 7, 8, 9, 10, 6, 5, 4, 3, 2, 1, 3, 4, 5, 6, 7, 8, 9, 10
    ]
}

# Create DataFrame
df = pd.DataFrame(data=knowledge_data)

# Set the style and color palette
sns.set(style="whitegrid")
palette = ["#3498db", "#e74c3c", "#2ecc71", "#f1c40f", "#9b59b6"]

# Create the histogram chart
plt.figure(figsize=(10, 14))
sns.histplot(df['knowledge_level'], kde=False, color="#2ecc71", bins=20, binwidth=0.5)

# Additional styling options
plt.title('Participants\' Knowledge Levels in AI', pad=20)
plt.xlabel('Knowledge Level')
plt.ylabel('Frequency')
plt.ylim(0, None)

# Save or show the figure
plt.savefig('knowledge_levels_distribution.png')
plt.show()