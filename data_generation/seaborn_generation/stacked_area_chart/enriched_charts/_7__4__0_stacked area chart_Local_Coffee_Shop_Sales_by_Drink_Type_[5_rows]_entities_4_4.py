
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Temperature (°C)": [5, 6, 10, 15, 20, 25, 30, 29, 25, 18, 10, 7],
    "Precipitation (mm)": [78, 55, 80, 120, 90, 100, 150, 130, 110, 95, 85, 75],
    "Sunlight Hours": [150, 160, 200, 220, 240, 260, 280, 270, 250, 220, 190, 160]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the index to 'Month'
df.set_index('Month', inplace=True)

# Plot the data
sns.set(style="whitegrid")
plt.figure(figsize=(16, 12))
plt.stackplot(df.index, df["Temperature (°C)"], df["Precipitation (mm)"], df["Sunlight Hours"], 
              colors=['#4682B4', '#FFD700', '#32CD32'], 
              labels=['Temperature (°C)', 'Precipitation (mm)', 'Sunlight Hours'])
plt.legend(loc='upper left')
plt.title('Monthly Climate Data', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Values', fontsize=14)

# Adding Annotations/Labels
for i, row in df.iterrows():
    plt.text(i, row.sum() + 5, str(row.sum()), fontsize=9, horizontalalignment='center')

plt.show()