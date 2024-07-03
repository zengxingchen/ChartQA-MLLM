
import matplotlib.pyplot as plt
from datetime import datetime

# Provided chart data
data = [
    {'Date': '2023-03-01', 'Tomatoes/kg': 2.99, 'Apples/kg': 3.5, 'Lettuce/each': 1.2, 'Potatoes/kg': 0.8, 'Oranges/kg': 4.0, 'Honey/500g': 6.0},
    {'Date': '2023-03-08', 'Tomatoes/kg': 3.1, 'Apples/kg': 3.6, 'Lettuce/each': 1.25, 'Potatoes/kg': 0.85, 'Oranges/kg': 4.2, 'Honey/500g': 6.2},
    ... # (include all the data points as provided above)
    {'Date': '2023-05-10', 'Tomatoes/kg': 3.1, 'Apples/kg': 3.6, 'Lettuce/each': 1.25, 'Potatoes/kg': 0.83, 'Oranges/kg': 4.2, 'Honey/500g': 6.25}
]

# Parsing the dates and sorting data by date
data.sort(key=lambda x: datetime.strptime(x['Date'], '%Y-%m-%d'))

# Extracting the dates
dates = [datetime.strptime(d['Date'], '%Y-%m-%d') for d in data]

# Extracting prices for each product
tomatoes = [d['Tomatoes/kg'] for d in data]
apples = [d['Apples/kg'] for d in data]
lettuce = [d['Lettuce/each'] for d in data]
potatoes = [d['Potatoes/kg'] for d in data]
oranges = [d['Oranges/kg'] for d in data]
honey = [d['Honey/500g'] for d in data]

# Stacking the data
plt.figure(figsize=(10, 8))

bottom1 = list(map(lambda x, y: x + y, tomatoes, apples))
bottom2 = list(map(lambda x, y: x + y, bottom1, lettuce))
bottom3 = list(map(lambda x, y: x + y, bottom2, potatoes))
bottom4 = list(map(lambda x, y: x + y, bottom3, oranges))

# Plotting each stack
plt.bar(dates, tomatoes, label='Tomatoes/kg')
plt.bar(dates, apples, bottom=tomatoes, label='Apples/kg')
plt.bar(dates, lettuce, bottom=bottom1, label='Lettuce/each')
plt.bar(dates, potatoes, bottom=bottom2, label='Potatoes/kg')
plt.bar(dates, oranges, bottom=bottom3, label='Oranges/kg')
plt.bar(dates, honey, bottom=bottom4, label='Honey/500g')

# Customizing the plot with diversified visual encodings
plt.title('Prices Stacked Bar Chart')
plt.xlabel('Date')
plt.ylabel('Price')
plt.xticks(dates, [date.strftime('%Y-%m-%d') for date in dates], rotation=45)
plt.legend(title='Product Prices')

# Tight layout to ensure proper spacing
plt.tight_layout()

# Show plot with added grid
plt.grid(True)
plt.show()