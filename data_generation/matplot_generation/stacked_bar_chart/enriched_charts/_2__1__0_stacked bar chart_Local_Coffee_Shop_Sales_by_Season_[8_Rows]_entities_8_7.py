
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030']
technology = [800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550]
finance = [700, 740, 780, 820, 860, 900, 940, 980, 1020, 1060, 1100, 1140, 1180, 1220, 1260, 1300]
healthcare = [600, 630, 660, 690, 720, 750, 780, 810, 840, 870, 900, 930, 960, 990, 1020, 1050]

# Plot
fig, ax = plt.subplots(figsize=(10, 14))

ax.barh(years, technology, color='#1f77b4', edgecolor='white', height=0.6, label='Technology')
ax.barh(years, finance, left=technology, color='#ff7f0e', edgecolor='white', height=0.6, label='Finance')
ax.barh(years, healthcare, left=[i + j for i, j in zip(technology, finance)], color='#2ca02c', edgecolor='white', height=0.6, label='Healthcare')

# Labels and Title
ax.set_xlabel('Annual Revenue (in Millions)')
ax.set_title('Annual Revenue from Different Sectors (2015-2030)', pad=20)
ax.legend(loc='lower right', bbox_to_anchor=(1, 0))

# Numerical Labels
for i in range(len(years)):
    ax.text(technology[i] / 2, i, str(technology[i]), ha='center', va='center', color='white', fontweight='bold')
    ax.text(technology[i] + finance[i] / 2, i, str(finance[i]), ha='center', va='center', color='white', fontweight='bold')
    ax.text(technology[i] + finance[i] + healthcare[i] / 2, i, str(healthcare[i]), ha='center', va='center', color='white', fontweight='bold')

# Display the plot
plt.tight_layout()
plt.show()