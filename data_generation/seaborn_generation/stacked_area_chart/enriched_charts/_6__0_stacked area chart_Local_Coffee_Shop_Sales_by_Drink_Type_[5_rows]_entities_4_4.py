
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Visitors": [100, 150, 200, 250, 300, 350, 400, 450, 300, 250, 200, 150],
    "Revenue": [5000, 7500, 12000, 16000, 20000, 25000, 30000, 35000, 20000, 16000, 12000, 7500],
    "Events": [5, 7, 10, 12, 15, 18, 20, 22, 15, 12, 10, 7]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the index to 'Month'
df.set_index('Month', inplace=True)

# Plot the data
sns.set(style="whitegrid")
plt.figure(figsize=(14, 10))
plt.stackplot(df.index, df["Visitors"], df["Revenue"], df["Events"], 
              colors=['#2E8B57', '#FF6347', '#4682B4'], 
              labels=['Visitors', 'Revenue', 'Events'])
plt.legend(loc='upper left')
plt.title('Annual Festival Overview by Month')
plt.xlabel('Month')
plt.ylabel('Values')

# Adding Annotations/Labels
for i, row in df.iterrows():
    plt.text(i, row.sum(), str(row.sum()), fontsize=9, horizontalalignment='center')

plt.show()