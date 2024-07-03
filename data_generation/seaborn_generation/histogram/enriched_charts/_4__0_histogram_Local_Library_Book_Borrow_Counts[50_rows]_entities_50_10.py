
import seaborn as sns
import matplotlib.pyplot as plt

# Given data in a list
stress_levels = [15, 22, 33, 45, 18, 27, 35, 40, 23, 38, 28, 37, 32, 30, 25, 43, 41, 34, 26, 29, 24, 
                 19, 21, 39, 31, 44, 20, 17, 36, 42, 16, 23, 22, 33, 34, 32, 29, 26, 25, 38]

# Create the seaborn histogram
sns.set()  # Use seaborn's default settings
plt.figure(figsize=(10, 7))  # Change width and height of the chart

# Create the histogram with modified aesthetics
ax = sns.histplot(stress_levels,
                  color="#FF5733",  # Set specific color code
                  binwidth=3,       # Set the width of the bins
                  bins=15,          # Could set explicit number of bins
                  orientation='vertical')  # Change the direction of the chart

# Customize the chart
ax.set_title("Stress Levels in a Workplace")  # Set a title
ax.set_xlabel("Stress Level")  # Set the x-axis label
ax.set_ylabel("Count")    # Set the y-axis label

# Display the plot
plt.show()