
import pandas as pd
import matplotlib.pyplot as plt

# First, convert your data into a pandas DataFrame
data = [
    {'Week': '2021-W01', 'Apples': 150, 'Berries': 120, 'Carrots': 100, 'Lettuce': 180, 'Tomatoes': 90},
    {'Week': '2021-W02', 'Apples': 165, 'Berries': 130, 'Carrots': 110, 'Lettuce': 190, 'Tomatoes': 100},
    {'Week': '2021-W03', 'Apples': 170, 'Berries': 145, 'Carrots': 115, 'Lettuce': 200, 'Tomatoes': 105},
    {'Week': '2021-W04', 'Apples': 160, 'Berries': 135, 'Carrots': 120, 'Lettuce': 210, 'Tomatoes': 110},
    {'Week': '2021-W05', 'Apples': 155, 'Berries': 140, 'Carrots': 125, 'Lettuce': 205, 'Tomatoes': 115},
    {'Week': '2021-W06', 'Apples': 150, 'Berries': 145, 'Carrots': 130, 'Lettuce': 215, 'Tomatoes': 120},
    {'Week': '2021-W07', 'Apples': 145, 'Berries': 150, 'Carrots': 135, 'Lettuce': 220, 'Tomatoes': 125},
    {'Week': '2021-W08', 'Apples': 140, 'Berries': 155, 'Carrots': 140, 'Lettuce': 225, 'Tomatoes': 130},
    {'Week': '2021-W09', 'Apples': 130, 'Berries': 160, 'Carrots': 145, 'Lettuce': 230, 'Tomatoes': 135}
]
df = pd.DataFrame(data)

# Set the index of the DataFrame to be the 'Week' column
df = df.set_index('Week')

# You can create the stacked area plot using the plot.area function from pandas,
# which is built on top of matplotlib
df.plot.area()

# Adding some customizations to match Seaborn's style
plt.style.use('seaborn-darkgrid')  # Setting the style to match Seaborn's default
plt.title('Weekly Sales of Fruits and Vegetables')
plt.xlabel('Week')
plt.ylabel('Quantity Sold')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Show the plot
plt.tight_layout()
plt.show()