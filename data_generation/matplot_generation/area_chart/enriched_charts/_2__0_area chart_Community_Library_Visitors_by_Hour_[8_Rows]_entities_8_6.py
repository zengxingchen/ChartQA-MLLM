
import matplotlib.pyplot as plt

# Data
months = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]
running_distance = [
    120, 130, 145, 150, 160, 155,
    165, 170, 180, 190, 200, 210
]

# Plot
fig, ax = plt.subplots(figsize=(14, 8))
ax.fill_between(months, running_distance, color='#ff5733', alpha=0.6)

# Style
ax.set_title('Monthly Running Distance in 2023', fontsize=20, pad=20)
ax.set_xlabel('Month', fontsize=16)
ax.set_ylabel('Running Distance (km)', fontsize=16)
ax.set_ylim(0, max(running_distance) + 50)
ax.margins(x=0)
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Annotation
peak_distance = max(running_distance)
peak_month = months[running_distance.index(peak_distance)]
ax.annotate(f'Peak Distance: {peak_distance} km', xy=(peak_month, peak_distance), xytext=(5, 30),
            textcoords='offset points', arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.5"))

plt.show()