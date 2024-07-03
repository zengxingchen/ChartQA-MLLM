
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Manufacturer': 'Samsung', 'Market Share(%)': 21},
    {'Manufacturer': 'Apple', 'Market Share(%)': 16},
    {'Manufacturer': 'Xiaomi', 'Market Share(%)': 11},
    {'Manufacturer': 'Oppo', 'Market Share(%)': 8},
    {'Manufacturer': 'Vivo', 'Market Share(%)': 7},
    {'Manufacturer': 'Realme', 'Market Share(%)': 4},
    {'Manufacturer': 'Motorola', 'Market Share(%)': 2},
    {'Manufacturer': 'Others', 'Market Share(%)': 31}
]

# Extracting the data for the pie chart
manufacturers = [d['Manufacturer'] for d in data]
market_shares = [d['Market Share(%)'] for d in data]
colors = plt.cm.tab20c.colors  # Using a diverse set of colors from one of matplotlib's colormaps

# Create a pie chart
plt.figure(figsize=(10, 8))  # Set the figure size
plt.pie(market_shares, labels=manufacturers, autopct='%1.1f%%', startangle=140, colors=colors)

# Draw a circle at the center to make it a donut chart
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular
plt.title('Smartphone Market Share (2023)')  # Adding a title to the pie chart
plt.show()