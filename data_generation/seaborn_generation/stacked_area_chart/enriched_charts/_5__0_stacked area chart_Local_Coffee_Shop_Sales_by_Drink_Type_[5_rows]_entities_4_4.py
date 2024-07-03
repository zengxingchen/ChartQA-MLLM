
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Apples": [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65],
    "Oranges": [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],
    "Bananas": [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the index to 'Month'
df.set_index('Month', inplace=True)

# Plot the data
sns.set(style="whitegrid")
plt.figure(figsize=(14, 10))
plt.stackplot(df.index, df["Apples"], df["Oranges"], df["Bananas"], 
              colors=['#FF6347', '#FFD700', '#32CD32'], 
              labels=['Apples', 'Oranges', 'Bananas'])
plt.legend(loc='upper right')
plt.title('Monthly Fruit Consumption', fontsize=16, y=1.02)
plt.xlabel('Month')
plt.ylabel('Number of Fruits')

# Adding Annotations/Labels
for i, row in df.iterrows():
    plt.text(i, row.sum() + 5, str(row.sum()), fontsize=9, horizontalalignment='center')

plt.show()