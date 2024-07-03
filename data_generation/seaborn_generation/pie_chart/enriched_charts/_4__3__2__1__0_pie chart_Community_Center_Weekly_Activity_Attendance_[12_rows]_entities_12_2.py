
import matplotlib.pyplot as plt

categories = ['Education', 'Healthcare', 'Infrastructure', 'Defense', 'Research', 'Social Services', 'Others']
percentages = [15, 25, 20, 10, 10, 10, 10]
colors = ['#ff6666', '#ffcc99', '#66b3ff', '#99ff99', '#ffb3e6', '#c2c2f0', '#ffb366']

fig, ax = plt.subplots(figsize=(10, 6))
ax.pie(percentages, labels=categories, autopct='%1.1f%%', colors=colors, startangle=140)
ax.set_title('Government Budget Allocation', pad=20)

plt.show()