
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data as provided
data = [
    {'Date': '2023-03-01', 'Daily Earnings ($)': 1200, 'Cups of Coffee Sold': 150, 'Pastry Sales ($)': 300},
    {'Date': '2023-03-02', 'Daily Earnings ($)': 1350, 'Cups of Coffee Sold': 180, 'Pastry Sales ($)': 350},
    {'Date': '2023-03-03', 'Daily Earnings ($)': 1100, 'Cups of Coffee Sold': 140, 'Pastry Sales ($)': 250},
    {'Date': '2023-03-04', 'Daily Earnings ($)': 1600, 'Cups of Coffee Sold': 200, 'Pastry Sales ($)': 400},
    {'Date': '2023-03-05', 'Daily Earnings ($)': 1700, 'Cups of Coffee Sold': 210, 'Pastry Sales ($)': 450}
]

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Convert 'Date' column to datetime format for better x-axis representation
df['Date'] = pd.to_datetime(df['Date'])

# Set the style and palette of the Seaborn plot
sns.set(style="whitegrid")
palette = sns.color_palette("husl", 3)

# Plotting the "Daily Earnings ($)"
sns.lineplot(x='Date', y='Daily Earnings ($)', data=df, marker='o', label='Daily Earnings ($)', color=palette[0])

# Plotting the "Cups of Coffee Sold"
sns.lineplot(x='Date', y='Cups of Coffee Sold', data=df, marker='s', label='Cups of Coffee Sold', color=palette[1])

# Plotting the "Pastry Sales ($)"
sns.lineplot(x='Date', y='Pastry Sales ($)', data=df, marker='^', label='Pastry Sales ($)', color=palette[2])

# Additional tweaks for better visualization
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.title('Daily Performance Metrics')  # Chart title
plt.xlabel('Date')  # x-axis label
plt.ylabel('Value')  # y-axis label shared by all metrics

# Show legend with proper title
plt.legend(title='Metric')

# Tight layout often produces a better plot layout
plt.tight_layout()

# Show the plot
plt.show()