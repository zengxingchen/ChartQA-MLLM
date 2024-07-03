
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Given dataset in a dictionary
data = {
    'Year': [2015, 2016, 2017, 2018, 2019],
    'Publishing': [5000, 5200, 5400, 5600, 5800],
    'Distribution': [8000, 8200, 8400, 8600, 8800],
    'Editing': [6000, 6200, 6400, 6600, 6800],
    'Marketing': [7000, 7200, 7400, 7600, 7800],
    'Sales': [7500, 7700, 7900, 8100, 8300]
}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Unpivot the DataFrame from wide to long format
df_long = pd.melt(df, id_vars='Year', var_name='Category', value_name='Amount')

# Create a vertical bar plot
plt.figure(figsize=(10, 12))
sns.barplot(
    x='Category', 
    y='Amount', 
    hue='Year', 
    data=df_long,
    palette=['#FF5733', '#33FF57', '#3357FF', '#FF33A7', '#FFC233'],
    dodge=True,
    edgecolor='.2',
    linewidth=.6,
    orient='v'
)

# Adjusting the bar width (by adjusting the distance between the bars)
plt.xticks(rotation=45)
plt.legend(title='Year')

# Set the title and the labels of the plot
plt.title('Yearly Publishing Industry Expenditure Comparison')
plt.xlabel('Expenditure Category')
plt.ylabel('Amount (in USD)')

# Show the plot
plt.show()