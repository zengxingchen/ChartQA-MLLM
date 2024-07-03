
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Recycling Events": [8, 15, 20, 25, 28, 30, 35, 38, 40, 45, 48, 50],
    "Tree Planting Events": [10, 18, 25, 30, 32, 35, 38, 40, 45, 48, 50, 55],
    "Environmental Workshops": [12, 22, 28, 35, 40, 45, 50, 55, 60, 65, 70, 75]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the index to 'Month'
df.set_index('Month', inplace=True)

# Plot the data
sns.set(style="whitegrid")
plt.figure(figsize=(16, 12))
plt.stackplot(df.index, df["Recycling Events"], df["Tree Planting Events"], df["Environmental Workshops"], 
              colors=['#4682B4', '#FFA500', '#228B22'], 
              labels=['Recycling Events', 'Tree Planting Events', 'Environmental Workshops'])
plt.legend(loc='upper left')
plt.title('Monthly Environmental Events', fontsize=18, pad=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Number of Events', fontsize=14)

# Adding Annotations/Labels
for i, row in df.iterrows():
    plt.text(i, row.sum() + 5, str(row.sum()), fontsize=10, horizontalalignment='center')

plt.show()