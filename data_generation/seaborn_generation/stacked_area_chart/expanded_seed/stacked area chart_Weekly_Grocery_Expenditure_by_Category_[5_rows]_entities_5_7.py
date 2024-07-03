
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Given chart table data
data = [
    {'Date': '2023-03-01', 'Fruits': 45, 'Vegetables': 30, 'Meat': 60, 'Dairy': 25, 'Bakery': 15},
    {'Date': '2023-03-08', 'Fruits': 50, 'Vegetables': 25, 'Meat': 55, 'Dairy': 30, 'Bakery': 20},
    {'Date': '2023-03-15', 'Fruits': 60, 'Vegetables': 35, 'Meat': 50, 'Dairy': 28, 'Bakery': 22},
    {'Date': '2023-03-22', 'Fruits': 55, 'Vegetables': 45, 'Meat': 65, 'Dairy': 33, 'Bakery': 18},
    {'Date': '2023-03-29', 'Fruits': 40, 'Vegetables': 32, 'Meat': 70, 'Dairy': 35, 'Bakery': 20}
]

# Convert to pandas DataFrame
df = pd.DataFrame(data)

# Set Date as index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Create data for stacking
columns = df.columns
data_for_stacking = [df[col] for col in columns]

# We use Seaborn just to set the aesthetic style
sns.set_style('whitegrid')

# Plot stacked area chart
plt.stackplot(df.index, data_for_stacking, labels=columns, alpha=0.8)

# Additional customizations
plt.legend(loc='upper left')
plt.title('Sales Data Over Time')
plt.xlabel('Date')
plt.ylabel('Quantity Sold')
plt.xticks(rotation=45)

# Ensure the dates are nicely spaced
plt.gca().xaxis.set_major_locator(plt.MatplotlibDateFormatter('%Y-%m-%d'))

# Show the plot
plt.tight_layout()
plt.show()