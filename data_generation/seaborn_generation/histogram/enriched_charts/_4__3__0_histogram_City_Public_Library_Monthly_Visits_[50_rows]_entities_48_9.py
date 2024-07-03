
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
reading_data = {
    "reading_time": [
        5, 10, 15, 10, 20, 25, 15, 20, 25, 30, 35, 15, 20, 25, 30, 40, 45, 50, 20, 15, 10, 5, 10, 20, 25, 30, 35, 40, 45, 50,
        35, 30, 25, 20, 15, 10, 5, 15, 25, 35, 45, 10, 20, 30, 40, 50, 25, 30, 35, 40, 45, 50, 30, 25, 20, 15, 10, 5, 15, 20, 25, 30, 35, 40, 45, 50
    ]
}

# Create DataFrame
df = pd.DataFrame(data=reading_data)

# Set the style and color palette
sns.set(style="whitegrid")
palette = ["#FF5733", "#33FF57", "#3357FF", "#FF33A6", "#FFBD33"]

# Create the histogram chart
plt.figure(figsize=(14, 10))
sns.histplot(df['reading_time'], kde=False, color="#33FF57", bins=15, binwidth=3)

# Additional styling options
plt.title('Daily Reading Time of Participants', pad=20)
plt.xlabel('Reading Time (minutes)')
plt.ylabel('Frequency')
plt.ylim(0, None)
plt.gca().invert_yaxis()  # Invert the direction of the chart to horizontal

# Save or show the figure
plt.savefig('reading_time_distribution.png')
plt.show()