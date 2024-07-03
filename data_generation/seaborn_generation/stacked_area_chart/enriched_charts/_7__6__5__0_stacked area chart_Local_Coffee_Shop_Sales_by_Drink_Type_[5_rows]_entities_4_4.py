
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Meditation": [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],
    "Yoga": [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    "Therapy": [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the index to 'Month'
df.set_index('Month', inplace=True)

# Plot the data
sns.set(style="whitegrid")
plt.figure(figsize=(18, 14))
plt.stackplot(df.index, df["Meditation"], df["Yoga"], df["Therapy"], 
              colors=['#FF6347', '#4682B4', '#8A2BE2'], 
              labels=['Meditation', 'Yoga', 'Therapy'])
plt.legend(loc='upper left')
plt.title('Monthly Participation in Mental Wellness Activities', fontsize=20, y=1.02)
plt.xlabel('Month')
plt.ylabel('Number of Participants')

# Adding Annotations/Labels
for i, row in df.iterrows():
    plt.text(i, row.sum() + 5, str(row.sum()), fontsize=10, horizontalalignment='center')

plt.show()