
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data points
data = {
    'Sport': ['Running', 'Running', 'Running', 'Running', 'Swimming', 'Swimming', 'Swimming', 'Swimming',
              'Cycling', 'Cycling', 'Cycling', 'Cycling'],
    'Group': ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D'],
    'Score': [76, 82, 79, 70, 88, 85, 90, 78, 92, 87, 95, 88],
    'Participants': [150, 160, 200, 140, 180, 170, 150, 165, 130, 120, 110, 135]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(14, 10))
bubble_plot = sns.scatterplot(data=df, x='Sport', y='Score', size='Participants',
                              sizes=(100, 1000), hue='Group',
                              palette=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"])

# Customizing the plot
bubble_plot.set_title('Average Scores in Sports by Group with Number of Participants', fontsize=16, pad=20)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
bubble_plot.set_xlabel("Sport")
bubble_plot.set_ylabel("Average Score")

# Show the plot
plt.show()