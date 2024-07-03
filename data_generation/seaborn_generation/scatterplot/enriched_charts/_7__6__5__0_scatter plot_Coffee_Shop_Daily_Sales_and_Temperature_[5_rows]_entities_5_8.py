
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from the provided table data
data = {
    'FruitID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
    'AverageDailyFruitIntake': [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20, 20.5],
    'VitaminLevels': [50, 55, 60, 65, 70, 75, 80, 78, 85, 90, 92, 95, 97, 100, 102, 105, 108, 110, 112, 115, 118, 120, 122, 125, 127, 130, 132, 135, 138, 140, 142, 145, 148, 150, 152, 155, 158, 160, 162, 165]
}
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_theme(style="whitegrid")

# Create the scatter plot
plt.figure(figsize=(14, 8))
scatter_plot = sns.scatterplot(x='AverageDailyFruitIntake', y='VitaminLevels', data=df, color='#2ca02c', s=100)

# Set the chart title and labels
scatter_plot.set_title('Relationship Between Daily Fruit Consumption and Vitamin Levels', fontsize=18, y=1.05)
scatter_plot.set_xlabel('Average Daily Fruit Intake (servings)', fontsize=14)
scatter_plot.set_ylabel('Vitamin Levels (mg/dL)', fontsize=14)

# Show the plot
plt.show()