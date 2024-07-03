
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Given data
data = [
    {'Year': 2017, 'Number of Commuters (in thousands)': 120},
    {'Year': 2018, 'Number of Commuters (in thousands)': 135},
    {'Year': 2019, 'Number of Commuters (in thousands)': 150},
    {'Year': 2020, 'Number of Commuters (in thousands)': 80}
]

# Convert the dictionary list to a DataFrame
df = pd.DataFrame(data)

# Create the line plot using Seaborn
sns.set_theme(style="whitegrid")

# Define the area chart
fig, ax = plt.subplots()
sns.lineplot(
    data=df,
    x='Year',
    y='Number of Commuters (in thousands)',
    ax=ax,
    color="royalblue",
    marker="o"
)

# Fill the area under the plot
plt.fill_between(
    x=df['Year'],
    y1=df['Number of Commuters (in thousands)'],
    color="lightblue"
)

# Customize the visualization
ax.set_title('Number of Commuters Over Years', fontsize=16)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Number of Commuters (in thousands)', fontsize=12)
sns.despine(fig) # Removes the top and right spines

# Show the plot
plt.show()