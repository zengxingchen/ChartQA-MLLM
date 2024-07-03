
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Define the data for the bubble chart in a DataFrame
data = {
    'Item': ['Running Shoes', 'Fitness Tracker', 'Yoga Mat', 'Dumbbells', 'Protein Powder', 
             'Treadmill', 'Bicycle', 'Jump Rope', 'Resistance Bands', 'Kettlebells', 
             'Pull-up Bar', 'Foam Roller', 'Exercise Ball', 'Rowing Machine', 'Boxing Gloves'],
    'Weight': [0.8, 0.05, 1.2, 5.0, 1.0, 60.0, 15.0, 0.1, 0.2, 4.5, 3.0, 0.5, 2.0, 25.0, 0.7],
    'Price': [120, 150, 30, 60, 50, 1200, 600, 10, 25, 80, 40, 20, 35, 900, 45],
    'Popularity': [88, 92, 85, 75, 80, 70, 78, 90, 82, 73, 68, 65, 77, 83, 79],
    'Color': ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF', 
              '#FFC300', '#DAF7A6', '#900C3F', '#C70039', '#581845', 
              '#28B463', '#1F618D', '#7D3C98', '#D98880', '#D4AC0D']
}

df = pd.DataFrame(data)

# Set the size of the bubble chart
plt.figure(figsize=(14, 10))

# Create the bubble chart
bubble_chart = sns.scatterplot(data=df, x='Weight', y='Price', 
                               size='Popularity', hue='Color', 
                               sizes=(100, 2000), edgecolor='w', alpha=0.7, palette=df['Color'].tolist())

# Customize the axes and title
plt.xlabel('Weight (kg)')
plt.ylabel('Price ($)')
plt.title('Fitness Equipment Popularity: Weight vs. Price', pad=20)
plt.legend(title='Equipment Color', bbox_to_anchor=(1.05, 1), loc=2)

# Show the plot
plt.show()