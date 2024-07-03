
import seaborn as sns
import matplotlib.pyplot as plt

# Data: Age distribution
age_data = [24, 36, 42, 18, 29, 34, 56, 71, 23, 39, 47, 58, 65, 73, 20, 33, 37,
            44, 50, 62, 24, 48, 55, 61, 69, 26, 38, 49, 53, 60, 25, 41, 45, 57,
            63, 27, 31, 40, 52, 66, 28, 35, 43, 51, 64, 30, 32, 46, 54, 67, 70,
            59, 68, 74, 75, 21, 22, 19]

# Set the size of the chart
plt.figure(figsize=(12, 6))

# Create a histogram with horizontal orientation
sns.histplot(data=age_data, kde=False, color="#3498db", binwidth=5, orientation='horizontal')

# Set chart title and labels
plt.title('Age Distribution of a Population')
plt.xlabel('Frequency')
plt.ylabel('Age')

# Show the plot
plt.show()