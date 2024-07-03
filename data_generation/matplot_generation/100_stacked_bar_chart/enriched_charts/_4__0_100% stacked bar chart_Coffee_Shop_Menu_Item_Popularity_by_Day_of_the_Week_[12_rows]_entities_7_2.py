import matplotlib.pyplot as plt

# Data for each quarter
Q1 = [25, 50, 25]
Q2 = [30, 50, 20]
Q3 = [35, 40, 25]
Q4 = [40, 35, 25]
Q5 = [45, 30, 25]
Q6 = [50, 25, 25]
Q7 = [30, 45, 25]
Q8 = [35, 40, 25]

quarters = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8']
products = ['Product A', 'Product B', 'Product C']

# Accumulate the values for stacked bar chart
product_A = [Q1[0], Q2[0], Q3[0], Q4[0], Q5[0], Q6[0], Q7[0], Q8[0]]
product_B = [Q1[1], Q2[1], Q3[1], Q4[1], Q5[1], Q6[1], Q7[1], Q8[1]]
product_C = [Q1[2], Q2[2], Q3[2], Q4[2], Q5[2], Q6[2], Q7[2], Q8[2]]

# Calculate the cumulative bottom starting positions for each bar
product_B_bottom = [i for i in product_A]
product_C_bottom = [product_A[i] + product_B[i] for i in range(len(product_B))]

fig, ax = plt.subplots(figsize=(10, 8))  # change the figure size

# Plotting
bar_width = 0.75  # Change the width of the bars

ax.bar(quarters, product_A, color='#FF5733', edgecolor='white', width=bar_width, label='Product A')
ax.bar(quarters, product_B, bottom=product_B_bottom, color='#33FF57', edgecolor='white', width=bar_width, label='Product B')
ax.bar(quarters, product_C, bottom=product_C_bottom, color='#3357FF', edgecolor='white', width=bar_width, label='Product C')

# Add some text for labels and custom y-axis tick labels, etc.
ax.set_ylabel('Percentage')
ax.set_title('Market Share by Product and Quarter')
ax.set_yticks([0, 25, 50, 75, 100])
ax.set_yticklabels(['0%', '25%', '50%', '75%', '100%'])

ax.legend()

# Display the plot
plt.show()