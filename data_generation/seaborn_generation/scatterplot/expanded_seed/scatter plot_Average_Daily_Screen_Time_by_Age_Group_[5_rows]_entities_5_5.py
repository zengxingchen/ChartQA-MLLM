
import seaborn as sns
import matplotlib.pyplot as plt

# Data provided
data = [
    {'Age Group': '16-24', 'Hours': 3.8},
    {'Age Group': '25-34', 'Hours': 3.6},
    {'Age Group': '35-44', 'Hours': 3.1},
    {'Age Group': '45-54', 'Hours': 2.8},
    {'Age Group': '55-64', 'Hours': 2.5}
]

# Create a DataFrame from the data
import pandas as pd
df = pd.DataFrame(data)

# In order to use seaborn's scatterplot with a categorical variable like "Age Group",
# we need to assign actual numeric values to the categories. We'll map each age group
# to a numeric value using the order in which they appear.
age_group_mapping = {age_group: index for index, age_group in enumerate(df['Age Group'].unique())}
df['Age Group Value'] = df['Age Group'].map(age_group_mapping)

# Now we'll plot using these numeric values.
plt.figure(figsize=(10, 6))
scatter = sns.scatterplot(
    x='Age Group Value',
    y='Hours',
    hue='Age Group',  # Color by Age Group
    size='Hours',     # Vary size by Hours
    sizes=(100, 400),  # Control range of sizes to make differences visible
    data=df,
    palette='viridis', # Use a nice color palette
    legend='full'      # Show legend in full
)

# Adjust the ticks on the x-axis to show the age group labels instead of numbers
scatter.set_xticks(range(len(age_group_mapping)))
scatter.set_xticklabels(age_group_mapping.keys())

# Set the axis labels appropriately
plt.xlabel('Age Group')
plt.ylabel('Hours Spent')
plt.title('Hours Spent by Age Group')

# Display the legend
plt.legend(title='Age Group')

# Show the plot
plt.show()