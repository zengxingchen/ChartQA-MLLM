
import matplotlib.pyplot as plt

# Data for the chart
technologies = ['Online Courses', 'Virtual Classrooms', 'Educational Apps', 'AI Tutors', 'Blockchain Certificates', 'AR Learning Tools', 'Gamified Learning']
adoption_rates = [35, 25, 20, 10, 5, 3, 2]
colors = ['#4B0082', '#FF4500', '#32CD32', '#1E90FF', '#FFD700', '#FF69B4', '#8A2BE2']

# Create a pie chart
plt.figure(figsize=(12, 8)) # Set the width and height of the chart
plt.pie(adoption_rates, labels=technologies, autopct='%1.1f%%', colors=colors, startangle=140)

plt.title('Projected Adoption Rates of Educational Technologies in 2030', y=1.05) # Change the headline to match the topic
plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the chart
plt.show()