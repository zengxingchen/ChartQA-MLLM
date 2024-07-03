
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Given chart table data
data = [
    {'Date': '2023-01-01', 'Smartphones': 250, 'Computers': 400, 'Tablets': 150, 'Smart TVs': 200, 'Game Consoles': 180, 'Other Devices': 70},
    {'Date': '2023-01-08', 'Smartphones': 260, 'Computers': 410, 'Tablets': 160, 'Smart TVs': 210, 'Game Consoles': 190, 'Other Devices': 75},
    # ... (additional data rows have been omitted for brevity)
    {'Date': '2023-03-19', 'Smartphones': 330, 'Computers': 480, 'Tablets': 215, 'Smart TVs': 280, 'Game Consoles': 250, 'Other Devices': 105}
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Set the aesthetic style of the plots
sns.set_style('whitegrid')

# Prepare data for the stackplot
x = df['Date']
columns = df.columns[1:]
y = [df[column].values for column in columns]

# Create the stacked area chart
plt.figure(figsize=(10, 6))
plt.stackplot(x, y, labels=columns, alpha=0.8)

# Beautify the plot
plt.legend(loc='upper left')
plt.title('Device Usage Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Devices')
plt.xticks(rotation=45)  # Rotate the x-axis labels for better readability

# Tight layout often provides a better layout
plt.tight_layout()

# Show the plot
plt.show()