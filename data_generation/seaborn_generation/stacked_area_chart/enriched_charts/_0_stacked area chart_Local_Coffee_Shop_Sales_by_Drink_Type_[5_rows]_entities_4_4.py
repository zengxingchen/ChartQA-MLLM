
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Butterflies": [20, 25, 30, 60, 80, 100, 90, 70, 60, 50, 30, 25],
    "Bees": [35, 40, 50, 65, 70, 90, 80, 75, 65, 55, 40, 35],
    "Birds": [78, 85, 90, 120, 130, 140, 150, 160, 155, 145, 100, 80]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the index to 'Month'
df.set_index('Month', inplace=True)

# Plot the data
sns.set(style="whitegrid")
plt.figure(figsize=(12, 8))
plt.stackplot(df.index, df["Butterflies"], df["Bees"], df["Birds"], 
              colors=['#FFD700', '#FF69B4', '#1E90FF'], 
              labels=['Butterflies', 'Bees', 'Birds'])
plt.legend(loc='upper left')
plt.title('Park Wildlife Observations by Month')
plt.xlabel('Month')
plt.ylabel('Number of Observations')

# Adding Annotations/Labels
for i, row in df.iterrows():
    plt.text(i, row.sum(), str(row.sum()), fontsize=9, horizontalalignment='center')

plt.show()