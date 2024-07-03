
import matplotlib.pyplot as plt

# Data for each quarter
Q1 = [30, 45, 25]
Q2 = [35, 40, 25]
Q3 = [40, 35, 25]
Q4 = [45, 30, 25]

quarters = ['Q1', 'Q2', 'Q3', 'Q4']
products = ['Product A', 'Product B', 'Product C']

# Accumulate the values for stacked bar chart
product_A = [Q1[0], Q2[0], Q3[0], Q4[0]]
product_B = [Q1[1], Q2[1], Q3[1], Q4[1]]
product_C = [Q1[2], Q2[2], Q3[2], Q4[2]]

# Calculate the cumulative bottom starting positions for each bar
product_B_bottom = [i for i in product_A]
product_C_bottom = [product_A[i] + product_B[i] for i in range(len(product_B))]

fig, ax = plt.subplots(figsize=(8, 6))  # change the figure size

# Plotting
bar_width = 0.35  # Change the height/width of the bars

ax.barh(quarters, product_A, color='#FFA07A', edgecolor='white', height=bar_width, label='Product A')
ax.barh(quarters, product_B, left=product_B_bottom, color='#20B2AA', edgecolor='white', height=bar_width, label='Product B')
ax.barh(quarters, product_C, left=product_C_bottom, color='#778899', edgecolor='white', height=bar_width, label='Product C')

# Add some text for labels and custom x-axis tick labels, etc.
ax.set_xlabel('Percentage')
ax.set_title('Market Share by Product and Quarter')

# Customize the x-ticks to display percentages
ax.set_xticks([0, 25, 50, 75, 100])
ax.set_xticklabels(['0%', '25%', '50%', '75%', '100%'])

ax.legend()

# Display the plot
plt.show()