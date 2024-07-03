
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data points
data = {
    'Age Group': ['Young Adult', 'Young Adult', 'Young Adult', 'Middle-aged', 'Middle-aged', 'Middle-aged',
                  'Senior', 'Senior', 'Senior', 'Elderly', 'Elderly', 'Elderly'],
    'Travel Destination': ['Beach Resort', 'Mountain Hike', 'City Tour', 'Beach Resort', 'Mountain Hike', 
                           'City Tour', 'Beach Resort', 'Mountain Hike', 'City Tour', 'Beach Resort', 
                           'Mountain Hike', 'City Tour'],
    'Score': [90, 85, 88, 80, 78, 82, 75, 70, 68, 65, 60, 62],
    'Reviews': [250, 220, 210, 200, 180, 170, 160, 150, 140, 130, 120, 110]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(16, 12))
bubble_plot = sns.scatterplot(data=df, x='Travel Destination', y='Score', size='Reviews',
                              sizes=(100, 1000), hue='Age Group',
                              palette=["#4c72b0", "#55a868", "#c44e52", "#8172b3"])

# Customizing the plot
bubble_plot.set_title('Travel Destination Satisfaction Scores by Age Group with Number of Reviews', pad=20)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
bubble_plot.set_xlabel("Travel Destination")
bubble_plot.set_ylabel("Average Satisfaction Score")

# Show the plot
plt.show()