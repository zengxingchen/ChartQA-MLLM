
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Week': 1, 'Espresso': 180, 'Latte': 210, 'Cappuccino': 170, 'American Coffee': 140, 'Iced Coffee': 120},
    {'Week': 2, 'Espresso': 185, 'Latte': 205, 'Cappuccino': 180, 'American Coffee': 145, 'Iced Coffee': 130},
    # ... Add all other weeks data here
    {'Week': 14, 'Espresso': 245, 'Latte': 265, 'Cappuccino': 230, 'American Coffee': 205, 'Iced Coffee': 215}
]

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data)

# Reshape dataframe for seaborn compatibility
df_melted = df.melt(id_vars='Week', var_name='Coffee Type', value_name='Sales')

# Create the area plot
plt.figure(figsize=(12, 7))
sns.set_style("whitegrid")

# Plot each coffee type individually to enable the use of a gradient
for coffee_type in df_melted['Coffee Type'].unique():
    sns.lineplot(
        x='Week',
        y='Sales',
        hue='Coffee Type',
        data=df_melted[df_melted['Coffee Type'] == coffee_type],
        palette=sns.cubehelix_palette(start=.5, rot=-.5, as_cmap=True)
    )

# Fill the area under the lineplots
weeks = df['Week']
for i, coffee_type in enumerate(df.columns[1:]):
    plt.fill_between(weeks, df[coffee_type], label=coffee_type, alpha=0.5, step='pre')

# Showing the legend
plt.legend(title='Coffee Type')

# Additional styling and labels
plt.title('Weekly Coffee Sales Data')
plt.xlabel('Week')
plt.ylabel('Number of Sales')
sns.despine()

# Display the plot
plt.show()