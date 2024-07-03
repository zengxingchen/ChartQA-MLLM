
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Given chart data
chart_data = [
    {'Time': '8 AM', ' Sales ($)': 120},
    {'Time': '9 AM', ' Sales ($)': 235},
    {'Time': '10 AM', ' Sales ($)': 190},
    {'Time': '11 AM', ' Sales ($)': 150},
    {'Time': '12 PM', ' Sales ($)': 165}
]

# Convert to pandas DataFrame
df = pd.DataFrame(chart_data)

# Rename columns to remove leading spaces and standardize
df.columns = ['Time', 'Sales']

# Convert 'Time' to a categorical type so that it maintains order in the plot
df['Time'] = pd.Categorical(df['Time'], categories=[
    '8 AM', '9 AM', '10 AM', '11 AM', '12 PM'], ordered=True)

# Plot the area chart using seaborn lineplot and matplotlib fill_between
sns.set_theme(style="whitegrid")

# Create the lineplot
ax = sns.lineplot(x='Time', y='Sales', data=df, sort=False)

# Fill the area under the lineplot
plt.fill_between(x=df['Time'], y1=df['Sales'], alpha=0.3)

# Customize the chart
plt.title('Sales Over Time')
plt.xlabel('Time of Day')
plt.ylabel('Sales ($)')

# Show the plot
plt.show()