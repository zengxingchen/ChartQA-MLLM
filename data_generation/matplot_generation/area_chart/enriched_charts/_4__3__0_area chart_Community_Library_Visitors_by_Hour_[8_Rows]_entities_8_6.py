
import matplotlib.pyplot as plt

# Data
days = list(range(1, 32))
steps = [
    2000, 2500, 1800, 3000, 2600, 3100, 2700, 2200, 2900, 2800, 
    3300, 3500, 3400, 3600, 3700, 3800, 3900, 4000, 4100, 4200, 
    4300, 4400, 4500, 4600, 4700, 4800, 4900, 5000, 5100, 5200, 5300
]

# Plot
fig, ax = plt.subplots(figsize=(12, 6))
ax.fill_between(days, steps, color='#1E90FF', alpha=0.7)

# Style
ax.set_title('Daily Step Count in January 2024', fontsize=18, pad=15)
ax.set_xlabel('Day', fontsize=12)
ax.set_ylabel('Steps', fontsize=12)
ax.set_ylim(0, max(steps) + 1000)
ax.margins(x=0)
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Annotation
peak_steps = max(steps)
peak_day = days[steps.index(peak_steps)]
ax.annotate(f'Peak Steps: {peak_steps}', xy=(peak_day, peak_steps), xytext=(5, 20),
            textcoords='offset points', arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.5"))

plt.show()