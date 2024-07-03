
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Calories": [2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100],
    "Burned": [500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050],
    "Net": [1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000, 2050]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the index to 'Month'
df.set_index('Month', inplace=True)

# Plot the data
sns.set(style="whitegrid")
plt.figure(figsize=(20, 16))
plt.stackplot(df.index, df["Calories"], df["Burned"], df["Net"], 
              colors=['#FF7F50', '#6495ED', '#9ACD32'], 
              labels=['Calories', 'Burned', 'Net'])
plt.legend(loc='upper left')
plt.title('Monthly Caloric Intake and Burned', fontsize=20)
plt.xlabel('Month', fontsize=18)
plt.ylabel('Calories', fontsize=18)

# Adding Annotations/Labels
for i, row in df.iterrows():
    plt.text(i, row.sum() + 50, str(row.sum()), fontsize=12, horizontalalignment='center')

plt.show()