
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Concerts": [10, 12, 20, 25, 30, 35, 40, 50, 55, 60, 65, 70],
    "Plays": [15, 18, 25, 30, 35, 40, 50, 55, 60, 65, 70, 75],
    "Exhibitions": [25, 22, 30, 40, 45, 50, 60, 65, 70, 75, 80, 85]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the index to 'Month'
df.set_index('Month', inplace=True)

# Plot the data
sns.set(style="whitegrid")
plt.figure(figsize=(14, 10))
plt.stackplot(df.index, df["Concerts"], df["Plays"], df["Exhibitions"], 
              colors=['#7B68EE', '#FF6347', '#32CD32'], 
              labels=['Concerts', 'Plays', 'Exhibitions'])
plt.legend(loc='upper left')
plt.title('Monthly Music and Performing Arts Events')
plt.xlabel('Month')
plt.ylabel('Number of Events')

# Adding Annotations/Labels
for i, row in df.iterrows():
    plt.text(i, row.sum() + 5, str(row.sum()), fontsize=9, horizontalalignment='center')

plt.show()