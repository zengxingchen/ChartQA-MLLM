
import matplotlib.pyplot as plt

# Data
months = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]
article_count = [
    25, 30, 35, 45, 50, 60,
    55, 65, 70, 80, 75, 90
]

# Plot
fig, ax = plt.subplots(figsize=(16, 10))
ax.fill_between(months, article_count, color='#007acc', alpha=0.6)

# Style
ax.set_title('Monthly Article Count in 2023', fontsize=22, pad=25)
ax.set_xlabel('Month', fontsize=18)
ax.set_ylabel('Number of Articles', fontsize=18)
ax.set_ylim(0, max(article_count) + 20)
ax.margins(x=0)
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Annotation
peak_articles = max(article_count)
peak_month = months[article_count.index(peak_articles)]
ax.annotate(f'Peak: {peak_articles} articles', xy=(peak_month, peak_articles), xytext=(5, 30),
            textcoords='offset points', arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.5"))

plt.show()