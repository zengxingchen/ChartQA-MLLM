
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Hiking Trips": [12, 15, 20, 25, 30, 35, 40, 45, 38, 30, 20, 15],
    "Camping Trips": [9, 12, 18, 22, 27, 30, 35, 38, 32, 25, 18, 10],
    "Kayaking Trips": [7, 10, 12, 15, 20, 25, 30, 35, 28, 20, 12, 8]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the index to 'Month'
df.set_index('Month', inplace=True)

# Plot the data
sns.set(style="whitegrid")
plt.figure(figsize=(14, 10))
plt.stackplot(df.index, df["Hiking Trips"], df["Camping Trips"], df["Kayaking Trips"], 
              colors=['#1f77b4', '#ff7f0e', '#2ca02c'], 
              labels=['Hiking Trips', 'Camping Trips', 'Kayaking Trips'])
plt.legend(loc='upper right')
plt.title('Monthly Outdoor Activities', fontsize=18, pad=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Number of Trips', fontsize=14)

# Adding Annotations/Labels
for i, row in df.iterrows():
    plt.text(i, row.sum() + 2, str(row.sum()), fontsize=10, horizontalalignment='center')

plt.show()