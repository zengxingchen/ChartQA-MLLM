
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data points
data = {
    'Group': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'D', 'D', 'D'],
    'Skill': ['Math', 'Science', 'Language', 'Math', 'Science', 'Language',
              'Math', 'Science', 'Language', 'Math', 'Science', 'Language'],
    'Score': [88, 92, 85, 83, 87, 90, 95, 90, 92, 78, 85, 88],
    'Individuals': [150, 180, 130, 160, 170, 120, 200, 150, 110, 140, 165, 135]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(12, 8))
bubble_plot = sns.scatterplot(data=df, x='Skill', y='Score', size='Individuals',
                              sizes=(100, 1000), hue='Group',
                              palette=["#3498db", "#e74c3c", "#2ecc71", "#f1c40f"])

# Customizing the plot
bubble_plot.set_title('Average Skills Scores by Group with Number of Individuals')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
bubble_plot.set_xlabel("Skill")
bubble_plot.set_ylabel("Average Score")

# Show the plot
plt.show()