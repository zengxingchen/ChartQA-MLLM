
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data preparation
data = {
    'Sport': ['Basketball', 'Soccer', 'Tennis', 'Swimming', 'Running', 'Cycling', 'Boxing', 'Gymnastics', 'Skiing', 'Baseball', 'Hockey', 'Rowing', 'Volleyball', 'Rugby', 'Golf'],
    'Average_Score': [85, 78, 90, 82, 88, 74, 81, 87, 79, 83, 77, 86, 80, 76, 84]
}

df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(10, 14))
sns.barplot(x='Average_Score', y='Sport', data=df, palette=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf", "#9edae5", "#ffbb78", "#98df8a", "#ff9896", "#c5b0d5"], linewidth=0.8)

# Customize the chart
plt.title('Average Scores by Sport', fontsize=16, pad=20)
plt.xlabel('Average Score', fontsize=14)
plt.ylabel('Sport', fontsize=14)
plt.grid(axis='x')

# Show the plot
plt.show()