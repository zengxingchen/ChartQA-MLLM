
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Define the data for the bubble chart in a DataFrame
data = {
    'Item': ['Laptop', 'Smartphone', 'Tablet', 'Smartwatch', 'Headphones', 
             'Speaker', 'Camera', 'Drone', 'Printer', 'Monitor', 'Keyboard', 
             'Mouse', 'Gaming Console', 'VR Headset'],
    'Weight': [1.5, 0.2, 0.5, 0.1, 0.3, 1.0, 0.8, 1.2, 6.0, 4.0, 0.6, 0.1, 3.5, 1.1],
    'Price': [1200, 800, 600, 200, 150, 300, 500, 1000, 250, 350, 100, 50, 400, 600],
    'Popularity': [85, 90, 75, 70, 80, 65, 77, 82, 60, 73, 68, 66, 83, 78],
    'Color': ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
              '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', 
              '#e7969c', '#aec7e8', '#ffbb78', '#98df8a']
}

df = pd.DataFrame(data)

# Set the size of the bubble chart
plt.figure(figsize=(12, 9))

# Create the bubble chart
bubble_chart = sns.scatterplot(data=df, x='Weight', y='Price', 
                               size='Popularity', hue='Color', 
                               sizes=(100, 2000), edgecolor='w', alpha=0.7, palette=df['Color'].tolist())

# Customize the axes and title
plt.xlabel('Weight (kg)')
plt.ylabel('Price ($)')
plt.title('Gadget Popularity: Weight vs. Price', pad=20)
plt.legend(title='Gadget Color', bbox_to_anchor=(1.05, 1), loc=2)

# Show the plot
plt.show()