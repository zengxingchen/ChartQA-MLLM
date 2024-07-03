
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data points
values = [
    5, 15, 20, 22, 25, 28, 30, 32, 35, 38, 40, 42, 45, 48, 50, 52, 55, 58, 
    60, 62, 65, 68, 70, 72, 75, 78, 80, 82, 85, 88, 90, 92, 95, 98, 100, 
    102, 105, 108, 110, 112, 115, 118, 120, 122, 125, 128, 130, 132, 135, 
    138, 140, 142, 145, 148, 150, 152, 155, 158, 160, 162, 165, 168, 170, 
    172, 175, 178, 180, 182, 185, 188, 190, 192, 195, 198, 200
]

# Create DataFrame
data = pd.DataFrame({'Values': values})

# Set the style
sns.set(style="whitegrid")

# Create the histogram
plt.figure(figsize=(12, 6))  # Change width and height of the chart
sns.histplot(data['Values'], bins=15, color="#4682b4", kde=False, binwidth=10)  # Change color and bin width

# Customize the plot with title and labels
plt.title('Number of Pages Read in a Month', fontsize=20, pad=20)  # Change the topic/headline of the chart
plt.xlabel('Number of Pages', fontsize=15)
plt.ylabel('Frequency', fontsize=15)

# Display the plot
plt.show()