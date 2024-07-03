
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create DataFrame from the data provided
data = [
    {'Date': '2023-03-01', 'Temperature (°C)': 7, 'Daily Sales ($)': 450},
    {'Date': '2023-03-02', 'Temperature (°C)': 12, 'Daily Sales ($)': 520},
    {'Date': '2023-03-03', 'Temperature (°C)': 9, 'Daily Sales ($)': 480},
    {'Date': '2023-03-04', 'Temperature (°C)': 14, 'Daily Sales ($)': 600},
    {'Date': '2023-03-05', 'Temperature (°C)': 8, 'Daily Sales ($)': 470}
]
df = pd.DataFrame(data)

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Generate a scatterplot
plt.figure(figsize=(10, 6))
scatter_plot = sns.scatterplot(
    data=df,
    x='Temperature (°C)', 
    y='Daily Sales ($)',
    hue='Date',  # encode date on color
    size='Temperature (°C)',  # use temperature for size encoding
    sizes=(100, 400),  # specify the range of sizes
    palette='viridis',  # use a color palette that represents time well
    legend='full'  # display a legend for size and hue
)

# Improve the appearance of the legend (dates might appear in a non-readable way)
handles, labels = scatter_plot.get_legend_handles_labels()
plt.legend(handles=handles[1:], labels=labels[1:], title='Date')

# Show the plot
plt.show()