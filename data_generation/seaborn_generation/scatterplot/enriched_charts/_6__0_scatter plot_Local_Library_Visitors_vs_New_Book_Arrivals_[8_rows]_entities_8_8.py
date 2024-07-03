
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Generate the data
data = {
    'Parameter': [
        10, 15, 20, 25, 30, 35, 40, 45, 50, 55,
        12, 18, 22, 28, 32, 38, 42, 48, 52, 56
    ],
    'Measurement': [
        220, 330, 450, 500, 600, 700, 800, 850, 920, 950,
        290, 390, 480, 560, 650, 740, 820, 900, 930, 960
    ]
}

# Create a Pandas DataFrame
df = pd.DataFrame(data)

# Define a color palette
palette = {
    220: "#1f77b4",
    330: "#ff7f0e",
    450: "#2ca02c",
    500: "#d62728",
    600: "#9467bd",
    700: "#8c564b",
    800: "#e377c2",
    850: "#7f7f7f",
    920: "#bcbd22",
    950: "#17becf",
    290: "#1f77b4",
    390: "#ff7f0e",
    480: "#2ca02c",
    560: "#d62728",
    650: "#9467bd",
    740: "#8c564b",
    820: "#e377c2",
    900: "#7f7f7f",
    930: "#bcbd22",
    960: "#17becf",
}

# Create a scatter plot
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Parameter', y='Measurement', data=df, palette=palette, hue='Measurement', s=100, edgecolor='#333333', linewidth=1)

# Title and labels
plt.title('Correlation between Parameters and Measurements', fontsize=18, pad=20)
plt.xlabel('Parameter', fontsize=12)
plt.ylabel('Measurement', fontsize=12)

# Show plot
plt.legend(title='Measurement', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()