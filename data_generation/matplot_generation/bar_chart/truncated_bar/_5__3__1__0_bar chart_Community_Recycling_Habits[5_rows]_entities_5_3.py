
import matplotlib.pyplot as plt

topics = [
    'Climate Action', 'Clean Water and Sanitation', 'Affordable and Clean Energy', 'Quality Education',
    'Gender Equality', 'Good Health and Well-being', 'Sustainable Cities and Communities', 
    'Responsible Consumption and Production', 'Life Below Water', 'Life on Land',
    'Decent Work and Economic Growth', 'Industry Innovation and Infrastructure', 'Reduced Inequality', 
    'Partnerships for the Goals', 'No Poverty', 'Zero Hunger', 'Peace and Justice Strong Institutions',
    'Climate Action', 'Clean Water and Sanitation', 'Affordable and Clean Energy'
]
popularity = [
    9200, 8700, 8300, 7900, 7500, 7200, 6800, 6500, 6100, 5700, 5400, 5000, 4700, 
    4400, 4100, 3900, 3600, 3300, 3100, 2900
]
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF', '#33FFF5', '#FF9933', 
    '#99FF33', '#33FF99', '#5733FF', '#FF33A6', '#A633FF', '#33FFF5', '#FF9933', 
    '#99FF33', '#33FF99', '#5733FF', '#FF5733', '#33FF57', '#3357FF'
]

plt.figure(figsize=(12, 10))
plt.bar(topics, popularity, color=colors, width=0.5)
plt.xticks(rotation=90)

plt.ylabel('Popularity (in thousands)')
plt.title('Popularity of Sustainability Goals in 2024')
plt.ylim(2500, 9500)
plt.tight_layout()
plt.show()