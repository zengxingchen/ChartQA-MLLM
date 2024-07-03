
import pandas as pd
import matplotlib.pyplot as plt

# Define the data as a list of dictionaries
data = [
    {'Date': '2023-03-01', 'Espresso': 50, 'Americano': 75, 'Latte': 100, 'Cappuccino': 60, 'Tea': 40},
    {'Date': '2023-03-08', 'Espresso': 55, 'Americano': 80, 'Latte': 110, 'Cappuccino': 65, 'Tea': 45},
    {'Date': '2023-03-15', 'Espresso': 60, 'Americano': 85, 'Latte': 120, 'Cappuccino': 70, 'Tea': 50},
    {'Date': '2023-03-22', 'Espresso': 58, 'Americano': 78, 'Latte': 125, 'Cappuccino': 68, 'Tea': 48},
    {'Date': '2023-03-29', 'Espresso': 62, 'Americano': 82, 'Latte': 130, 'Cappuccino': 72, 'Tea': 52}
]

# Convert the list of dictionaries to a Pandas DataFrame
df = pd.DataFrame(data)

# Convert the 'Date' column to a datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Set the 'Date' column as the index
df.set_index('Date', inplace=True)

# Plot stacked area chart using Matplotlib
fig, ax = plt.subplots(figsize=(10, 6))
labels = df.columns
df.plot(kind='area', stacked=True, ax=ax, labels=labels)

# Customize the plot with Matplotlib
ax.set_title('Coffee Shop Sales Data (Stacked Area Chart)', fontsize=16)
ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Units Sold', fontsize=12)
ax.legend(title='Products', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()