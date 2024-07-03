
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Your data as a list of dictionaries
data = [
    {'Month': 'Jan-2022', 'Espresso': 300, 'Americano': 350, 'Cappuccino': 200, 'Latte': 400, 'Mocha': 250},
    {'Month': 'Feb-2022', 'Espresso': 310, 'Americano': 340, 'Cappuccino': 210, 'Latte': 410, 'Mocha': 260},
    {'Month': 'Mar-2022', 'Espresso': 320, 'Americano': 330, 'Cappuccino': 220, 'Latte': 420, 'Mocha': 270},
    {'Month': 'Apr-2022', 'Espresso': 330, 'Americano': 320, 'Cappuccino': 230, 'Latte': 430, 'Mocha': 280},
    {'Month': 'May-2022', 'Espresso': 340, 'Americano': 310, 'Cappuccino': 240, 'Latte': 440, 'Mocha': 290},
    {'Month': 'Jun-2022', 'Espresso': 350, 'Americano': 300, 'Cappuccino': 250, 'Latte': 450, 'Mocha': 300},
    {'Month': 'Jul-2022', 'Espresso': 360, 'Americano': 290, 'Cappuccino': 260, 'Latte': 460, 'Mocha': 310},
    {'Month': 'Aug-2022', 'Espresso': 370, 'Americano': 280, 'Cappuccino': 270, 'Latte': 470, 'Mocha': 320},
    {'Month': 'Sep-2022', 'Espresso': 380, 'Americano': 270, 'Cappuccino': 280, 'Latte': 480, 'Mocha': 330},
    {'Month': 'Oct-2022', 'Espresso': 390, 'Americano': 260, 'Cappuccino': 290, 'Latte': 490, 'Mocha': 340},
    {'Month': 'Nov-2022', 'Espresso': 400, 'Americano': 250, 'Cappuccino': 300, 'Latte': 500, 'Mocha': 350},
    {'Month': 'Dec-2022', 'Espresso': 410, 'Americano': 240, 'Cappuccino': 310, 'Latte': 510, 'Mocha': 360}
]

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data)

# Convert the 'Month' column to datetime to help with plotting
df['Month'] = pd.to_datetime(df['Month'], format='%b-%Y')

# Set the index to 'Month' for easier plotting
df = df.set_index('Month')

# Prepare the data for stacking
x = df.index
y = [df[col] for col in df.columns]

# Using Seaborn's style
sns.set(style="whitegrid")

# Create the stackplot
plt.stackplot(x, y, labels=df.columns, alpha=0.8)

# Formatting
plt.legend(loc='upper left')
plt.title('Coffee Sales by Type Over Time')
plt.ylabel('Number of Coffees Sold')
plt.xlabel('Month')
plt.xticks(rotation=45)
plt.tight_layout()  # Adjust the plot to ensure everything fits without overlapping

# Show the plot
plt.show()