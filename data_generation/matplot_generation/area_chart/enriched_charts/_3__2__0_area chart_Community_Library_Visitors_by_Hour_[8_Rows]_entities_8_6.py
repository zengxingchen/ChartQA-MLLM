import matplotlib.pyplot as plt

# Data
months = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]
reading_pages = [
    50, 75, 100, 125, 150, 175,
    200, 225, 250, 275, 300, 325
]

# Plot
fig, ax = plt.subplots(figsize=(16, 10))
ax.fill_between(months, reading_pages, color='#1f77b4', alpha=0.6)

# Style
ax.set_title('Monthly Reading Progress in 2023', fontsize=22, pad=30)
ax.set_xlabel('Month', fontsize=18)
ax.set_ylabel('Reading Progress (pages)', fontsize=18)
ax.set_ylim(0, max(reading_pages) + 50)
ax.margins(x=0)
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Annotation
peak_pages = max(reading_pages)
peak_month = months[reading_pages.index(peak_pages)]
ax.annotate(f'Peak Reading: {peak_pages} pages', xy=(peak_month, peak_pages), xytext=(20, 40),
            textcoords='offset points', arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.5"))

plt.show()