
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "SciFi": [8, 9, 11, 13, 15, 18, 21, 23, 25, 28, 30, 33],
    "Fantasy": [12, 13, 15, 17, 20, 23, 26, 29, 32, 35, 37, 40],
    "Mystery": [18, 20, 22, 25, 28, 30, 32, 35, 38, 40, 42, 45]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the index to 'Month'
df.set_index('Month', inplace=True)

# Plot the data
sns.set(style="whitegrid")
plt.figure(figsize=(16, 8))
plt.stackplot(df.index, df["SciFi"], df["Fantasy"], df["Mystery"], 
              colors=['#1f77b4', '#ff7f0e', '#2ca02c'], 
              labels=['Sci-Fi', 'Fantasy', 'Mystery'])
plt.legend(loc='upper left')
plt.title('Monthly Book Sales by Genre', fontsize=16, y=1.02)
plt.xlabel('Month')
plt.ylabel('Number of Books Sold')

# Adding Annotations/Labels
for i, row in df.iterrows():
    plt.text(i, row.sum() + 2, str(row.sum()), fontsize=9, horizontalalignment='center')

plt.show()