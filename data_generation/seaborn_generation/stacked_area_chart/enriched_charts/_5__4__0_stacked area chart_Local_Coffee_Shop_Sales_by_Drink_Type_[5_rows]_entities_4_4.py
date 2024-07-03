
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Domestic Travel": [30, 25, 35, 40, 45, 50, 60, 65, 70, 75, 80, 85],
    "International Travel": [20, 18, 28, 35, 40, 45, 55, 60, 65, 70, 75, 80],
    "Adventure Activities": [15, 12, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the index to 'Month'
df.set_index('Month', inplace=True)

# Plot the data
sns.set(style="whitegrid")
plt.figure(figsize=(16, 12))
plt.stackplot(df.index, df["Domestic Travel"], df["International Travel"], df["Adventure Activities"], 
              colors=['#1E90FF', '#FFD700', '#32CD32'], 
              labels=['Domestic Travel', 'International Travel', 'Adventure Activities'])
plt.legend(loc='upper right')
plt.title('Monthly Travel and Adventure Activities', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Number of Activities', fontsize=14)

# Adding Annotations/Labels
for i, row in df.iterrows():
    plt.text(i, row.sum() + 5, str(row.sum()), fontsize=10, horizontalalignment='center')

plt.show()