
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data points
data = {
    'Age Group': ['Young Adult', 'Young Adult', 'Young Adult', 'Middle-aged', 'Middle-aged', 'Middle-aged',
                  'Senior', 'Senior', 'Senior', 'Elderly', 'Elderly', 'Elderly'],
    'Activity Type': ['Adventure Sports', 'Cultural Tours', 'Beach Leisure', 'Adventure Sports', 'Cultural Tours', 
                      'Beach Leisure', 'Adventure Sports', 'Cultural Tours', 'Beach Leisure', 'Adventure Sports', 
                      'Cultural Tours', 'Beach Leisure'],
    'Satisfaction Score': [90, 85, 88, 75, 82, 80, 65, 70, 68, 60, 62, 58],
    'Participants': [180, 200, 190, 170, 160, 150, 140, 130, 120, 110, 100, 90]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(16, 12))
bubble_plot = sns.scatterplot(data=df, x='Activity Type', y='Satisfaction Score', size='Participants',
                              sizes=(100, 1000), hue='Age Group',
                              palette=["#ff5733", "#33ff57", "#3357ff", "#ff33a8"])

# Customizing the plot
bubble_plot.set_title('Tourist Satisfaction Scores by Activity Type and Age Group', pad=20)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
bubble_plot.set_xlabel("Activity Type")
bubble_plot.set_ylabel("Satisfaction Score")

# Show the plot
plt.show()