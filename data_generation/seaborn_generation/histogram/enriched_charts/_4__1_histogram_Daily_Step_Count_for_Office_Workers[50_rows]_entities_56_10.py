
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data points
heights = [
    151, 155, 150, 158, 165, 160, 170, 175, 172, 168, 162, 157, 166, 161, 163, 169, 171, 174, 
    180, 185, 178, 176, 177, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200, 202, 204, 206, 
    208, 210, 212, 214, 216, 218, 220
]

# Create DataFrame
data = pd.DataFrame({'Height': heights})

# Set the style
sns.set(style="whitegrid")

# Create the histogram
plt.figure(figsize=(10, 8))  # Change width and height of the chart
sns.histplot(data['Height'], bins=20, color="#8e44ad", kde=False, binwidth=4)  # Change color and bin width

# Customize the plot with title and labels
plt.title('Height Distribution of Individuals', fontsize=20)  # Change the topic/headline of the chart
plt.xlabel('Frequency', fontsize=15)
plt.ylabel('Height (cm)', fontsize=15)

# Change the direction of the chart
plt.gca().invert_yaxis()

# Display the plot
plt.show()