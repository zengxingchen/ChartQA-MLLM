
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Camping": [12, 18, 22, 28, 32, 38, 42, 48, 52, 58, 62, 68],
    "Mountain Climbing": [22, 28, 32, 38, 42, 48, 52, 58, 62, 68, 72, 78],
    "Skiing": [32, 38, 42, 48, 52, 58, 62, 68, 72, 78, 82, 88]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the index to 'Month'
df.set_index('Month', inplace=True)

# Plot the data
sns.set(style="whitegrid")
plt.figure(figsize=(16, 12))
plt.stackplot(df.index, df["Camping"], df["Mountain Climbing"], df["Skiing"], 
              colors=['#1E90FF', '#32CD32', '#FFD700'], 
              labels=['Camping', 'Mountain Climbing', 'Skiing'])
plt.legend(loc='upper left')
plt.title('Monthly Outdoor Activities Participation', fontsize=18, y=1.05)
plt.xlabel('Month')
plt.ylabel('Number of Participants')

# Adding Annotations/Labels
for i, row in df.iterrows():
    plt.text(i, row.sum() + 5, str(row.sum()), fontsize=10, horizontalalignment='center')

plt.show()