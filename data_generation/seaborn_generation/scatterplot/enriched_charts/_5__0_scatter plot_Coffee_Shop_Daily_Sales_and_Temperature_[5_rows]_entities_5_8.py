
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from the provided table data
data = {
    'StudentID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],
    'DailyCaloriesConsumed': [1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900],
    'WeightLoss': [2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 6.7, 7.3, 8.1, 8.8, 9.2, 10.3]
}
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_theme(style="whitegrid")

# Create the scatter plot
plt.figure(figsize=(14, 8))
scatter_plot = sns.scatterplot(x='DailyCaloriesConsumed', y='WeightLoss',
                               data=df, color='#e377c2', s=70)

# Set the chart title and labels
scatter_plot.set_title('Relationship Between Daily Calorie Intake and Weight Loss', fontsize=16)
scatter_plot.set_xlabel('Daily Calories Consumed', fontsize=14)
scatter_plot.set_ylabel('Weight Loss (kg)', fontsize=14)

# Show the plot
plt.show()