
import seaborn as sns
import matplotlib.pyplot as plt

# Given data in a list
salaries = [40, 55, 60, 45, 50, 47, 52, 61, 58, 65, 49, 57, 62, 54, 63, 48, 51, 44, 43, 46, 59, 55,
            50, 53, 66, 64, 56, 68, 70, 72, 74, 60, 67, 69, 71, 73, 75, 76, 78, 77, 79, 80, 81, 82,
            84, 83, 85, 86, 87, 88, 89, 90, 92, 91, 93, 94, 95, 96, 97, 98, 99, 100]

# Create the seaborn histogram
sns.set()  # Use seaborn's default settings
plt.figure(figsize=(12, 8))  # Change width and height of the chart

# Create the histogram with modified aesthetics
ax = sns.histplot(salaries,
                  color="#3498db",  # Set specific color code
                  binwidth=5,       # Set the width (height for vertical) of the bins
                  orientation='horizontal')  # Change the direction of the chart

# Customize the chart
ax.set_title("Annual Salaries Distribution in Finance Sector", pad=20)  # Set a title
ax.set_ylabel("Annual Salaries (in Thousands USD)")  # Set the y-axis label
ax.set_xlabel("Count")  # Set the x-axis label

# Display the plot
plt.show()