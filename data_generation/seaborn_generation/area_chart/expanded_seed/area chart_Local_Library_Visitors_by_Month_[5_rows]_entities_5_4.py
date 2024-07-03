
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Given chart table data
data = [
    {'Month': 'January', 'Visitors': 4500},
    {'Month': 'February', 'Visitors': 3750},
    {'Month': 'March', 'Visitors': 5200},
    {'Month': 'April', 'Visitors': 4800},
    {'Month': 'May', 'Visitors': 5000}
]

# Convert the chart table data into a DataFrame
df = pd.DataFrame(data)

# Convert 'Month' to a categorical type to maintain the month order
df['Month'] = pd.Categorical(df['Month'], categories=[
    'January', 'February', 'March', 'April', 'May'],
    ordered=True)

# Sort the data by Month
df.sort_values('Month', inplace=True)

# Set the style and context of the seaborn plots
sns.set_style("whitegrid")
sns.set_context("talk")

# Create the area plot
plt.figure(figsize=(10, 6))
area_plot = sns.lineplot(data=df, x='Month', y='Visitors', marker='o', size=10)

# Fill the area under the line
plt.fill_between(df['Month'], df['Visitors'], alpha=0.2)

# Customize the axes and layout
plt.title('Monthly Visitors', fontsize=20)
plt.xlabel('Month', fontsize=15)
plt.ylabel('Number of Visitors', fontsize=15)
plt.xticks(rotation=45)

# Display the plot
plt.tight_layout()
plt.show()