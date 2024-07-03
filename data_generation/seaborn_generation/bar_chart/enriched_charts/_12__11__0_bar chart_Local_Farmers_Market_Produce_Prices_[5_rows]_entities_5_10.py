
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Given dataset
data = {
    'Fruit': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grape', 'Honeydew', 'Ita Palm', 'Jackfruit'],
    'Average Calories': [95, 105, 50, 282, 73, 107, 62, 36, 128, 155]
}

# Create DataFrame
df = pd.DataFrame(data)

# Initialize a Matplotlib figure and set its size
plt.figure(figsize=(10, 8))

# Create horizontal bar chart
sns.barplot(
    y='Fruit',
    x='Average Calories',
    data=df,
    palette=[
        '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFD2',
        '#FFC733', '#8D33FF', '#FF8D33', '#33FFF2', '#F233FF'
    ]
)

# Customize the chart
plt.title('Average Calorie Content of Different Fruits', fontsize=16, pad=20)
plt.xlabel('Average Calories', fontsize=14)
plt.ylabel('Fruit', fontsize=14)

# Adjust the height of the bars
for patch in plt.gca().patches:
    patch.set_height(0.6)

# Show the plot
plt.show()