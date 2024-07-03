
import matplotlib.pyplot as plt

# Data for the pie chart
categories = ['Digital Advertising', 'E-commerce', 'SaaS', 'Fintech', 'HealthTech', 'EdTech', 'AgriTech', 'SpaceTech', 'LegalTech']
percentages = [25.0, 20.0, 15.0, 12.0, 10.0, 8.0, 5.0, 3.0, 2.0]

# Colors for each section of the pie chart
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#33FFF5', '#FF8333', '#33A8FF', '#F533FF', '#FFA833']

# Create a pie chart
plt.figure(figsize=(12, 10))  # Modify the size of the chart
plt.pie(percentages, labels=categories, colors=colors, startangle=140, autopct='%1.1f%%', pctdistance=0.85)

# Draw a circle at the center to turn the pie chart into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Set the title of the chart
plt.title('Investment Distribution in Future Technologies - 2023', pad=30)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')

# Show the chart
plt.show()