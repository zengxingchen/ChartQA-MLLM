
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June']
books = [50, 60, 55, 70, 65, 75]
magazines = [30, 35, 32, 40, 38, 42]
newspapers = [20, 25, 22, 30, 28, 35]
digital_media = [40, 45, 42, 50, 48, 55]
comics = [15, 20, 18, 25, 22, 30]

# Stacked Bar Chart
fig, ax = plt.subplots(figsize=(10, 8))  # changing width and height of the chart

bar_width = 0.6  # change width of bars
index = range(len(months))

p1 = plt.bar(index, books, bar_width, label='Books', color='#FF4500')
p2 = plt.bar(index, magazines, bar_width, bottom=books, label='Magazines', color='#1E90FF')
p3 = plt.bar(index, newspapers, bar_width, bottom=[b + m for b, m in zip(books, magazines)], label='Newspapers', color='#3CB371')
p4 = plt.bar(index, digital_media, bar_width, bottom=[b + m + n for b, m, n in zip(books, magazines, newspapers)], label='Digital Media', color='#FFD700')
p5 = plt.bar(index, comics, bar_width, bottom=[b + m + n + d for b, m, n, d in zip(books, magazines, newspapers, digital_media)], label='Comics', color='#DA70D6')

plt.xlabel('Months')
plt.xticks(index, months)
plt.title('Monthly Reading Materials Expenditure', pad=30)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), shadow=True, ncol=1)

# Customizing the grid
plt.grid(axis='x')

# Adding numerical labels
for i in index:
    total = books[i] + magazines[i] + newspapers[i] + digital_media[i] + comics[i]
    plt.text(i, total + 5, str(total), ha='center', va='bottom')

plt.show()