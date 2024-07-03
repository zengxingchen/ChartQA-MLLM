
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define the chart data
chart_data = [
    {'Date': '2023-01-01', 'Espresso': 95, 'Cappuccino': 110, 'Latte': 123, 'Americano': 80},
    {'Date': '2023-01-02', 'Espresso': 123, 'Cappuccino': 140, 'Latte': 156, 'Americano': 95},
    {'Date': '2023-01-03', 'Espresso': 116, 'Cappuccino': 130, 'Latte': 146, 'Americano': 88},
    {'Date': '2023-01-04', 'Espresso': 107, 'Cappuccino': 120, 'Latte': 135, 'Americano': 85}
]

# Convert to a DataFrame
df = pd.DataFrame(chart_data)

# Convert 'Date' to datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Melt the DataFrame from wide to long format
df_long = df.melt(id_vars='Date', var_name='Coffee_Type', value_name='Sales')

# Create the line plot using Seaborn
sns.set_theme(style="whitegrid")  # Setting the theme for the plot

plt.figure(figsize=(10, 6))  # Set the figure size
line_plot = sns.lineplot(data=df_long, x='Date', y='Sales', hue='Coffee_Type', marker='o', dashes=False)

# Beautify the plot
plt.title('Coffee Sales Over Time')  # Title of the plot
plt.xlabel('Date')  # X-axis label
plt.ylabel('Number of Cups Sold')  # Y-axis label
plt.xticks(rotation=45)  # Rotate the x-axis labels to show dates at an angle

# Show legend
plt.legend(title='Coffee Type', loc='upper left')

# Display the plot
plt.show()