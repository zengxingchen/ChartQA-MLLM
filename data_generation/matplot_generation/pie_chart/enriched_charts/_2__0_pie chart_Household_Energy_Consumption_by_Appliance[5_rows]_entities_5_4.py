
import matplotlib.pyplot as plt

# Data to plot
labels = 'Fiction', 'Non-Fiction', 'Science', 'Biography', 'Comics'
sizes = [40.0, 30.0, 15.0, 10.0, 5.0]
colors = ['#ff6666','#66ff66','#6666ff','#ffcc66','#66cccc']

# Create pie chart
plt.figure(figsize=(12, 9))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

plt.title('Book Sales Distribution by Genre in 2023', pad=20)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()