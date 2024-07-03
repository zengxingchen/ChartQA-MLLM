
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Expenses": [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105],
    "Revenue": [40, 42, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90],
    "Profit": [10, 13, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the index to 'Month'
df.set_index('Month', inplace=True)

# Plot the data
sns.set(style="whitegrid")
plt.figure(figsize=(18, 14))
plt.stackplot(df.index, df["Expenses"], df["Revenue"], df["Profit"], 
              colors=['#FF6347', '#4682B4', '#3CB371'], 
              labels=['Expenses', 'Revenue', 'Profit'])
plt.legend(loc='upper left')
plt.title('Monthly Business Performance', fontsize=18)
plt.xlabel('Month', fontsize=16)
plt.ylabel('Amount (in thousands)', fontsize=16)

# Adding Annotations/Labels
for i, row in df.iterrows():
    plt.text(i, row.sum() + 5, str(row.sum()), fontsize=12, horizontalalignment='center')

plt.show()