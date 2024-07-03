
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June']
fruits = [120, 110, 130, 140, 115, 125]
vegetables = [100, 90, 95, 105, 100, 110]
dairy = [80, 85, 78, 82, 88, 90]
meat = [140, 135, 145, 150, 155, 160]
grains = [60, 70, 75, 65, 80, 85]

# Stacked Bar Chart
fig, ax = plt.subplots(figsize=(8, 10))  # changing width and height of the chart

bar_height = 0.5  # change height of bars
index = range(len(months))

p1 = plt.bar(index, fruits, bar_height, label='Fruits', color='#FF6347')
p2 = plt.bar(index, vegetables, bar_height, bottom=fruits, label='Vegetables', color='#32CD32')
p3 = plt.bar(index, dairy, bar_height, bottom=[f + v for f, v in zip(fruits, vegetables)], label='Dairy', color='#FFD700')
p4 = plt.bar(index, meat, bar_height, bottom=[f + v + d for f, v, d in zip(fruits, vegetables, dairy)], label='Meat', color='#8A2BE2')
p5 = plt.bar(index, grains, bar_height, bottom=[f + v + d + m for f, v, d, m in zip(fruits, vegetables, dairy, meat)], label='Grains', color='#00CED1')

plt.ylabel('Months')
plt.xticks(index, months)
plt.title('Monthly Food Expenses', pad=20)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), shadow=True, ncol=3)

# Customizing the grid
plt.grid(axis='y')

# Adding numerical labels
for i in index:
    total = fruits[i] + vegetables[i] + dairy[i] + meat[i] + grains[i]
    plt.text(i, total + 5, str(total), ha='center', va='bottom')

plt.show()