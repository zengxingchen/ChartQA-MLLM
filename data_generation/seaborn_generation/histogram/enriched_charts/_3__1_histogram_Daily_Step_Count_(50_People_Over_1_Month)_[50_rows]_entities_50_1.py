
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create the DataFrame directly from the data provided
data = {
    'Push-ups': [
        10, 15, 20, 25, 30, 35, 40, 45, 50, 55,
        60, 65, 70, 75, 80, 85, 90, 95, 100, 105,
        110, 115, 120, 125, 130, 135, 140, 145, 150, 155,
        160, 165, 170, 175, 180, 185, 190, 195, 200
    ]
}
df = pd.DataFrame(data)

# Customize the plot size
plt.figure(figsize=(12, 8))

# Plot the histogram with custom bin width (band) and color
sns.histplot(df['Push-ups'], bins=20, color='#e74c3c', kde=False, binwidth=10)

# Customize the plot labels and title
plt.title('Distribution of Push-ups Completed by Individuals', fontsize=15, pad=20)
plt.xlabel('Number of Push-ups', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

# Rotate the chart to horizontal
plt.gca().invert_yaxis()

# Show the plot
plt.show()