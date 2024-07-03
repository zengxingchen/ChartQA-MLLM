
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
height_data = {
    "height": [
        150, 160, 155, 165, 170, 160, 150, 155, 168, 172, 175, 165, 170, 158, 162,
        155, 166, 178, 180, 160, 158, 165, 170, 175, 162, 168, 174, 178, 160, 165
    ]
}

# Create DataFrame
df = pd.DataFrame(data=height_data)

# Set the style and color palette
sns.set(style="whitegrid")
palette = ["#FFA07A", "#20B2AA", "#778899", "#FF6347", "#4682B4"]

# Create the histogram chart
plt.figure(figsize=(10, 12))
sns.histplot(df['height'], kde=False, color="#FF4500", bins=15, binwidth=2)

# Additional styling options
plt.title('Height Distribution Among Participants', fontsize=16)
plt.xlabel('Height (cm)', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.ylim(0, None)

# Save or show the figure
plt.savefig('height_distribution.png')
plt.show()