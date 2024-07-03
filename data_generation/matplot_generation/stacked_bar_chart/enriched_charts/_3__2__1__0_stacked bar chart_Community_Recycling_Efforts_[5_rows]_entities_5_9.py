
import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
books = [900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450]
magazines = [450, 470, 480, 490, 500, 520, 530, 540, 560, 570, 590, 600]
newspapers = [350, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470]
comics = [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260]

y = np.arange(len(months))  # the label locations
height = 0.6  # the height of the bars

fig, ax = plt.subplots(figsize=(10, 12))  # Changing width and height of the chart

# Stacked horizontal bar chart
ax.barh(y, books, height, label='Books', color='#4daf4a')
ax.barh(y, magazines, height, left=books, label='Magazines', color='#377eb8')
ax.barh(y, newspapers, height, left=np.add(books, magazines), label='Newspapers', color='#ff7f00')
ax.barh(y, comics, height, left=np.add(np.add(books, magazines), newspapers), label='Comics', color='#984ea3')

# Add some text for labels and custom y-axis tick labels
ax.set_xlabel('Sales (Units)')
ax.set_title('Monthly Sales of Reading Materials', pad=20)
ax.set_yticks(y)
ax.set_yticklabels(months)
ax.legend(loc='lower right', bbox_to_anchor=(1.35, 0.5))

# Assign numerical label of each bar
for i in range(len(months)):
    plt.text(books[i]/2, i, str(books[i]), ha='center', va='center', color='white')
    plt.text(books[i] + magazines[i]/2, i, str(magazines[i]), ha='center', va='center', color='white')
    plt.text(books[i] + magazines[i] + newspapers[i]/2, i, str(newspapers[i]), ha='center', va='center', color='white')
    plt.text(books[i] + magazines[i] + newspapers[i] + comics[i]/2, i, str(comics[i]), ha='center', va='center', color='white')

plt.show()