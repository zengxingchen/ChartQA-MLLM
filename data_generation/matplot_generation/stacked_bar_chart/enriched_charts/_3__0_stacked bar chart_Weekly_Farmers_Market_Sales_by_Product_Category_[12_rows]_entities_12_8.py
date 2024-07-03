
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June']
books = [200, 250, 220, 210, 240, 230]
stationery = [50, 45, 55, 60, 50, 55]
online_courses = [100, 120, 110, 130, 140, 150]
workshops = [80, 90, 85, 95, 100, 105]

# Stacked Bar Chart
fig, ax = plt.subplots(figsize=(12, 8))  # changing width and height of the chart

bar_width = 0.4  # change width of bars
index = range(len(months))

p1 = plt.bar(index, books, bar_width, label='Books', color='#FF6347')
p2 = plt.bar(index, stationery, bar_width, bottom=books, label='Stationery', color='#4682B4')
p3 = plt.bar(index, online_courses, bar_width, bottom=[b + s for b, s in zip(books, stationery)], label='Online Courses', color='#32CD32')
p4 = plt.bar(index, workshops, bar_width, bottom=[b + s + o for b, s, o in zip(books, stationery, online_courses)], label='Workshops', color='#FFD700')

plt.ylabel('Expenses in USD')
plt.xticks(index, months)
plt.title('Educational Monthly Expenses')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), shadow=True, ncol=1)

# Customizing the grid
plt.grid(axis='y')

# Adding numerical labels to each bar segment
for i in range(len(months)):
    plt.text(i, books[i] / 2, str(books[i]), ha='center', va='center', color='white')
    plt.text(i, books[i] + stationery[i] / 2, str(stationery[i]), ha='center', va='center', color='white')
    plt.text(i, books[i] + stationery[i] + online_courses[i] / 2, str(online_courses[i]), ha='center', va='center', color='white')
    plt.text(i, books[i] + stationery[i] + online_courses[i] + workshops[i] / 2, str(workshops[i]), ha='center', va='center', color='white')

plt.show()