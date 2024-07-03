
import matplotlib.pyplot as plt

# Data for the chart
technologies = ['Artificial Intelligence', 'Blockchain', 'Quantum Computing', 'Augmented Reality', 'Virtual Reality', '5G Networks', 'Other']
adoption_rates = [30, 15, 5, 10, 10, 20, 10]
colors = ['#FF5733', '#33FFBD', '#335BFF', '#FF33A6', '#33FF57', '#FF8C33', '#6A33FF']

# Create a pie chart
plt.figure(figsize=(10, 10)) # Set the width and height of the chart
plt.pie(adoption_rates, labels=technologies, autopct='%1.1f%%', colors=colors, startangle=90)

plt.title('Projected Adoption Rates of Emerging Technologies in 2030', y=1.08) # Change the headline to match the topic
plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the chart
plt.show()