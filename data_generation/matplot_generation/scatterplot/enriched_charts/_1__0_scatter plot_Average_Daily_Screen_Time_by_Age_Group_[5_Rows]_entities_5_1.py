
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
sales = [150, 180, 220, 300, 360, 400, 390, 380, 350, 310, 250, 200]

colors = [
    '#FF5733', '#FF8D1A', '#FFC300', '#DAF7A6', '#33FF57', 
    '#33FFF6', '#3375FF', '#8D33FF', '#FF33F6', '#FF338D', 
    '#FF6F33', '#FF3333'
]

plt.figure(figsize=(12, 7))

plt.scatter(months, sales, c=colors)

plt.title('Monthly Sales Data for 2024', pad=20)
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.xticks(months)

plt.show()