
import matplotlib.pyplot as plt

# Table data
food_category = ['Fruits', 'Vegetables', 'Dairy', 'Grains', 'Protein', 'Other']
market_share = [40.2, 30.1, 15.4, 7.5, 5.0, 1.8]
colors = ['#FFA07A', '#20B2AA', '#FFD700', '#CD5C5C', '#6A5ACD', '#708090']

# Plot
fig, ax = plt.subplots(figsize=(12, 8))  # Change width and height of the chart
ax.pie(market_share, labels=food_category, autopct='%1.1f%%', startangle=140, colors=colors)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Distribution of Food Consumption by Category in 2023', pad=20)
plt.show()