import matplotlib.pyplot as plt

royalties = [
    5000, 6000, 6200, 6800, 7200, 7600, 8000, 8200, 8500, 8800, 9200, 9500, 9800, 10000, 
    10300, 10700, 11000, 11300, 11500, 11800, 12200, 12500, 12700, 13000, 13300, 13600, 
    14000, 14200, 14500, 14800, 15200, 15500, 15800, 16000, 16300, 16500, 16800, 17200, 
    17500, 17800, 18200, 18500, 18800, 19200, 19500, 19800, 20000, 20300, 20500, 20800, 
    21200, 21500, 21700, 22000, 22300, 22700, 23000, 23300, 23500, 23800, 24000, 24500, 
    25000
]

fig, ax = plt.subplots(figsize=(10, 6))
n, bins, patches = ax.hist(royalties, bins=12, orientation='horizontal', color='#2C7BB6', edgecolor='#D7191C', linewidth=1.5)

ax.set_title('Author Royalties Distribution', pad=20)
ax.set_ylabel('Royalties ($)', labelpad=15)
ax.set_xlabel('Number of Authors', labelpad=15)
ax.set_xlim(0, 10)

for i, patch in enumerate(patches):
    patch.set_facecolor(plt.cm.viridis(i / len(patches)))

plt.tight_layout()
plt.show()