
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data points
data = {
    'Age Group': ['Young Adult', 'Young Adult', 'Young Adult', 'Middle-aged', 'Middle-aged', 'Middle-aged',
                  'Senior', 'Senior', 'Senior', 'Elderly', 'Elderly', 'Elderly'],
    'Therapy Type': ['Cognitive Behavioral Therapy', 'Mindfulness', 'Group Therapy', 'Cognitive Behavioral Therapy', 
                     'Mindfulness', 'Group Therapy', 'Cognitive Behavioral Therapy', 'Mindfulness', 'Group Therapy', 
                     'Cognitive Behavioral Therapy', 'Mindfulness', 'Group Therapy'],
    'Mental Well-being Score': [85, 88, 80, 78, 82, 75, 70, 73, 68, 65, 68, 62],
    'Participants': [150, 160, 140, 130, 120, 110, 100, 90, 85, 75, 70, 65]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(14, 10))
bubble_plot = sns.scatterplot(data=df, x='Therapy Type', y='Mental Well-being Score', size='Participants',
                              sizes=(100, 1000), hue='Age Group',
                              palette=["#FF6347", "#4682B4", "#3CB371", "#FFD700"])

# Customizing the plot
bubble_plot.set_title('Mental Well-being Scores by Therapy Type and Age Group', pad=20)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
bubble_plot.set_xlabel("Therapy Type")
bubble_plot.set_ylabel("Mental Well-being Score")

# Show the plot
plt.show()