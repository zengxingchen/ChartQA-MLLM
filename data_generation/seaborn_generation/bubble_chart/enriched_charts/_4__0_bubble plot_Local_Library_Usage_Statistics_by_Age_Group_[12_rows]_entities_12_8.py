
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data points
data = {
    'Age Group': ['Young Adult', 'Young Adult', 'Young Adult', 'Middle-aged', 'Middle-aged', 'Middle-aged',
                  'Senior', 'Senior', 'Senior', 'Elderly', 'Elderly', 'Elderly'],
    'Health Metric': ['Cardio Health', 'Mental Well-being', 'Physical Fitness', 'Cardio Health', 'Mental Well-being', 
                      'Physical Fitness', 'Cardio Health', 'Mental Well-being', 'Physical Fitness', 'Cardio Health', 
                      'Mental Well-being', 'Physical Fitness'],
    'Score': [78, 85, 88, 82, 88, 80, 70, 75, 65, 68, 70, 60],
    'Participants': [200, 220, 210, 180, 190, 170, 160, 150, 140, 130, 120, 110]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(14, 10))
bubble_plot = sns.scatterplot(data=df, x='Health Metric', y='Score', size='Participants',
                              sizes=(100, 1000), hue='Age Group',
                              palette=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"])

# Customizing the plot
bubble_plot.set_title('Health Metrics Scores by Age Group with Number of Participants', pad=20)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
bubble_plot.set_xlabel("Health Metric")
bubble_plot.set_ylabel("Average Score")

# Show the plot
plt.show()