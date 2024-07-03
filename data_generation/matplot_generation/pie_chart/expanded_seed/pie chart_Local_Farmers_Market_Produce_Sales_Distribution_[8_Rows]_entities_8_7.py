
import matplotlib.pyplot as plt

# Data from table
chart_data = [
    {'Produce': 'Tomatoes', 'Percentage Sold': '22%'},
    {'Produce': 'Carrots', 'Percentage Sold': '15%'},
    {'Produce': 'Apples', 'Percentage Sold': '14%'},
    {'Produce': 'Lettuce', 'Percentage Sold': '13%'},
    {'Produce': 'Strawberries', 'Percentage Sold': '12%'},
    {'Produce': 'Potatoes', 'Percentage Sold': '10%'},
    {'Produce': 'Peppers', 'Percentage Sold': '8%'},
    {'Produce': 'Onions', 'Percentage Sold': '6%'}
]

# Extracting produce names and their corresponding percentages
produces = [item['Produce'] for item in chart_data]
percentages = [int(item['Percentage Sold'].strip('%')) for item in chart_data]

# Generating a color map
colors = plt.cm.Spectral([float(x)/max(percentages) for x in percentages])

# Creating the pie chart
plt.figure(figsize=(10, 8)) # Set the figure size
plt.pie(percentages, labels=produces, colors=colors, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 10})

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Produce Sales Distribution', pad=20)  # Title with padding
plt.show()