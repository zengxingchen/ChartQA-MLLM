
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Given dataset in a dictionary
data = {
    'Year': [2015, 2016, 2017, 2018, 2019],
    'Stress Management': [4000, 4200, 4400, 4600, 4800],
    'Mental Health': [6000, 6200, 6400, 6600, 6800],
    'Physical Fitness': [7000, 7200, 7400, 7600, 7800],
    'Nutrition Therapy': [5000, 5100, 5200, 5300, 5400],
    'Sleep Improvement': [3000, 3100, 3200, 3300, 3400]
}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Unpivot the DataFrame from wide to long format
df_long = pd.melt(df, id_vars='Year', var_name='Category', value_name='Amount')

# Create a horizontal bar plot
plt.figure(figsize=(12, 10))
sns.barplot(
    y='Category', 
    x='Amount', 
    hue='Year', 
    data=df_long,
    palette=['#1F77B4', '#FF7F0E', '#2CA02C', '#D62728', '#9467BD'],
    dodge=True,
    edgecolor='.2',
    linewidth=.6,
    orient='h'
)

# Adjusting the bar width (by adjusting the distance between the bars)
plt.yticks(rotation=0)
plt.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left')

# Set the title and the labels of the plot
plt.title('Yearly Health & Psychology Expenditure Comparison', y=1.05)
plt.xlabel('Amount (in USD)')
plt.ylabel('Expenditure Category')

# Show the plot
plt.tight_layout()
plt.show()