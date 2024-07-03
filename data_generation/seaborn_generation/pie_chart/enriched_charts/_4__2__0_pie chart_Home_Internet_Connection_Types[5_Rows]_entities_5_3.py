
import matplotlib.pyplot as plt

# Data
categories = ['Growth in Renewable Energy Sectors', 'Advances in Electric Vehicles', 'Solar Power Adoption', 
              'Wind Power Adoption', 'Hydropower Usage', 'Geothermal Energy Development', 'Bioenergy Advancements', 
              'Nuclear Energy Renaissance']
popularity = [14.7, 11.3, 22.4, 18.2, 9.8, 6.7, 4.5, 12.4]
colors = ['#FFA07A', '#20B2AA', '#778899', '#FFB6C1', '#98FB98', '#DA70D6', '#FFD700', '#8A2BE2']

# Create a pie chart
plt.figure(figsize=(10, 6))
plt.pie(popularity, labels=categories, autopct='%1.1f%%', startangle=140, colors=colors)

# Title
plt.title('Adoption Rates of Various Renewable Energy Sources in 2023', y=1.05)

# Display the chart
plt.show()