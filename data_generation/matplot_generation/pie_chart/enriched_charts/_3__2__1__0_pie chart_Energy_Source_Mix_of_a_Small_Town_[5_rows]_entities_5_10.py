
import matplotlib.pyplot as plt

labels = 'Accommodation', 'Food and Beverages', 'Transport', 'Entertainment', 'Shopping', 'Miscellaneous'
sizes = [500, 300, 200, 150, 100, 75]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

plt.figure(figsize=(10,7))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

plt.title('Vacation Expense Distribution', pad=20)
plt.axis('equal')  
plt.show()