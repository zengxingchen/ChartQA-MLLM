
import matplotlib.pyplot as plt

# Data for the stacked area chart
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
person_a = [12000, 13000, 14000, 15000, 15500, 16000, 16500, 17000, 17500, 18000, 18500, 19000]
person_b = [15000, 15500, 16000, 16500, 17000, 17500, 18000, 18500, 19000, 19500, 20000, 20500]
person_c = [8000, 8200, 8400, 8600, 8800, 9000, 9200, 9400, 9600, 9800, 10000, 10200]

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(12, 8)) # Modify figure size
ax.stackplot(months, person_a, person_b, person_c, colors=['#FF6347', '#4682B4', '#32CD32'])

# Customize the chart with a title and labels
ax.set_title('Monthly Steps Taken by Different Individuals', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Steps Taken', fontsize=14)

# Assign annotation/text label on the chart.
for i in range(len(months)):
    total_steps = person_a[i] + person_b[i] + person_c[i]
    ax.text(i, total_steps, f"{total_steps:,}", ha='center', va='bottom')

# Show the figure
plt.tight_layout()
plt.show()