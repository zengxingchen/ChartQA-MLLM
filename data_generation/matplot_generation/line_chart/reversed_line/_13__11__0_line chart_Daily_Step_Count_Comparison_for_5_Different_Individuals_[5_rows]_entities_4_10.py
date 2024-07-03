
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
sales = [500, 550, 700, 600, 800, 900, 1000, 950, 850, 750, 650, 600]

plt.figure(figsize=(14, 10))
plt.plot(months, sales, color='#1f77b4', marker='o')

# Adding labels with annotations
for i, (month, sale) in enumerate(zip(months, sales)):
    plt.annotate(f'${sale}', (month, sale), textcoords="offset points", xytext=(0,10), ha='center')

# Inverting y-axis
plt.gca().invert_yaxis()

# Adding title and labels
plt.title('Monthly Sales in a Small Business', pad=20)
plt.xlabel('Month')
plt.ylabel('Sales ($)')

# Display chart
plt.show()