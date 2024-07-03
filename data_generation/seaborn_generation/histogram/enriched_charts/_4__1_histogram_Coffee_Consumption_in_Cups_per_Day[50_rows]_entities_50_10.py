
import seaborn as sns
import matplotlib.pyplot as plt

# Data points
countries_visited = [
    2, 3, 1, 4, 5, 8, 9, 7, 6, 3, 2, 4, 5, 6, 8, 9, 10, 11, 12, 15,
    7, 8, 10, 11, 3, 4, 2, 1, 5, 6, 7, 9, 12, 13, 14, 16, 18, 20, 21,
    3, 4, 6, 8, 9, 10, 12, 13, 15, 17, 19, 20, 21, 22, 3, 5, 7, 9, 11,
    4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 5, 7, 9, 11, 13, 15, 17, 19, 21
]

# Setting the size of the chart
plt.figure(figsize=(12, 8))

# Creating a histogram with modified bin width and color scheme
sns.histplot(countries_visited, bins=12, color="#FF5733", binwidth=1, orientation='horizontal')

# Customizing the chart's appearance
plt.title('Number of Countries Visited by Survey Participants', pad=20)
plt.xlabel('Frequency')
plt.ylabel('Number of Countries Visited')

# Display the histogram
plt.show()