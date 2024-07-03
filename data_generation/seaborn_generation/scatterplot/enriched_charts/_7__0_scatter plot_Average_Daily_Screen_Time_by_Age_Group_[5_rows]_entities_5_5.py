
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data preparation
data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    'AverageCalories': [2200, 2300, 2500, 2100, 2700, 2600, 2800, 2000, 2900, 2400, 2500, 2300, 2200, 2800, 2700, 2900, 2100, 2500, 2400, 2200, 2700, 2800, 2900, 2000, 2600, 2500, 2300, 2200, 2400, 2500, 2600],
    'StepsWalked': [5000, 5500, 7000, 4500, 8000, 7500, 8500, 4000, 9000, 6000, 6500, 5500, 5000, 8500, 8000, 9000, 4500, 7000, 6000, 5000, 8000, 8500, 9000, 4000, 7500, 7000, 5500, 5000, 6000, 6500, 7500]
}

df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(12, 8))
scatterplot = sns.scatterplot(x='AverageCalories', y='StepsWalked', data=df, color='#1E90FF')

# Add a title and adjust aesthetics
scatterplot.set_title('Daily Calorie Intake vs Steps Walked', fontsize=16, pad=20)
scatterplot.set_xlabel('Average Calories', fontsize=12)
scatterplot.set_ylabel('Steps Walked', fontsize=12)

plt.show()