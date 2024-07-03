
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
visitors = [300, 450, 350, 600, 750, 900, 800, 850, 650, 500, 400, 350]

colors = [
    '#FF0000', '#FF4500', '#FF6347', '#FF7F50', '#FF8C00', 
    '#FFA500', '#FFD700', '#FFFF00', '#ADFF2F', '#7FFF00', 
    '#32CD32', '#00FF00'
]

plt.figure(figsize=(14, 8))

plt.scatter(months, visitors, c=colors)

plt.title('Monthly Visitor Statistics for 2024', pad=20)
plt.xlabel('Month')
plt.ylabel('Number of Visitors')
plt.xticks(months)

plt.show()