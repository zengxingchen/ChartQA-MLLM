
import matplotlib.pyplot as plt

# Data
cities = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
    "Philadelphia", "San Antonio", "San Diego", "Dallas", "Seattle",
    "Denver", "Washington", "Boston", "San Jose", "Austin",
    "Miami", "Atlanta", "Orlando", "Las Vegas", "San Francisco"
]
tourist_visits = [200000, 180000, 160000, 150000, 140000, 130000, 120000, 110000, 100000, 95000, 90000, 85000, 80000, 75000, 70000, 69000, 68000, 67000, 66000, 65000]
expenses = [4000, 3800, 3500, 3700, 3000, 3400, 3300, 3200, 3100, 2900, 2800, 2700, 2600, 2500, 2400, 2450, 2550, 2650, 2750, 2850]

# Scatter plot
fig, ax = plt.subplots(figsize=(14, 8))  # Change the width and height of the chart
scatter = ax.scatter(
    tourist_visits,
    expenses,
    alpha=0.7,
    c=[
        '#FF6347', '#4682B4', '#FFA07A', '#20B2AA', '#8470FF',
        '#FF69B4', '#8A2BE2', '#00FA9A', '#CD3333', '#FF4500',
        '#DA70D6', '#1E90FF', '#32CD32', '#800080', '#40E0D0',
        '#FF7F50', '#6A5ACD', '#7B68EE', '#ADFF2F', '#FFB6C1'
    ],
    edgecolors='w'
)

# Customizing the looks of the plot
ax.set_title('Average Monthly Tourist Visits vs Average Monthly Expenses', pad=20)
ax.set_xlabel('Average Monthly Tourist Visits')
ax.set_ylabel('Average Monthly Expenses (USD)')

# Adding the city names as labels next to each point
for i, city in enumerate(cities):
    ax.annotate(city, (tourist_visits[i], expenses[i]), fontsize=8)

plt.show()