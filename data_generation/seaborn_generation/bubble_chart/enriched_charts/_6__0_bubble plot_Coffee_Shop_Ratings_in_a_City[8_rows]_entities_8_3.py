
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Prepare the data in a Pandas DataFrame
data = {
    'Fruit': ['Apple', 'Banana', 'Orange', 'Strawberry', 'Blueberry', 'Kiwi', 'Mango', 'Pineapple', 'Grapes', 'Watermelon', 'Avocado'],
    'Vitamin C (mg)': [14, 10, 70, 85, 10, 92, 60, 47, 4, 12, 10],
    'Calories': [95, 105, 62, 50, 85, 42, 202, 82, 62, 30, 234],
    'Popularity': [75, 85, 90, 80, 65, 70, 55, 60, 50, 95, 45]
}
df = pd.DataFrame(data)

# Create the plot
plt.figure(figsize=(16, 10))
bubble = sns.scatterplot(data=df, x='Calories', y='Vitamin C (mg)', size='Popularity', hue='Fruit', 
                         palette=['#FF0000','#FFA500','#FFFF00','#008000','#0000FF','#4B0082','#EE82EE','#00FFFF','#8A2BE2','#FFC0CB','#808080'], 
                         sizes=(50, 1500), alpha=0.7, edgecolor='w', linewidth=0.5)

# Customize the axes and title
plt.title('Health Benefits of Various Fruits: Vitamin C Content vs. Calories', fontsize=18)
plt.xlabel('Calories per Serving', fontsize=14)
plt.ylabel('Vitamin C Content (mg)', fontsize=14)

# Adjust legend
bubble.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Fruits')

# Show the bubble chart
plt.show()