
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
revenue = [450, 380, 510, 490, 520, 480, 460, 550, 570, 590, 530, 510]

# Color scheme using specific color codes
colors = ['#3366CC', '#DC3912', '#FF9900', '#109618', '#990099', '#3B3EAC', 
          '#0099C6', '#DD4477', '#66AA00', '#B82E2E', '#316395', '#994499']

# Create vertical bar chart
plt.figure(figsize=(12, 7))
bars = plt.bar(months, revenue, color=colors, width=0.7)

# Adjusting the width and height of bars
for bar in bars:
    bar.set_width(0.6)

# Changing the layout and labels
plt.ylabel('Revenue ($)', fontsize=12)
plt.title('Monthly Revenue Data for a Fashion Store', fontsize=16)
plt.ylim(0, max(revenue) * 1.1)  # Set y-axis limit higher to accommodate labels

# Adding value labels above each bar
for i, v in enumerate(revenue):
    plt.text(i, v + 20, str(v), color='black', ha='center', fontsize=11)

# Show the final result
plt.tight_layout()
plt.show()