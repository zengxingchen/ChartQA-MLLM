
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data = [
    {'Day': 'Monday', 'Espresso': '15%', 'Latte': '35%', 'Cappuccino': '25%', 'American': '10%', 'Tea': '10%', 'Hot Chocolate': '5%'},
    {'Day': 'Tuesday', 'Espresso': '20%', 'Latte': '30%', 'Cappuccino': '22%', 'American': '13%', 'Tea': '10%', 'Hot Chocolate': '5%'},
    {'Day': 'Wednesday', 'Espresso': '18%', 'Latte': '32%', 'Cappuccino': '25%', 'American': '10%', 'Tea': '12%', 'Hot Chocolate': '3%'},
    {'Day': 'Thursday', 'Espresso': '15%', 'Latte': '33%', 'Cappuccino': '27%', 'American': '12%', 'Tea': '8%', 'Hot Chocolate': '5%'},
    {'Day': 'Friday', 'Espresso': '25%', 'Latte': '25%', 'Cappuccino': '20%', 'American': '15%', 'Tea': '10%', 'Hot Chocolate': '5%'},
    {'Day': 'Saturday', 'Espresso': '30%', 'Latte': '20%', 'Cappuccino': '18%', 'American': '15%', 'Tea': '12%', 'Hot Chocolate': '5%'},
    {'Day': 'Sunday', 'Espresso': '22%', 'Latte': '31%', 'Cappuccino': '23%', 'American': '10%', 'Tea': '9%', 'Hot Chocolate': '5%'}
]

# Transform data into a pandas DataFrame
df = pd.DataFrame(data)

# Convert percentage strings to numerical values
for col in df.columns:
    if col != 'Day':
        df[col] = df[col].str.rstrip('%').astype('float') / 100

# Prepare data for 100% stacked bar chart
df.set_index('Day', inplace=True)
df.sort_index(inplace=True)

# Calculate cumulative sum for stacking
cumsum_df = df.cumsum(axis=1)

# Start plotting
df.plot(kind='bar', stacked=True, figsize=(10, 7))

# Customizing the plot with seaborn visual encodings
palette = sns.color_palette("husl", len(df.columns))
for i, col in enumerate(df.columns):
    # Plotting each layer of the stacked bar
    plt.bar(df.index, df[col], bottom=cumsum_df[col] - df[col], color=palette[i], edgecolor='white')

# Additional customizations
plt.xticks(rotation=45)
plt.yticks(ticks=[0, 0.2, 0.4, 0.6, 0.8, 1], labels=['0%', '20%', '40%', '60%', '80%', '100%'])
plt.xlabel('Day of the Week')
plt.ylabel('Percentage')
plt.title('Percentage of Drinks Sold by Day')
plt.legend(df.columns, bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Show the plot
plt.show()