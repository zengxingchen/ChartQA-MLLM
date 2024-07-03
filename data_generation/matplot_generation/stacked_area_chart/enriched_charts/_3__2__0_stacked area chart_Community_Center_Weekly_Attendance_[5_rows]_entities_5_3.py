
import matplotlib.pyplot as plt

# Data for the stacked area chart
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
person_a = [11000, 11500, 12000, 12500, 13000, 13500, 14000, 14500, 15000, 15500, 16000, 16500]
person_b = [14000, 14500, 15000, 15500, 16000, 16500, 17000, 17500, 18000, 18500, 19000, 19500]
person_c = [9000, 9500, 9800, 10000, 10500, 11000, 11500, 12000, 12500, 13000, 13500, 14000]

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(14, 10)) # Modify figure size
ax.stackplot(months, person_a, person_b, person_c, colors=['#FF5733', '#33FF57', '#3357FF'], labels=['Person A', 'Person B', 'Person C'])

# Customize the chart with a title and labels
ax.set_title('Monthly Calories Burned by Different Individuals', fontsize=18, fontweight='bold', pad=25)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Calories Burned', fontsize=14)

# Assign annotation/text label on the chart.
for i in range(len(months)):
    total_steps = person_a[i] + person_b[i] + person_c[i]
    ax.text(i, total_steps, f"{total_steps:,}", ha='center', va='bottom')

# Add legend
ax.legend(loc='upper left')

# Show the figure
plt.tight_layout()
plt.show()