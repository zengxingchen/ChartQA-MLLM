
import matplotlib.pyplot as plt
import pandas as pd

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
ancient_artifacts = [4800, 5900, 6800, 7600, 8200, 8700, 9200, 9600, 10000, 10400, 10800, 11200]
medieval_relics = [3100, 3200, 3400, 3600, 3800, 4000, 4200, 4400, 4600, 4800, 5000, 5200]
modern_exhibits = [6500, 6700, 6900, 7100, 7300, 7500, 7700, 7900, 8100, 8300, 8500, 8700]

fig, ax = plt.subplots(figsize=(18, 12))
ax.stackplot(months, ancient_artifacts, medieval_relics, modern_exhibits, colors=['#FF5733', '#33A2FF', '#33FF99'])

ax.set_title('Monthly Museum Visitors (in Thousands)', fontsize=22, fontweight='bold', pad=30)
ax.set_xlabel('Month', fontsize=18)
ax.set_ylabel('Number of Visitors', fontsize=18)

for i in range(len(months)):
    total_visitors = ancient_artifacts[i] + medieval_relics[i] + modern_exhibits[i]
    ax.text(i, total_visitors, f"{total_visitors:,}", ha='center', va='bottom')

plt.legend(['Ancient Artifacts', 'Medieval Relics', 'Modern Exhibits'], loc='upper left')
plt.tight_layout()
plt.show()