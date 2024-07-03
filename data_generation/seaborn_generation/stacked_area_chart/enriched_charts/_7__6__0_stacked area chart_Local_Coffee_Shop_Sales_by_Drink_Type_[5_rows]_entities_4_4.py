
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Attendance": [120, 160, 220, 270, 320, 370, 420, 470, 350, 300, 250, 200],
    "Revenue": [6000, 8000, 14000, 18000, 22000, 27000, 32000, 37000, 21000, 18000, 14000, 10000],
    "New Memberships": [8, 10, 15, 20, 25, 30, 35, 40, 28, 22, 18, 12]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the index to 'Month'
df.set_index('Month', inplace=True)

# Plot the data
sns.set(style="whitegrid")
plt.figure(figsize=(16, 12))
plt.stackplot(df.index, df["Attendance"], df["Revenue"], df["New Memberships"], 
              colors=['#4B0082', '#FFD700', '#8A2BE2'], 
              labels=['Attendance', 'Revenue', 'New Memberships'])
plt.legend(loc='upper right')
plt.title('Monthly Gym Attendance and Membership Revenue', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Values', fontsize=14)

# Adding Annotations/Labels
for i, row in df.iterrows():
    plt.text(df.index.get_loc(i), row.sum(), str(row.sum()), fontsize=9, horizontalalignment='center')

plt.show()