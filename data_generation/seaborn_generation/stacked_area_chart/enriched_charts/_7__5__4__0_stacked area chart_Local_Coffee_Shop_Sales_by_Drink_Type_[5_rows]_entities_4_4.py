
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Vegetables": [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105],
    "Fruits": [30, 32, 35, 37, 40, 43, 45, 48, 50, 53, 55, 58],
    "Proteins": [25, 28, 30, 32, 35, 37, 40, 42, 45, 47, 50, 52],
    "Carbohydrates": [35, 38, 40, 42, 45, 47, 50, 52, 55, 57, 60, 62]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the index to 'Month'
df.set_index('Month', inplace=True)

# Plot the data
sns.set(style="whitegrid")
plt.figure(figsize=(18, 14))
plt.stackplot(df.index, df["Vegetables"], df["Fruits"], df["Proteins"], df["Carbohydrates"], 
              colors=['#FF6347', '#FFA07A', '#20B2AA', '#3CB371'], 
              labels=['Vegetables', 'Fruits', 'Proteins', 'Carbohydrates'])
plt.legend(loc='upper left')
plt.title('Monthly Food Consumption Patterns', fontsize=18)
plt.xlabel('Month', fontsize=16)
plt.ylabel('Quantity Consumed', fontsize=16)

# Adding Annotations/Labels
for i, row in df.iterrows():
    plt.text(i, row.sum() + 5, str(row.sum()), fontsize=10, horizontalalignment='center')

plt.show()