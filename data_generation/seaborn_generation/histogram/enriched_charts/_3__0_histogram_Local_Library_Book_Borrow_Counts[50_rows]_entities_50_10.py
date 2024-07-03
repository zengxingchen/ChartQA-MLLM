
import seaborn as sns
import matplotlib.pyplot as plt

# Given data in a list
ages = [25, 55, 65, 45, 34, 23, 39, 41, 30, 58, 31, 63, 50, 44, 28, 35, 22, 40, 48, 57, 68, 47,
        23, 36, 35, 40, 26, 27, 32, 33, 39, 25, 46, 42, 43, 51, 30, 38, 37, 49, 52, 54, 59, 61,
        62, 64, 25, 29, 33, 35, 27]

# Create the seaborn histogram
sns.set()  # Use seaborn's default settings
plt.figure(figsize=(10, 7))  # Change width and height of the chart

# Create the histogram with modified aesthetics
ax = sns.histplot(ages,
                  color="#e74c3c",  # Set specific color code
                  binwidth=4,       # Set the width (height for vertical) of the bins
                  orientation='vertical')  # Change the direction of the chart

# Customize the chart
ax.set_title("Age Distribution in Sports & Fitness Club", pad=20)  # Set a title
ax.set_xlabel("Age")  # Set the x-axis label
ax.set_ylabel("Count")    # Set the y-axis label

# Display the plot
plt.show()