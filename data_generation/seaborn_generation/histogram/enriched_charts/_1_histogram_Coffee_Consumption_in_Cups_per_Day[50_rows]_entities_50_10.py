
import seaborn as sns
import matplotlib.pyplot as plt

# Data points (repeated according to the number of appearances in the table above)
ages = [
    24, 29, 21, 22, 35, 39, 42, 43, 19, 20, 28, 37, 31, 33, 26, 23, 27, 41, 45, 38,
    36, 24, 25, 30, 34, 32, 40, 44, 18, 46, 47, 21, 29, 22, 35, 39, 43, 19, 20, 28,
    31, 33, 26, 23, 27, 41, 45, 38, 36, 25, 30, 34, 32, 40, 44, 18, 46, 47, 22, 35,
    39, 43, 19, 20, 28, 31, 33, 26, 23, 27, 41, 45, 38, 36, 25, 30, 34, 32, 40, 44,
    18, 46, 47
]

# Setting the size of the chart
plt.figure(figsize=(10, 6))

# Creating a histogram with modified bin width and color scheme
sns.histplot(ages, bins=15, color="#3498DB", binwidth=2)

# Customizing the chart's appearance
plt.title('Age Distribution of Survey Participants')
plt.xlabel('Age')
plt.ylabel('Frequency')

# Display the histogram
plt.show()