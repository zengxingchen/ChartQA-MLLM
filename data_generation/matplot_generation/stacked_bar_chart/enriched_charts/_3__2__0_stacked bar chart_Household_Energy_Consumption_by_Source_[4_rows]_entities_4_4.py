
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
research = [10000, 12000, 14000, 16000, 18000, 20000, 22000, 24000, 26000, 28000, 30000, 32000]
development = [15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000]
testing = [12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000]
deployment = [5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000]

fig, ax = plt.subplots(figsize=(10, 8))

bar_height = 0.6

# Plotting data
p1 = ax.barh(months, research, bar_height, color='#1f77b4', label='Research')
p2 = ax.barh(months, development, bar_height, left=research, color='#ff7f0e', label='Development')
p3 = ax.barh(months, testing, bar_height, left=[i+j for i,j in zip(research, development)], color='#2ca02c', label='Testing')
p4 = ax.barh(months, deployment, bar_height, left=[i+j+k for i,j,k in zip(research, development, testing)], color='#d62728', label='Deployment')

ax.set_xlabel('Hours')
ax.set_title('Monthly Software Project Hours Distribution', pad=20)
ax.legend(loc='lower right')

# Customize the grid
plt.grid(which='major', linestyle='--', linewidth='0.5', color='gray')

# Add numerical labels
for rects in [p1, p2, p3, p4]:
    for rect in rects:
        width = rect.get_width()
        ax.annotate(f'{width}',
                    xy=(rect.get_x() + width / 2, rect.get_y() + rect.get_height() / 2),
                    xytext=(0, 0),
                    textcoords="offset points",
                    ha='center', va='center', fontsize=8)

plt.show()