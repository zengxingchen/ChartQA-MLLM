
import matplotlib.pyplot as plt

# Data
months = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]
audience = [
    5000, 6200, 8000, 7200, 9000, 8500,
    9500, 10000, 10800, 11500, 12000, 13000
]

# Plot
fig, ax = plt.subplots(figsize=(14, 7))  # Modify width (14) and height (7) of the chart
ax.fill_between(months, audience, color='#8e44ad', alpha=0.6)  # Fill with a specific color code

# Style
ax.set_title('Monthly Audience Growth in 2023', fontsize=20)  # Changing the title
ax.set_xlabel('Month', fontsize=16)
ax.set_ylabel('Audience Count', fontsize=16)
ax.set_ylim(0, max(audience) + 3000)  # Set the y-axis limit to give some space at the top
ax.margins(x=0)  # Remove the white space on the x-axis edges
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Annotation
peak_audience = max(audience)
peak_month = months[audience.index(peak_audience)]
ax.annotate(f'Peak Audience: {peak_audience}', xy=(peak_month, peak_audience), xytext=(5, 20),
            textcoords='offset points', arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.5"))

plt.show()