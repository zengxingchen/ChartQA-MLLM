
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Given chart table data
data = [
    {'Month': 'January', ' Rainfall (mm)': 78}, 
    {'Month': 'February', ' Rainfall (mm)': 55}, 
    {'Month': 'March', ' Rainfall (mm)': 110}, 
    {'Month': 'April', ' Rainfall (mm)': 123}, 
    {'Month': 'May', ' Rainfall (mm)': 90}, 
    {'Month': 'June', ' Rainfall (mm)': 73}, 
    {'Month': 'July', ' Rainfall (mm)': 98}, 
    {'Month': 'August', ' Rainfall (mm)': 110}, 
    {'Month': 'September', ' Rainfall (mm)': 85}, 
    {'Month': 'October', ' Rainfall (mm)': 100}, 
    {'Month': 'November', ' Rainfall (mm)': 60}, 
    {'Month': 'December', ' Rainfall (mm)': 82}
]

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data)

# Convert 'Month' to a categorical type and order it correctly
ordering = ['January', 'February', 'March', 'April', 'May', 'June', 
            'July', 'August', 'September', 'October', 'November', 'December']
df['Month'] = pd.Categorical(df['Month'], categories=ordering, ordered=True)

# Sort the DataFrame based on 'Month'
df.sort_values(by='Month', inplace=True)

# Seaborn style
sns.set_theme(style='darkgrid')

# Plotting with seaborn for styling
fig, ax = plt.subplots()
sns.lineplot(data=df, x='Month', y=' Rainfall (mm)', ax=ax, color='royalblue', lw=2)

# Filling the area under the plot with matplotlib's fill_between
ax.fill_between(df['Month'], df[' Rainfall (mm)'], color='lightblue')

# Customize the plot with labels, title and a grid
ax.set_xlabel('Month')
ax.set_ylabel('Rainfall (mm)')
ax.set_title('Monthly Rainfall')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Show the plot
plt.tight_layout()  # Adjust subplots to fit the figure area.
plt.show()