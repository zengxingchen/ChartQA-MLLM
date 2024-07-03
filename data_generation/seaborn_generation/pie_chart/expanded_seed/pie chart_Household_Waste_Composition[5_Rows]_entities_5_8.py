
import matplotlib.pyplot as plt
import seaborn as sns

# Provided data
data = [
    {'Category': 'Food Waste', 'Percentage(%)': 44},
    {'Category': 'Paper and Cardboard', 'Percentage(%)': 27},
    {'Category': 'Plastics', 'Percentage(%)': 12},
    {'Category': 'Glass', 'Percentage(%)': 9},
    {'Category': 'Metal', 'Percentage(%)': 8}
]

# Extract the categories and percentages from the data
categories = [entry['Category'] for entry in data]
percentages = [entry['Percentage(%)'] for entry in data]

# Set Seaborn styles for aesthetic improvements
sns.set(style="whitegrid", context="talk")

# Create the pie chart
plt.figure(figsize=(10, 6))  # Set the figure size
plt.pie(percentages, labels=categories, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("hsv", len(data)))

# Add a circle at the center to turn the pie chart into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()  # Get the current figure
fig.gca().add_artist(centre_circle)  # Get the current axes and add the circle to the plot

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')

# Add a title
plt.title('Composition of Waste by Category', pad=20)

# Show the plot
plt.show()