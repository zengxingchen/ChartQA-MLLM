
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from the provided table data
data = {
    'ExerciseHours': [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 3, 5, 6.5, 7.5, 9],
    'HappinessScore': [45, 50, 55, 60, 63, 65, 68, 70, 72, 75, 77, 80, 82, 84, 86, 88, 90, 92, 94, 96, 67, 76, 81, 85, 93]
}
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_theme(style="whitegrid")

# Create the scatter plot
plt.figure(figsize=(14, 7))
scatter_plot = sns.scatterplot(x='ExerciseHours', y='HappinessScore',
                               data=df, color='#ff5733', s=70)

# Set the chart title and labels
scatter_plot.set_title('Impact of Daily Exercise on Happiness Scores', fontsize=18, pad=20)
scatter_plot.set_xlabel('Daily Exercise Hours', fontsize=14)
scatter_plot.set_ylabel('Happiness Score', fontsize=14)

# Show the plot
plt.show()