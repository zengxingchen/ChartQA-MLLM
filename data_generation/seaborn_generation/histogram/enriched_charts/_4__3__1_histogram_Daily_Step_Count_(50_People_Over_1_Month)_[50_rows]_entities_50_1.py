
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create the DataFrame directly from the data provided
data = {
    'Exercise Duration (minutes)': [
        5, 10, 15, 20, 25, 30, 35, 40, 45, 50,
        55, 60, 65, 70, 75, 80, 85, 90, 95, 100,
        105, 110, 115, 120, 125, 130, 135, 140, 145, 150,
        155, 160, 165, 170, 175, 180, 185, 190, 195, 200
    ]
}
df = pd.DataFrame(data)

# Customize the plot size
plt.figure(figsize=(10, 6))

# Plot the histogram with custom bin width (band) and color
sns.histplot(df['Exercise Duration (minutes)'], bins=15, color='#3498db', kde=False, binwidth=15)

# Customize the plot labels and title
plt.title('Distribution of Exercise Duration Among Individuals', fontsize=15, pad=20)
plt.xlabel('Exercise Duration (minutes)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

# Rotate the chart to horizontal
plt.gca().invert_yaxis()

# Show the plot
plt.show()