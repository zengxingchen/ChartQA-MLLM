import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
category_a = [80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135]
category_b = [90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145]
category_c = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210]

# Plot setup
fig, ax = plt.subplots(figsize=(10, 10))

# Stacked bar chart (vertical)
bar_width = 0.6
plt.bar(months, category_a, color='#FF6347', edgecolor='white', width=bar_width, label='Category A')
plt.bar(months, category_b, bottom=category_a, color='#4682B4', edgecolor='white', width=bar_width, label='Category B')
plt.bar(months, category_c, bottom=[i+j for i,j in zip(category_a, category_b)], color='#32CD32', edgecolor='white', width=bar_width, label='Category C')

# Labels, title and legend
plt.ylabel('Values')
plt.title('Monthly Distribution of Categories A, B, and C')
plt.legend(loc='upper right')

# Numerical labels for each bar
for i in range(len(months)):
    plt.text(i, category_a[i] / 2, str(category_a[i]), ha='center', va='center', color='white', fontweight='bold')
    plt.text(i, category_a[i] + (category_b[i] / 2), str(category_b[i]), ha='center', va='center', color='white', fontweight='bold')
    plt.text(i, category_a[i] + category_b[i] + (category_c[i] / 2), str(category_c[i]), ha='center', va='center', color='white', fontweight='bold')

# Show the plot
plt.show()