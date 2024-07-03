
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data provided
data = [
    {'Week': 1, 'Fruit Type': 'Apples', 'Units Sold': 150},
    {'Week': 1, 'Fruit Type': 'Oranges', 'Units Sold': 100},
    {'Week': 1, 'Fruit Type': 'Bananas', 'Units Sold': 180},
    {'Week': 2, 'Fruit Type': 'Apples', 'Units Sold': 200},
    {'Week': 2, 'Fruit Type': 'Oranges', 'Units Sold': 120},
    {'Week': 2, 'Fruit Type': 'Bananas', 'Units Sold': 160},
    {'Week': 3, 'Fruit Type': 'Apples', 'Units Sold': 170},
    {'Week': 3, 'Fruit Type': 'Oranges', 'Units Sold': 130},
    {'Week': 3, 'Fruit Type': 'Bananas', 'Units Sold': 190},
    {'Week': 4, 'Fruit Type': 'Apples', 'Units Sold': 180},
    {'Week': 4, 'Fruit Type': 'Oranges', 'Units Sold': 140},
    {'Week': 4, 'Fruit Type': 'Bananas', 'Units Sold': 210}
]

# Converting data to a pandas DataFrame
df = pd.DataFrame(data)

# Defining markers for each 'Fruit Type'
markers = {"Apples": "s", "Oranges": "o", "Bananas": "^"}

# Creating the scatterplot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Week', y='Units Sold', 
                style='Fruit Type', markers=markers, 
                hue='Week', palette='deep', s=100)

# Adding title and labels
plt.title('Fruit Units Sold per Week')
plt.xlabel('Week')
plt.ylabel('Units Sold')

# Show legend
plt.legend(title='Week & Fruit Type')

# Show the plot
plt.show()