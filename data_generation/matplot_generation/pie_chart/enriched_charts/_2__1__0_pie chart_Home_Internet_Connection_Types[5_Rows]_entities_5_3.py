
import matplotlib.pyplot as plt

# Data
destinations = ['Paris', 'Bali', 'Tokyo', 'New York', 'Rome', 'Sydney', 'Cape Town', 'Dubai', 'Rio de Janeiro']
percentages = [25.00, 20.00, 15.00, 10.00, 8.00, 7.00, 6.00, 5.00, 4.00]
colors = ['#FF5733', '#33FFBD', '#3375FF', '#FF33A8', '#85FF33', '#FFC300', '#8D33FF', '#FF3380', '#33FFF9']

# Create a pie chart
plt.figure(figsize=(10, 6))
plt.pie(percentages, labels=destinations, autopct='%1.1f%%', startangle=140, colors=colors)

# Title
plt.title('Popular Travel Destinations in 2023', fontsize=16)

# Display the chart
plt.show()