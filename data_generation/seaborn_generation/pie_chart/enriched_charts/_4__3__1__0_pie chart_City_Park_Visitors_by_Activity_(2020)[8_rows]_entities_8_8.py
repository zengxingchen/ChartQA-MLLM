
import matplotlib.pyplot as plt

categories = ['Fruits', 'Vegetables', 'Grains', 'Proteins', 'Dairy', 'Fats', 'Sugars', 'Beverages']
values = [120, 150, 100, 130, 90, 60, 50, 80]
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#FF69B4', '#8A2BE2', '#D2691E', '#40E0D0']

plt.figure(figsize=(12, 8))
plt.pie(values, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.axis('equal')
plt.title('Distribution of Food Categories in a Balanced Diet', pad=40)
plt.show()