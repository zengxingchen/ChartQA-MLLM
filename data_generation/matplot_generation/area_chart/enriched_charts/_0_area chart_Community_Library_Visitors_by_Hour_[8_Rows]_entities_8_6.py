
import matplotlib.pyplot as plt

# Data
months = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]
revenue = [
    12000, 13500, 15000, 16000, 15500, 14500,
    15000, 15500, 16000, 16500, 17000, 20000
]

# Plot
fig, ax = plt.subplots(figsize=(12, 6))  # Modify width (12) and height (6) of the chart
ax.fill_between(months, revenue, color='#3498db', alpha=0.5)  # Fill with a specific color code

# Style
ax.set_title('Monthly Revenue in 2023', fontsize=18)  # Changing the title
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Revenue ($)', fontsize=14)
ax.set_ylim(0, max(revenue) + 5000)  # Set the y-axis limit to give some space at the top
ax.margins(x=0)  # Remove the white space on the x-axis edges
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Annotation
peak_revenue = max(revenue)
peak_month = months[revenue.index(peak_revenue)]
ax.annotate(f'Peak Revenue: ${peak_revenue}', xy=(peak_month, peak_revenue), xytext=(5, 20),
            textcoords='offset points', arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.5"))

plt.show()