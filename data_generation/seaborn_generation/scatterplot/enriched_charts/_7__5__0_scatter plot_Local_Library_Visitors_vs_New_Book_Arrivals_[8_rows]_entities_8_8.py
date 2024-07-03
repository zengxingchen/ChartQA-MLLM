
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Generate the data
data = {
    'Exercise Duration': [
        10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60,
        12, 17, 22, 27, 32, 37, 42, 47, 52, 57, 62, 67
    ],
    'Calories Burned': [
        100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600,
        150, 175, 225, 275, 325, 375, 425, 475, 525, 575, 625, 675
    ]
}

# Create a Pandas DataFrame
df = pd.DataFrame(data)

# Define a new color palette
palette = {
    100: "#1f77b4",
    150: "#ff7f0e",
    200: "#2ca02c",
    250: "#d62728",
    300: "#9467bd",
    350: "#8c564b",
    400: "#e377c2",
    450: "#7f7f7f",
    500: "#bcbd22",
    550: "#17becf",
    600: "#aec7e8",
    175: "#ff9896",
    225: "#c5b0d5",
    275: "#c49c94",
    325: "#f7b6d2",
    375: "#c7c7c7",
    425: "#dbdb8d",
    475: "#9edae5",
    525: "#ffbb78",
    575: "#98df8a",
    625: "#ff9896",
    675: "#c7c7c7"
}

# Create a scatter plot
plt.figure(figsize=(14, 10))
sns.scatterplot(x='Exercise Duration', y='Calories Burned', data=df, palette=palette, hue='Calories Burned', s=100, edgecolor='#333333', linewidth=1)

# Title and labels
plt.title('Correlation between Exercise Duration and Calories Burned', fontsize=18, pad=20)
plt.xlabel('Exercise Duration (minutes)', fontsize=14)
plt.ylabel('Calories Burned', fontsize=14)

# Show plot
plt.legend(title='Calories Burned', bbox_to_anchor=(1.05, 1))
plt.tight_layout()
plt.show()