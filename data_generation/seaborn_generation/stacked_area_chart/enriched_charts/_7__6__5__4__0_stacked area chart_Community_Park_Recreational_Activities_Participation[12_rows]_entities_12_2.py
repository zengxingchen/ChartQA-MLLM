
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data in a Pandas DataFrame
data = pd.DataFrame({
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Gym_A': [450, 460, 470, 480, 490, 500, 
              510, 520, 530, 540, 550, 560],
    'Gym_B': [500, 510, 520, 530, 540, 550,
              560, 570, 580, 590, 600, 610],
    'Gym_C': [550, 560, 570, 580, 590, 600,
              610, 620, 630, 640, 650, 660]
})

# Transform data for stacked area plot
data = data.set_index('Month')
data.index = pd.CategoricalIndex(data.index, 
                                 categories=['January', 'February', 'March', 'April', 'May', 'June',
                                             'July', 'August', 'September', 'October', 'November', 'December'], 
                                 ordered=True)
data = data.sort_index()

# Stacked area plot
plt.figure(figsize=(18, 8))
sns.set_style("whitegrid")

# Define colors for each category
colors = ["#3498db", "#e74c3c", "#2ecc71"]

# Generating the stacked areas
plt.stackplot(data.index, data['Gym_A'], data['Gym_B'], data['Gym_C'], labels=['Gym A', 'Gym B', 'Gym C'], colors=colors)

# Aesthetics
plt.title('Monthly Gym Attendance - 2021', fontsize=22, pad=30)
plt.ylabel('Attendance', fontsize=16)
plt.xlabel('Month', fontsize=16)
plt.xticks(rotation=45)
plt.legend(loc='upper left')

# Annotating a specific data point
plt.text('December', 660, 'Peak for Gym C', horizontalalignment='center', color='black')

# Show plot
sns.despine()
plt.show()