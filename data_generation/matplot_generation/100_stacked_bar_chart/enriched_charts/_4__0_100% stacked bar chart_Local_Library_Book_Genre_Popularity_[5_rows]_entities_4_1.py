
import matplotlib.pyplot as plt

# Preparing data
categories = [
    'Classic Literature', 'Contemporary Literature', 'Poetry', 'Science Fiction',
    'Fantasy', 'Non-Fiction', 'Drama', 'Mystery', 'Biography', 'Autobiography', 'History', 'Philosophy'
]
A = [45, 20, 25, 35, 40, 30, 25, 20, 30, 25, 40, 35]
B = [30, 35, 30, 30, 35, 40, 25, 30, 40, 35, 30, 30]
C = [25, 45, 45, 35, 25, 30, 50, 50, 30, 40, 30, 35]

# Summing the data points to normalize
totals = [i + j + k for i, j, k in zip(A, B, C)]
A_percentage = [i / j * 100 for i, j in zip(A, totals)]
B_percentage = [i / j * 100 for i, j in zip(B, totals)]
C_percentage = [i / j * 100 for i, j in zip(C, totals)]

fig, ax = plt.subplots(figsize=(12, 10))  # Changed width & height of the chart

# Stacking the bars vertically
ax.bar(categories, A_percentage, color='#FF5733', edgecolor='white', width=0.8)  # Changed color & bandwidth
ax.bar(categories, B_percentage, bottom=A_percentage, color='#33FF57', edgecolor='white', width=0.8)  # Changed color
ax.bar(categories, C_percentage, bottom=[i + j for i, j in zip(A_percentage, B_percentage)], color='#3357FF', edgecolor='white', width=0.8)  # Changed color

# Adding labels
ax.set_ylabel('Percentage')
ax.set_title('Popularity of Literature Genres')

# Customizing the legend
plt.legend(['Classic', 'Contemporary', 'Modern'], loc='upper right', bbox_to_anchor=(1.1, 1))

plt.show()