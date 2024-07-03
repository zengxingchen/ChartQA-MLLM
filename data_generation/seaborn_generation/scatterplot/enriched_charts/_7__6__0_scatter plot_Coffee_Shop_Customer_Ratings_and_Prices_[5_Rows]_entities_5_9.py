
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data from the table provided above
data = {
    'Age': [10, 10, 10, 10, 12, 12, 12, 12, 14, 14, 14, 14, 16, 16, 16, 16, 18, 18, 18, 18, 20, 20, 20, 20, 22, 22, 22, 22, 24, 24, 24, 24],
    'Internet_Usage': [5, 6, 4, 7, 10, 8, 9, 11, 14, 12, 13, 15, 18, 16, 19, 17, 20, 21, 22, 23, 25, 26, 24, 27, 28, 29, 30, 31, 32, 33, 34, 35],
    'Calories_Burned': [120, 125, 110, 130, 180, 170, 175, 185, 200, 195, 198, 210, 250, 240, 255, 245, 300, 310, 320, 330, 340, 350, 335, 355, 360, 365, 370, 375, 380, 385, 390, 395]
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Create the scatterplot
plt.figure(figsize=(16, 12))
scatter_plot = sns.scatterplot(x='Internet_Usage', y='Calories_Burned', hue='Age', palette=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'], data=df)

# Customizing the scatterplot
scatter_plot.set_title('Internet Usage vs Calories Burned Among Different Age Groups in Health & Psychology')
scatter_plot.set_xlabel('Average Weekly Internet Usage (hours)')
scatter_plot.set_ylabel('Average Calories Burned (per week)')

plt.legend(title='Age Group')
plt.show()