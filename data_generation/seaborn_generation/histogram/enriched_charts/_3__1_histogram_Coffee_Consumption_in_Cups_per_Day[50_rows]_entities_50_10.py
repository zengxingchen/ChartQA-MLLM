
import seaborn as sns
import matplotlib.pyplot as plt

# Data points for the number of trips taken per year by participants
trips = [
    2, 3, 5, 1, 4, 6, 7, 5, 3, 2, 4, 3, 6, 8, 9, 4, 5, 6, 7, 8, 10, 3, 2, 4, 6, 8, 7, 5, 4, 9, 11,
    2, 3, 1, 5, 7, 8, 9, 4, 3, 5, 6, 8, 7, 2, 3, 4, 6, 7, 8, 9, 10, 3, 2, 4, 6, 7, 8, 9, 11, 2, 1, 
    5, 7, 8, 6, 3, 2, 4, 5, 6, 8, 7, 9, 3, 2, 1, 4, 6, 7, 8, 10, 9, 11, 5, 4, 3, 2, 1
]

# Setting the size of the chart
plt.figure(figsize=(12, 8))

# Creating a horizontal histogram with modified bin width and color scheme
sns.histplot(trips, bins=10, color="#1ABC9C", binwidth=1, orientation='horizontal')

# Customizing the chart's appearance
plt.title('Number of Trips Taken per Year by Participants')
plt.xlabel('Frequency')
plt.ylabel('Number of Trips')

# Display the histogram
plt.show()