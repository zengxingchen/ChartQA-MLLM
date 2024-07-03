
import matplotlib.pyplot as plt

# Data points
activities = ['Running', 'Swimming', 'Cycling', 'Weightlifting', 'Yoga', 'Martial Arts', 'Others']
market_share = [30.0, 15.0, 25.0, 10.0, 8.0, 7.0, 5.0]

# Colors using hexadecimal color codes
colors = ['#ff9999', '#66c2ff', '#99ff66', '#ffcc66', '#c266ff', '#ff66b2', '#c2ffcc']

# Plotting the pie chart
plt.figure(figsize=(8, 8))  # Width and height of the chart
plt.pie(market_share, labels=activities, colors=colors, autopct='%1.1f%%', startangle=140)

# Title of the chart
plt.title('Popularity of Different Physical Activities in 2023', pad=20)

# Display the chart
plt.show()