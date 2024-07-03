
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Q1', 'Q2', 'Q3', 'Q4']
books = [25, 30, 35, 40]
electronics = [15, 20, 30, 35]
clothing = [35, 25, 20, 15]
home = [25, 25, 15, 10]

# Normalize the data
total = np.array(books) + np.array(electronics) + np.array(clothing) + np.array(home)
books_percentage = np.array(books) / total * 100
electronics_percentage = np.array(electronics) / total * 100
clothing_percentage = np.array(clothing) / total * 100
home_percentage = np.array(home) / total * 100

# Plotting
barWidth = 0.5
fig, ax = plt.subplots(figsize=(10, 6))

bar1 = np.add(books_percentage, electronics_percentage).tolist()
bar2 = np.add(bar1, clothing_percentage).tolist()

# Create bars
plt.barh(categories, books_percentage, color='#FF5733', edgecolor='grey', height=barWidth)
plt.barh(categories, electronics_percentage, left=books_percentage, color='#33FF57', edgecolor='grey', height=barWidth)
plt.barh(categories, clothing_percentage, left=bar1, color='#3357FF', edgecolor='grey', height=barWidth)
plt.barh(categories, home_percentage, left=bar2, color='#FF33A1', edgecolor='grey', height=barWidth)

# Add title and labels
plt.xlabel('Percentage')
plt.title('Quarterly Sales Distribution by Category')
plt.legend(['Books', 'Electronics', 'Clothing', 'Home'], loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=4)

plt.show()