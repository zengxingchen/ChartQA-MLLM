
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
USA = [2200, 2500, 2800, 2600, 3000, 3200, 3400, 3300, 3200, 3000, 2900, 3100]
Canada = [1800, 1900, 2100, 2000, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900]
Mexico = [1500, 1400, 1600, 1700, 1900, 1800, 2000, 2100, 1900, 2200, 2100, 2200]
Brazil = [1300, 1200, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300]

bar_width = 0.35
indices = range(len(months))

fig, ax = plt.subplots(figsize=(10, 12))

ax.bar(indices, USA, width=bar_width, color='#1f78b4', label='USA')
ax.bar([i + bar_width for i in indices], Canada, width=bar_width, color='#33a02c', label='Canada')
ax.bar([i + 2 * bar_width for i in indices], Mexico, width=bar_width, color='#e31a1c', label='Mexico')
ax.bar([i + 3 * bar_width for i in indices], Brazil, width=bar_width, color='#ff7f00', label='Brazil')

ax.set_ylabel('Energy Consumption (TWh)')
ax.set_title('Monthly Energy Consumption by Country')
ax.set_xticks([i + 1.5 * bar_width for i in indices])
ax.set_xticklabels(months)
ax.legend(loc='upper left')

for spine in ax.spines.values():
    spine.set_visible(False)

ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

for i, v in enumerate(USA):
    ax.text(i, v + 100, str(v), ha='center', va='bottom')
for i, v in enumerate(Canada):
    ax.text(i + bar_width, v + 100, str(v), ha='center', va='bottom')
for i, v in enumerate(Mexico):
    ax.text(i + 2 * bar_width, v + 100, str(v), ha='center', va='bottom')
for i, v in enumerate(Brazil):
    ax.text(i + 3 * bar_width, v + 100, str(v), ha='center', va='bottom')

plt.tight_layout()
plt.show()