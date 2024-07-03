
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data points
ages = [
    23, 27, 21, 34, 45, 55, 43, 38, 41, 29, 26, 48, 40, 31, 33, 36, 37, 58, 60, 42, 39, 35,
    49, 52, 24, 28, 22, 30, 32, 25, 56, 57, 53, 54, 50, 51, 47, 46, 44, 20, 19, 18, 17,
    16, 15, 14, 13, 12, 11, 10, 59, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72,
    73, 74, 75, 76, 77, 78, 
    # Add more data points, if needed, to reach the required number
]

# Create DataFrame
data = pd.DataFrame({'Age': ages})

# Set the style
sns.set(style="whitegrid")

# Create the histogram
plt.figure(figsize=(12, 6))  # Change width and height of the chart
sns.histplot(data['Age'], bins=30, color="#3498db", kde=False, binwidth=2.5)  # Change color and bin width

# Customize the plot with title and labels
plt.title('Age Distribution of Individuals', fontsize=20)  # Change the topic/headline of the chart
plt.xlabel('Age', fontsize=15)
plt.ylabel('Frequency', fontsize=15)

# Display the plot
plt.show()