
import seaborn as sns
import matplotlib.pyplot as plt

# Given data
data = [
    {'Day': 1, 'Riders': 3402}, {'Day': 2, 'Riders': 3210}, {'Day': 3, 'Riders': 3655},
    {'Day': 4, 'Riders': 3122}, {'Day': 5, 'Riders': 3300}, {'Day': 6, 'Riders': 3431},
    {'Day': 7, 'Riders': 3550}, {'Day': 8, 'Riders': 3622}, {'Day': 9, 'Riders': 3488},
    {'Day': 10, 'Riders': 3222}, {'Day': 11, 'Riders': 3666}, {'Day': 12, 'Riders': 3804},
    {'Day': 13, 'Riders': 3599}, {'Day': 14, 'Riders': 3711}, {'Day': 15, 'Riders': 3644}
]

# Convert list of dictionaries to a pandas DataFrame
import pandas as pd
df = pd.DataFrame(data)

# Set the style and color palette of the plot
sns.set_style("whitegrid")
sns.set_palette("pastel")

# Initialize the matplotlib figure
plt.figure(figsize=(10, 6))

# Create a histogram based on the 'Riders' column
sns.histplot(df['Riders'], bins=8, kde=True, color="skyblue", edgecolor="gray")

# Add a vertical line for the mean
mean_value = df['Riders'].mean()
plt.axvline(mean_value, color='red', linestyle='--')

# Annotate the mean line
plt.text(mean_value + 20, 2, f'Mean: {mean_value:.2f}', color='red', fontsize=12)

# Set titles and labels
plt.title('Histogram of Daily Riders', fontsize=16)
plt.xlabel('Number of Riders', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

# Remove the top and right spines for aesthetics
sns.despine(top=True, right=True)

# Show the plot
plt.show()