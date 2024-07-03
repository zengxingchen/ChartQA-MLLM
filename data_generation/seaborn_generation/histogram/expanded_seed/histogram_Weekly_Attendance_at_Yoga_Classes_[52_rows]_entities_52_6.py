
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Given chart table data
data = [
    {'Week': 1, 'Participants': 23},
    {'Week': 2, 'Participants': 27},
    {'Week': 3, 'Participants': 25},
    {'Week': 4, 'Participants': 22},
    {'Week': 5, 'Participants': 30},
    {'Week': 6, 'Participants': 21},
    {'Week': 7, 'Participants': 33},
    {'Week': 8, 'Participants': 35},
    {'Week': 9, 'Participants': 19},
    {'Week': 10, 'Participants': 24},
    {'Week': 11, 'Participants': 28},
    {'Week': 12, 'Participants': 31},
    {'Week': 13, 'Participants': 27},
    {'Week': 14, 'Participants': 22},
    {'Week': 15, 'Participants': 20}
]

# Convert data to pandas DataFrame
df = pd.DataFrame(data)

# Set the style and color palette of the plot
sns.set_style("whitegrid")
sns.set_palette("pastel")

# Plot the histogram using Seaborn
plt.figure(figsize=(10, 6))
sns.histplot(df['Participants'], bins=15, kde=True, color='skyblue', edgecolor='black')

# Customize the plot with titles and labels
plt.title('Distribution of Participants Over Weeks', fontsize=16)
plt.xlabel('Number of Participants', fontsize=14)
plt.ylabel('Frequency', fontsize=14)

# Show the plot
plt.show()