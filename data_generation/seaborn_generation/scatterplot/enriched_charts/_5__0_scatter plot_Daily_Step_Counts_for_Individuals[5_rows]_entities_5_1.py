
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data into a pandas DataFrame
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday',
            'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'CaloriesBurned': [300, 350, 400, 380, 450, 480, 500, 320, 410, 460, 430, 490, 530, 550],
    'Steps': [7000, 7500, 8000, 8200, 9000, 10000, 10500, 7200, 8300, 8800, 8600, 9300, 11000, 11500]
}

df = pd.DataFrame(data)

# Set the style
sns.set(style="whitegrid")

# Create the scatterplot
plt.figure(figsize=(12, 8))
scatter_plot = sns.scatterplot(x='CaloriesBurned', y='Steps',
                               data=df, color="#E74C3C", s=60)

# Customize the axes and title
scatter_plot.set_title('Daily Calories Burned vs. Steps Taken', fontsize=18)
scatter_plot.set_xlabel('Calories Burned', fontsize=14)
scatter_plot.set_ylabel('Steps Taken', fontsize=14)

# Show the plot
plt.show()