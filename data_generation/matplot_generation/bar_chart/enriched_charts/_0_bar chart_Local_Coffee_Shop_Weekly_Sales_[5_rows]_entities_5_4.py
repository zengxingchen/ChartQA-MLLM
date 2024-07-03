
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
total_sales = [200, 180, 220, 240, 210, 230, 200, 250, 260, 240, 230, 220]

# Color scheme using color codes
colors = ['#FF5733', '#C70039', '#900C3F', '#571845', '#27AE60', '#2980B9',
          '#8E44AD', '#3498DB', '#2ECC71', '#F1C40F', '#E67E22', '#E74C3C']

# Create horizontal bar chart
plt.figure(figsize=(14, 8))
bars = plt.barh(months, total_sales, color=colors, height=0.6)

# Adjusting the width and height of bars
for bar in bars:
    bar.set_height(0.5)

# Changing the layout and labels
plt.xlabel('Total Sales', fontsize=12)
plt.title('Monthly Sales Data for a Retail Store', fontsize=16)
plt.xlim(0, max(total_sales) * 1.1)  # Set x-axis limit higher to accommodate labels

# Adding value labels next to each bar
for i, v in enumerate(total_sales):
    plt.text(v + 3, i - 0.1, str(v), color='black', va='center', fontsize=11)

# Show the final result
plt.tight_layout()
plt.show()