
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Generate the data
data = {
    'Exercise Hours': [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        4.5, 3.5, 5.5, 6.5, 7.5, 8.5, 9.5, 11, 12,
        13, 14, 15, 16
    ],
    'Calories Burned': [
        120, 240, 360, 400, 500, 600, 700, 760, 810, 900,
        420, 380, 530, 650, 770, 820, 870, 1000, 1100,
        1150, 1200, 1250, 1300
    ]
}

# Create a Pandas DataFrame
df = pd.DataFrame(data)

# Define a color palette
palette = {
    120: "#FF6347", 240: "#FFA07A", 360: "#FFD700", 400: "#32CD32",
    500: "#008080", 600: "#4682B4", 700: "#1E90FF", 760: "#7B68EE",
    810: "#8A2BE2", 900: "#9400D3", 420: "#FF69B4", 380: "#FF4500",
    530: "#2E8B57", 650: "#DAA520", 770: "#B0E0E6", 820: "#BA55D3",
    870: "#800080", 1000: "#FF00FF", 1100: "#FF1493", 1150: "#DB7093",
    1200: "#C71585", 1250: "#D2691E", 1300: "#8B4513"
}

# Create a scatter plot
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Exercise Hours', y='Calories Burned', data=df, palette=palette, hue='Calories Burned', s=100, edgecolor='#333333', linewidth=1)

# Title and labels
plt.title('Correlation between Exercise Hours and Calories Burned', fontsize=18)
plt.xlabel('Exercise Hours', fontsize=14)
plt.ylabel('Calories Burned', fontsize=14)

# Show plot
plt.legend(title='Calories Burned', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()