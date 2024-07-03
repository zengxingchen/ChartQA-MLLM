
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from the provided table data
data = {
    'StudentID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
    'MinutesMeditated': [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205],
    'StressLevel': [60, 58, 57, 55, 54, 52, 50, 49, 47, 45, 44, 42, 40, 39, 37, 36, 34, 33, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]
}
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_theme(style="whitegrid")

# Create the scatter plot
plt.figure(figsize=(14, 7))
scatter_plot = sns.scatterplot(x='MinutesMeditated', y='StressLevel',
                               data=df, color='#ff7f0e', s=60)

# Set the chart title and labels
scatter_plot.set_title('Impact of Meditation on Stress Levels', fontsize=16, pad=20)
scatter_plot.set_xlabel('Minutes Meditated', fontsize=14)
scatter_plot.set_ylabel('Stress Level', fontsize=14)

# Show the plot
plt.show()