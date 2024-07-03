
import matplotlib.pyplot as plt
import pandas as pd

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
ancient_artifacts = [5000, 6000, 7000, 8000, 8500, 9000, 9500, 10000, 10500, 11000, 11500, 12000]
medieval_relics = [3000, 3200, 3500, 3700, 4000, 4300, 4500, 4800, 5000, 5300, 5500, 5800]
modern_exhibits = [7000, 7100, 7200, 7300, 7500, 7600, 7800, 7900, 8000, 8200, 8300, 8500]

fig, ax = plt.subplots(figsize=(16, 10))
ax.stackplot(months, ancient_artifacts, medieval_relics, modern_exhibits, colors=['#FF5733', '#33FF57', '#3357FF'])

ax.set_title('Monthly Museum Visitors (in Thousands)', fontsize=20, fontweight='bold', pad=20)
ax.set_xlabel('Month', fontsize=16)
ax.set_ylabel('Number of Visitors', fontsize=16)

for i in range(len(months)):
    total_visitors = ancient_artifacts[i] + medieval_relics[i] + modern_exhibits[i]
    ax.text(i, total_visitors, f"{total_visitors:,}", ha='center', va='bottom')

plt.tight_layout()
plt.show()