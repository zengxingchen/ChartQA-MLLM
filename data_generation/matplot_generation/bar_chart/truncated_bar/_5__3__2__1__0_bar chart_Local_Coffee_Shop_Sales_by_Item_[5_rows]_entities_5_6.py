
import matplotlib.pyplot as plt

months = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]
books_read = [
    3, 5, 8, 12, 15, 20,
    18, 16, 14, 10, 6, 4
]

plt.figure(figsize=(14, 10))

bar_width = 0.7
plt.barh(months, books_read, color=[
    '#4B0082', '#FF6347', '#4682B4', '#FF1493', '#8A2BE2',
    '#00CED1', '#FF4500', '#9ACD32', '#FFD700', '#20B2AA',
    '#9370DB', '#FF69B4'
], height=bar_width)

plt.xlabel('Books Read', fontsize=14)
plt.ylabel('Month', fontsize=14)
plt.title('Monthly Book Reading Activity', fontsize=16)

plt.xlim(2, 22)  # Truncate y-axis to start from 2

plt.yticks(months, fontsize=10)

plt.show()