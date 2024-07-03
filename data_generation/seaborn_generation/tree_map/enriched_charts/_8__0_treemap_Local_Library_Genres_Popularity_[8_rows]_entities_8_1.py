
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import squarify

# Creating a DataFrame from the provided dataset
data = {
    'Category': ['Fruits', 'Fruits', 'Fruits', 'Fruits', 'Fruits', 
                 'Vegetables', 'Vegetables', 'Vegetables', 'Vegetables', 'Vegetables',
                 'Grains', 'Grains', 'Grains', 'Grains', 'Grains', 
                 'Proteins', 'Proteins', 'Proteins', 'Proteins', 'Proteins',
                 'Dairy', 'Dairy', 'Dairy', 'Dairy', 'Dairy'],
    'Food': ['Apple', 'Banana', 'Orange', 'Grapes', 'Strawberry', 
             'Carrot', 'Broccoli', 'Spinach', 'Tomato', 'Cucumber',
             'Rice', 'Bread', 'Pasta', 'Quinoa', 'Oats', 
             'Chicken Breast', 'Salmon', 'Tofu', 'Beef', 'Eggs',
             'Milk', 'Cheese', 'Yogurt', 'Butter', 'Cream'],
    'Calories': [52, 89, 47, 69, 32, 
                 41, 55, 23, 18, 16,
                 130, 265, 131, 120, 389,
                 165, 208, 76, 250, 155,
                 42, 402, 59, 717, 345]
}

df = pd.DataFrame(data)

# Plotting the treemap
plt.figure(figsize=(22, 14))
colors = ["#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#A133FF", "#33FFA1", "#FFD133", "#33D4FF", "#FF3333", "#33FF33",
          "#7F33FF", "#FFB433", "#FF3399", "#33FFA7", "#337FFF", "#FFC733", "#F333FF", "#33FFAB", "#FF5733", "#33FF57",
          "#3390FF", "#FF3399", "#A1FF33", "#D133FF", "#33FFD1"]

squarify.plot(sizes=df['Calories'], label=df['Food'], color=colors, alpha=0.8)
plt.title('Caloric Content of Various Foods', fontsize=28, fontweight='bold')
plt.axis('off')
plt.show()