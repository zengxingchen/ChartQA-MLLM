
import matplotlib.pyplot as plt

# Data
countries = ['United States', 'China', 'Japan', 'Germany', 'South Korea', 
             'France', 'India', 'United Kingdom', 'Brazil', 'Russia', 
             'Canada', 'Italy', 'Australia', 'Spain', 'Netherlands']
research_spending = [611.8, 451.2, 175.2, 120.6, 78.5,
                     62.4, 50.3, 44.6, 33.1, 32.6,
                     28.4, 24.8, 20.1, 19.8, 18.3]

# Colors
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700',
          '#FF5733', '#DAF7A6', '#FFC300', '#C70039', '#900C3F',
          '#581845', '#28B463', '#1F618D', '#9B59B6', '#5DADE2']

# Pie chart
fig, ax = plt.subplots(figsize=(12, 8))  # Width, Height of the chart
ax.pie(research_spending, labels=countries, colors=colors, autopct='%1.1f%%', startangle=140)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Global Research and Development Spending by Country (Billion USD)', pad=20)
plt.show()