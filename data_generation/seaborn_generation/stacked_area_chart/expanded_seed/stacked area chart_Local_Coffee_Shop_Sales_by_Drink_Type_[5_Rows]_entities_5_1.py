
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data provided
data = [
    {'Date': '2023-01-01', 'Espresso': 10, 'Latte': 20, 'Cappuccino': 15, 'Americano': 5, 'Mocha': 25},
    {'Date': '2023-01-02', 'Espresso': 17, 'Latte': 35, 'Cappuccino': 21, 'Americano': 13, 'Mocha': 29},
    {'Date': '2023-01-03', 'Espresso': 15, 'Latte': 29, 'Cappuccino': 19, 'Americano': 16, 'Mocha': 22},
    {'Date': '2023-01-04', 'Espresso': 9, 'Latte': 22, 'Cappuccino': 14, 'Americano': 8, 'Mocha': 18},
    {'Date': '2023-01-05', 'Espresso': 13, 'Latte': 33, 'Cappuccino': 16, 'Americano': 11, 'Mocha': 26}
]

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(data)

# Convert the 'Date' column to datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Set the aesthetic style of the plots
sns.set_style('whitegrid')

# Prepare data for the stackplot
dates = df['Date']
columns = df.columns[1:]  # Exclude 'Date' column for stackplot data
y = [df[col].values for col in columns]

# Create the figure and axis objects
fig, ax = plt.subplots()

# Create the stackplot
ax.stackplot(dates, y, labels=columns, alpha=0.8)

# Decorate the plot
ax.set_title('Coffee Sales Data (Stacked Area Chart)')
ax.set_xlabel('Date')
ax.set_ylabel('Number of Cups Sold')
ax.legend(loc='upper left')

# Rotate date labels for better readability
plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)

# Show the plot
plt.tight_layout()
plt.show()