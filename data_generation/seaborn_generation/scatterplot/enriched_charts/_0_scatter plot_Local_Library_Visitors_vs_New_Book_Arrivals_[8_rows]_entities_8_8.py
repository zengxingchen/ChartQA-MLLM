
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Generate the data
data = {
    'Hours Studied': [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        4.5, 3.5, 5.5, 6.5, 7.5, 8.5, 9.5, 11, 12
    ],
    'Test Score': [
        55, 65, 75, 80, 80, 83, 90, 88, 94, 95,
        77, 70, 82, 85, 91, 93, 96, 98, 99
    ]
}

# Create a Pandas DataFrame
df = pd.DataFrame(data)

# Define a color palette
palette = {
    55: "#ff0000",
    65: "#ffa500",
    75: "#ffff00",
    80: "#008000",
    83: "#0000ff",
    90: "#4b0082",
    88: "#800080",
    94: "#ee82ee",
    95: "#ffa07a",
    77: "#ff4500",
    70: "#ffd700",
    82: "#006400",
    85: "#1e90ff",
    91: "#9400d3",
    93: "#9932cc",
    96: "#c71585",
    98: "#db7093",
    99: "#ff1493",
}

# Create a scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Hours Studied', y='Test Score', data=df, palette=palette, hue='Test Score', s=100, edgecolor='#333333', linewidth=1)

# Title and labels
plt.title('Correlation between Hours Studied and Test Score', fontsize=18)
plt.xlabel('Hours Studied', fontsize=12)
plt.ylabel('Test Score', fontsize=12)

# Show plot
plt.legend(title='Test Score', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()