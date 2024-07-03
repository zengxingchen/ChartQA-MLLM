
import seaborn as sns
import matplotlib.pyplot as plt

# Data points for scores of participants
scores = [
    55, 70, 65, 85, 90, 95, 60, 50, 75, 80, 90, 85, 70, 75, 60, 65, 95, 80, 90, 85,
    70, 75, 65, 60, 55, 85, 75, 70, 95, 80, 65, 50, 55, 90, 85, 80, 75, 70, 65, 60,
    55, 50, 75, 85, 95, 80, 70, 65, 60, 55, 75, 85, 90, 95, 80, 70, 65, 60, 55, 50,
    85, 90, 80, 75, 70, 65, 55, 60, 85, 90, 75, 80, 70, 60, 55, 50, 85, 90, 80, 75,
    70, 65, 60, 55, 50, 85, 95, 80, 75, 70, 65
]

# Setting the size of the chart
plt.figure(figsize=(10, 6))

# Creating a vertical histogram with modified bin width and color scheme
sns.histplot(scores, bins=15, color="#FF5733", binwidth=5, orientation='vertical')

# Customizing the chart's appearance
plt.title('Distribution of Scores among Participants')
plt.xlabel('Scores')
plt.ylabel('Frequency')

# Display the histogram
plt.show()