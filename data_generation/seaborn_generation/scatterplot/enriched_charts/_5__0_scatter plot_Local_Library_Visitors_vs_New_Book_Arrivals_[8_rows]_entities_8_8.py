
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Generate the data
data = {
    'Hours Slept': [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
        3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5
    ],
    'Happiness Score': [
        45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100,
        52, 58, 63, 68, 78, 83, 88, 92, 98
    ]
}

# Create a Pandas DataFrame
df = pd.DataFrame(data)

# Define a color palette
palette = {
    45: "#ff6347",  # Tomato
    50: "#ff4500",  # OrangeRed
    55: "#ffa500",  # Orange
    60: "#ffd700",  # Gold
    65: "#adff2f",  # GreenYellow
    70: "#32cd32",  # LimeGreen
    75: "#00fa9a",  # MediumSpringGreen
    80: "#00ced1",  # DarkTurquoise
    85: "#1e90ff",  # DodgerBlue
    90: "#4169e1",  # RoyalBlue
    95: "#8a2be2",  # BlueViolet
    100: "#9400d3",  # DarkViolet
    52: "#ff7f50",  # Coral
    58: "#ff8c00",  # DarkOrange
    63: "#ffd700",  # Gold
    68: "#9acd32",  # YellowGreen
    78: "#66cdaa",  # MediumAquamarine
    83: "#4682b4",  # SteelBlue
    88: "#6a5acd",  # SlateBlue
    92: "#7b68ee",  # MediumSlateBlue
    98: "#8b0000",  # DarkRed
}

# Create a scatter plot
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Hours Slept', y='Happiness Score', data=df, palette=palette, hue='Happiness Score', s=100, edgecolor='#333333', linewidth=1)

# Title and labels
plt.title('Correlation between Hours Slept and Happiness Score', fontsize=18, pad=20)
plt.xlabel('Hours Slept', fontsize=14)
plt.ylabel('Happiness Score', fontsize=14)

# Show plot
plt.legend(title='Happiness Score', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()