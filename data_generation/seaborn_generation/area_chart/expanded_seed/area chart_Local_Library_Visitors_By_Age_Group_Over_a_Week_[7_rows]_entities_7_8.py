
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Given data
data = [
    {'Age Group': '0-12', 'Visitors': 95},
    {'Age Group': '13-18', 'Visitors': 78},
    {'Age Group': '19-25', 'Visitors': 110},
    {'Age Group': '26-35', 'Visitors': 123},
    {'Age Group': '36-50', 'Visitors': 88},
    {'Age Group': '51-65', 'Visitors': 76},
    {'Age Group': '65+', 'Visitors': 52}
]

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Cast the 'Age Group' as a categorical type with the defined order
age_order = ['0-12', '13-18', '19-25', '26-35', '36-50', '51-65', '65+']
df['Age Group'] = pd.Categorical(df['Age Group'], categories=age_order, ordered=True)

# Sort DataFrame according to the 'Age Group' category order
df = df.sort_values('Age Group')

# Set the style and context of the Seaborn plot for better aesthetics
sns.set_style('whitegrid')
sns.set_context('talk')

# Initialize the matplotlib figure
fig, ax = plt.subplots(figsize=(12, 6))

# Create a lineplot and capture the line to get data for fill_between
line = sns.lineplot(x='Age Group', y='Visitors', data=df, sort=False, ax=ax)

# Fill the area under the lineplot
plt.fill_between(x=df['Age Group'], y1=df['Visitors'], alpha=0.3)

# Customize the plot with titles, labels, etc.
plt.title('Visitors by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Number of Visitors')

# Show the final plot
plt.show()