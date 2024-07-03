
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Given data
data = [
    {'Year': 2018, 'Bicycles': 120, 'Personal Cars': 930, 'Public Transit': 785, 'Taxis': 65, 'Ride-Sharing': 110},
    {'Year': 2019, 'Bicycles': 125, 'Personal Cars': 895, 'Public Transit': 790, 'Taxis': 70, 'Ride-Sharing': 130},
    {'Year': 2020, 'Bicycles': 150, 'Personal Cars': 700, 'Public Transit': 800, 'Taxis': 50, 'Ride-Sharing': 200},
    {'Year': 2021, 'Bicycles': 160, 'Personal Cars': 650, 'Public Transit': 850, 'Taxis': 45, 'Ride-Sharing': 220},
    {'Year': 2022, 'Bicycles': 170, 'Personal Cars': 620, 'Public Transit': 890, 'Taxis': 40, 'Ride-Sharing': 240}
]

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Setting the style of Seaborn
sns.set_theme(style="whitegrid")

# Prepare data for stacking
x = df['Year'].values
columns = df.columns[1:]
y = [df[column].values for column in columns]

# Create the figure and the axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create the stacked area chart
ax.stackplot(x, y, labels=columns, alpha=0.8)

# Customize the legend
ax.legend(loc='upper left')

# Add titles and labels
ax.set_title('Transportation Usage Over 5 Years', fontsize=16)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of Users', fontsize=14)

# Improve the x-axis with the desired Year format and limits
plt.xticks(x)
plt.xlim(x.min(), x.max())

# Remove the top and right axes spines, which are not needed
sns.despine(left=True, bottom=True)

# Display the plot
plt.show()