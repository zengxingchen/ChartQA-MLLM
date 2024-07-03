
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame from the given data
data = [
    {'Date': '2023-03-20', 'Pastry Type': 'Croissant', 'Sales (Units)': 120},
    {'Date': '2023-03-20', 'Pastry Type': 'Muffin', 'Sales (Units)': 90},
    {'Date': '2023-03-21', 'Pastry Type': 'Croissant', 'Sales (Units)': 135},
    {'Date': '2023-03-21', 'Pastry Type': 'Muffin', 'Sales (Units)': 95},
    {'Date': '2023-03-22', 'Pastry Type': 'Croissant', 'Sales (Units)': 140},
    {'Date': '2023-03-22', 'Pastry Type': 'Muffin', 'Sales (Units)': 100},
    {'Date': '2023-03-23', 'Pastry Type': 'Croissant', 'Sales (Units)': 160},
    {'Date': '2023-03-23', 'Pastry Type': 'Muffin', 'Sales (Units)': 110},
    {'Date': '2023-03-24', 'Pastry Type': 'Croissant', 'Sales (Units)': 150}
]
df = pd.DataFrame(data)

# Convert 'Date' from string to datetime for proper plotting
df['Date'] = pd.to_datetime(df['Date'])

# Set the aesthetic parameters of Seaborn
sns.set_theme(style="whitegrid")

# Plot a scatterplot using Seaborn
plt.figure(figsize=(10, 6))

scatter_plot = sns.scatterplot(
    x='Date',
    y='Sales (Units)',
    hue='Pastry Type',    # color the points by 'Pastry Type'
    style='Pastry Type',  # use different markers for 'Pastry Type'
    s=100,                # set the size of the markers
    data=df
)

# Improve the format of x-axis dates
scatter_plot.xaxis.set_major_formatter(plt.FixedFormatter(df['Date'].dt.strftime('%Y-%m-%d')))
plt.xticks(rotation=45)  # rotate x-axis labels for better readability

# Set plot labels and title
plt.xlabel('Date')
plt.ylabel('Sales (Units)')
plt.title('Pastry Sales Scatterplot')

# Show the legend and plot
plt.legend(title='Pastry Type')
plt.tight_layout()  # adjust plot to ensure everything fits without overlapping
plt.show()