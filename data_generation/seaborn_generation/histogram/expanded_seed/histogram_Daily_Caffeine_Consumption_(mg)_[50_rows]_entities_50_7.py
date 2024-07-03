
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Your provided data
data = [
    {'Age Bracket': '18-24', 'Caffeine Intake (mg)': 80},
    {'Age Bracket': '18-24', 'Caffeine Intake (mg)': 250},
    {'Age Bracket': '18-24', 'Caffeine Intake (mg)': 90},
    {'Age Bracket': '18-24', 'Caffeine Intake (mg)': 120},
    {'Age Bracket': '18-24', 'Caffeine Intake (mg)': 110},
    {'Age Bracket': '25-34', 'Caffeine Intake (mg)': 300},
    {'Age Bracket': '25-34', 'Caffeine Intake (mg)': 80},
    {'Age Bracket': '25-34', 'Caffeine Intake (mg)': 220},
    {'Age Bracket': '25-34', 'Caffeine Intake (mg)': 150},
    {'Age Bracket': '25-34', 'Caffeine Intake (mg)': 170},
    {'Age Bracket': '35-44', 'Caffeine Intake (mg)': 85},
    {'Age Bracket': '35-44', 'Caffeine Intake (mg)': 130},
    {'Age Bracket': '35-44', 'Caffeine Intake (mg)': 250},
    {'Age Bracket': '35-44', 'Caffeine Intake (mg)': 200},
    {'Age Bracket': '35-44', 'Caffeine Intake (mg)': 190}
]

# Convert the list of dictionaries into a Pandas DataFrame
df = pd.DataFrame(data)

# Set the style and context of the Seaborn plots
sns.set(style="whitegrid", context="talk")

# Create a histogram using Seaborn's histplot
plt.figure(figsize=(10, 6))
hist_plot = sns.histplot(data=df, x='Caffeine Intake (mg)', hue='Age Bracket', multiple='stack', palette='viridis', edgecolor='black')

# Add titles and labels
plt.title('Histogram of Caffeine Intake by Age Bracket', fontsize=18)
plt.xlabel('Caffeine Intake (mg)', fontsize=14)
plt.ylabel('Frequency', fontsize=14)

# Improve layout
plt.tight_layout()

# Add a legend to the plot
plt.legend(title='Age Bracket', bbox_to_anchor=(1.01, 1), loc='upper left')

# Show the plot
plt.show()