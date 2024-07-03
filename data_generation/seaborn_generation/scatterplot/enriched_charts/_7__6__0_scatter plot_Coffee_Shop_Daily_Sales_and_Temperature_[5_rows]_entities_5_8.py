
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from the provided table data
data = {
    'SleepHours': [5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 5, 6, 7, 8, 9, 5, 6, 7, 8, 9, 10],
    'CognitivePerformanceScore': [50, 52, 55, 58, 62, 65, 68, 70, 72, 75, 78, 55, 58, 60, 65, 70, 53, 57, 61, 66, 74, 77]
}
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_theme(style="whitegrid")

# Create the scatter plot
plt.figure(figsize=(16, 9))
scatter_plot = sns.scatterplot(x='SleepHours', y='CognitivePerformanceScore',
                               data=df, color='#1f77b4', s=100)

# Set the chart title and labels
scatter_plot.set_title('Impact of Sleep Hours on Cognitive Performance', fontsize=20, pad=20)
scatter_plot.set_xlabel('Sleep Hours', fontsize=14)
scatter_plot.set_ylabel('Cognitive Performance Score', fontsize=14)

# Show the plot
plt.show()