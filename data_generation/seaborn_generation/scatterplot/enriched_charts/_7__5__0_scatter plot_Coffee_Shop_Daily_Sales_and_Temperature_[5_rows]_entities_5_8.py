
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from the provided table data
data = {
    'PersonID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'DailyExpenses': [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340],
    'Savings': [500, 480, 460, 440, 420, 400, 380, 360, 340, 320, 300, 280, 260, 240, 220, 200, 180, 160, 140, 120, 100, 80, 60, 40, 20, 0, -20, -40, -60, -80]
}
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_theme(style="whitegrid")

# Create the scatter plot
plt.figure(figsize=(16, 9))
scatter_plot = sns.scatterplot(x='DailyExpenses', y='Savings',
                               data=df, color='#1f77b4', s=70)

# Set the chart title and labels
scatter_plot.set_title('Relationship Between Daily Expenses and Savings', fontsize=16, pad=20)
scatter_plot.set_xlabel('Daily Expenses ($)', fontsize=14)
scatter_plot.set_ylabel('Savings ($)', fontsize=14)

# Show the plot
plt.show()