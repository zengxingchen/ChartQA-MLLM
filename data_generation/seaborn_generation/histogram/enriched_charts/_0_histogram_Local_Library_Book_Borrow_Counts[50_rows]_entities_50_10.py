
import seaborn as sns
import matplotlib.pyplot as plt

# Given data in a list
ages = [24, 55, 62, 45, 33, 23, 37, 41, 29, 58, 31, 60, 50, 44, 28, 34, 22, 39, 48, 56, 68, 47,
        23, 34, 35, 40, 26, 27, 31, 32, 39, 24, 46, 42, 43, 51, 30, 36, 38, 49, 52, 53, 57, 59,
        61, 63, 25, 29, 33, 35, 27]

# Create the seaborn histogram
sns.set()  # Use seaborn's default settings
plt.figure(figsize=(8, 6))  # Change width and height of the chart

# Create the histogram with modified aesthetics
ax = sns.histplot(ages,
                  color="#3498db",  # Set specific color code
                  binwidth=5,       # Set the width (height for vertical) of the bins
                  bins=20,          # Could set explicit number of bins
                  orientation='horizontal')  # Change the direction of the chart

# Customize the chart
ax.set_title("Population Ages in a Small City")  # Set a title
ax.set_xlabel("Count")  # Set the x-axis label (y-axis when vertical)
ax.set_ylabel("Age")    # Set the y-axis label (x-axis when vertical)

# Display the plot
plt.show()