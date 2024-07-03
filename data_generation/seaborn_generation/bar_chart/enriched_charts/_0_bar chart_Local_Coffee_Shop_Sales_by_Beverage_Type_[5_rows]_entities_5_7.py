
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Creating the data as a DataFrame
data = {
    'Fruit': ['Apple', 'Orange', 'Banana', 'Strawberry', 'Grape', 'Cherry', 'Watermelon', 'Kiwi', 'Blueberry', 'Pomegranate'],
    'Sales': [340, 210, 450, 120, 250, 160, 300, 190, 230, 180]
}

df = pd.DataFrame(data)

# Sorting data to make the chart easier to read
df = df.sort_values('Sales', ascending=False)

# Set up the matplotlib figure with changed width and height
plt.figure(figsize=(10, 8))

# Create the bar plot
sns.barplot(
    x='Sales',
    y='Fruit',
    data=df,
    palette=[
        '#FF9999', '#99FF99', '#9999FF', '#FFCC99', '#99CCFF', 
        '#FF99CC', '#CC99FF', '#FFFF99', '#99FFFF', '#FF6600'
    ],
    linewidth=1.5,
    edgecolor='black'
)

# Adjust the width of the bars
for bar in plt.gca().patches:
    bar.set_height(0.8)

# Adding chart labels and title
plt.xlabel('Monthly Sales')
plt.ylabel('Fruit')
plt.title('Monthly Sales of Fruits')

# Show the plot
plt.show()