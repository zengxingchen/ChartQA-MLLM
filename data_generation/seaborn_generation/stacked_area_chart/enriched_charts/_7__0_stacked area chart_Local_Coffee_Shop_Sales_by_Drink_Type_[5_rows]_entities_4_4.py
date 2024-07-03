
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Adventure Walks": [15, 25, 40, 55, 70, 85, 100, 95, 80, 65, 50, 35],
    "Hiking": [30, 35, 50, 65, 80, 95, 110, 105, 90, 75, 60, 45],
    "Mountain Climbing": [45, 50, 65, 80, 95, 110, 125, 120, 105, 90, 75, 60]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the index to 'Month'
df.set_index('Month', inplace=True)

# Plot the data
sns.set(style="whitegrid")
plt.figure(figsize=(14, 10))
plt.stackplot(df.index, df["Adventure Walks"], df["Hiking"], df["Mountain Climbing"], 
              colors=['#FFA07A', '#20B2AA', '#778899'], 
              labels=['Adventure Walks', 'Hiking', 'Mountain Climbing'])
plt.legend(loc='upper left')
plt.title('Outdoor Activities by Month', fontsize=18, pad=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Number of Participants', fontsize=14)

# Adding Annotations/Labels
for i, row in df.iterrows():
    plt.text(i, row.sum() + 5, str(row.sum()), fontsize=9, horizontalalignment='center')

plt.show()