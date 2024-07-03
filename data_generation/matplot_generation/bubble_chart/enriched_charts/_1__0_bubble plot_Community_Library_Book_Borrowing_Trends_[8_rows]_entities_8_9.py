
import matplotlib.pyplot as plt

data = {
    'Category': ['Fruits', 'Vegetables', 'Grains', 'Dairy', 'Meat', 'Seafood', 'Nuts', 
                 'Legumes', 'Sweets', 'Beverages', 'Snacks', 'Oils', 'Eggs', 'Herbs & Spices'],
    'Calories': [52, 25, 365, 150, 250, 200, 600, 350, 500, 50, 550, 900, 155, 300],
    'Protein (g)': [0.3, 2.5, 13, 8, 26, 20, 20, 25, 2, 0, 7, 0, 13, 11],
    'Satisfaction Score': [95, 90, 85, 80, 88, 92, 86, 84, 75, 78, 72, 70, 89, 81]
}

size = [value * 10 for value in data['Calories']]

plt.figure(figsize=(16, 10))

scatter = plt.scatter(data['Protein (g)'], data['Satisfaction Score'], 
                      s=size, alpha=0.5, 
                      c=['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF', '#800080', 
                         '#FF4500', '#2E8B57', '#4682B4', '#D2691E', '#8B4513', '#B22222', '#5F9EA0'])

plt.title('Food Category Nutritional Content and Satisfaction', pad=20)
plt.xlabel('Protein Content (g)')
plt.ylabel('Customer Satisfaction Score')

for index, category in enumerate(data['Category']):
    plt.text(data['Protein (g)'][index], data['Satisfaction Score'][index], 
             category, fontsize=9, ha='center', va='center')

plt.grid(True)
plt.show()