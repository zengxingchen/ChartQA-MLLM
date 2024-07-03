
import matplotlib.pyplot as plt

# Data from your table
data = [
    {'Flavor': 'Vanilla', 'Monthly_Sales(Jan)': 120, 'Monthly_Sales(Jun)': 180, 'Average_Temperature(Jun)': 75, 'Flavor_Rating': 4.5},
    {'Flavor': 'Chocolate', 'Monthly_Sales(Jan)': 95, 'Monthly_Sales(Jun)': 170, 'Average_Temperature(Jun)': 75, 'Flavor_Rating': 4.7},
    {'Flavor': 'Strawberry', 'Monthly_Sales(Jan)': 110, 'Monthly_Sales(Jun)': 160, 'Average_Temperature(Jun)': 75, 'Flavor_Rating': 4.3},
    {'Flavor': 'Mint Chocolate', 'Monthly_Sales(Jan)': 70, 'Monthly_Sales(Jun)': 140, 'Average_Temperature(Jun)': 75, 'Flavor_Rating': 4.4},
    {'Flavor': 'Rocky Road', 'Monthly_Sales(Jan)': 60, 'Monthly_Sales(Jun)': 130, 'Average_Temperature(Jun)': 75, 'Flavor_Rating': 4.6},
    {'Flavor': 'Cookie Dough', 'Monthly_Sales(Jan)': 55, 'Monthly_Sales(Jun)': 125, 'Average_Temperature(Jun)': 75, 'Flavor_Rating': 4.8},
    {'Flavor': 'Pistachio', 'Monthly_Sales(Jan)': 30, 'Monthly_Sales(Jun)': 85, 'Average_Temperature(Jun)': 75, 'Flavor_Rating': 4.2},
    {'Flavor': 'Salted Caramel', 'Monthly_Sales(Jan)': 65, 'Monthly_Sales(Jun)': 150, 'Average_Temperature(Jun)': 75, 'Flavor_Rating': 4.7},
    {'Flavor': 'Butter Pecan', 'Monthly_Sales(Jan)': 40, 'Monthly_Sales(Jun)': 100, 'Average_Temperature(Jun)': 75, 'Flavor_Rating': 4.5}
]

# Prepare data for plotting
flavors = [d['Flavor'] for d in data]
sales_jan = [d["Monthly_Sales(Jan)"] for d in data]
sales_jun = [d["Monthly_Sales(Jun)"] for d in data]
ratings = [d["Flavor_Rating"] for d in data]
# Average temperature will define the color, but since it's the same for all we'll use a placeholder
average_temperature = [d["Average_Temperature(Jun)"] for d in data]

# Normalize ratings for bubble sizes
size = [(rating / max(ratings)) * 1000 for rating in ratings]

# Create the bubble chart
plt.figure(figsize=(10, 8))
scatter = plt.scatter(sales_jan, sales_jun, s=size, c=average_temperature, alpha=0.5)

# Add titles and labels
plt.title('Ice Cream Flavor Popularity')
plt.xlabel('Monthly Sales in January')
plt.ylabel('Monthly Sales in June')

# Create a legend for the flavor ratings
for rating in set(ratings):
    plt.scatter([], [], s=(rating / max(ratings)) * 1000, c='grey', alpha=0.5, label=str(rating))
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Flavor Rating')

# Add flavor names as text labels next to the bubbles
for i, flavor in enumerate(flavors):
    plt.text(sales_jan[i], sales_jun[i], flavor, ha='center', va='center', fontsize=9)

plt.grid(True)
plt.show()