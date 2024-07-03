
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Given chart table data
data = [
    {'Participant ID': 1, 'Daily Steps': 5670},
    {'Participant ID': 2, 'Daily Steps': 6890},
    {'Participant ID': 3, 'Daily Steps': 9540},
    {'Participant ID': 4, 'Daily Steps': 7450},
    {'Participant ID': 5, 'Daily Steps': 6430},
    {'Participant ID': 6, 'Daily Steps': 7340},
    {'Participant ID': 7, 'Daily Steps': 8120},
    {'Participant ID': 8, 'Daily Steps': 5090},
    {'Participant ID': 9, 'Daily Steps': 10430},
    {'Participant ID': 10, 'Daily Steps': 5880},
    {'Participant ID': 11, 'Daily Steps': 6550},
    {'Participant ID': 12, 'Daily Steps': 7240},
    {'Participant ID': 13, 'Daily Steps': 9310},
    {'Participant ID': 14, 'Daily Steps': 4870},
    {'Participant ID': 15, 'Daily Steps': 10540}
]

# Convert the data into a Pandas DataFrame
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_style('whitegrid')

# Create the histogram
plt.figure(figsize=(10, 6))

# Plot a histogram with additional visual encodings
hist_plot = sns.histplot(
    df['Daily Steps'],
    bins=8,
    kde=True,
    color='skyblue',
    edgecolor='black',
    linewidth=1.5,
    alpha=0.7
)

# Set titles and labels
plt.title('Distribution of Daily Steps Among Participants', fontsize=16)
plt.xlabel('Daily Steps', fontsize=14)
plt.ylabel('Frequency', fontsize=14)

# Display the plot
plt.show()