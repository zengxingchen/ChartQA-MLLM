
import matplotlib.pyplot as plt

# Data
years = ['2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031']
new_york = [800, 850, 870, 900, 920, 950, 980, 1000, 1030, 1050, 1080]
los_angeles = [600, 620, 640, 660, 680, 700, 720, 740, 760, 780, 800]
chicago = [400, 420, 440, 460, 480, 500, 520, 540, 560, 580, 600]

# Colors
colors_ny = ['#FF5733', '#C70039', '#900C3F', '#581845', '#DAF7A6', '#FFC300', '#FF5733', '#C70039', '#900C3F', '#581845', '#DAF7A6']
colors_la = ['#3498DB', '#2ECC71', '#9B59B6', '#E74C3C', '#F1C40F', '#34495E', '#1ABC9C', '#E67E22', '#7D3C98', '#5DADE2', '#AF7AC5']
colors_ch = ['#2874A6', '#1F618D', '#2ECC71', '#D4AC0D', '#F1C40F', '#2C3E50', '#1ABC9C', '#E67E22', '#E74C3C', '#3498DB', '#7D3C98']

# Plot
fig, ax = plt.subplots(figsize=(10, 12))

bar_height = 0.6

bars_ny = plt.barh(years, new_york, color=colors_ny, edgecolor='white', height=bar_height, label='New York')
bars_la = plt.barh(years, los_angeles, left=new_york, color=colors_la, edgecolor='white', height=bar_height, label='Los Angeles')
bars_ch = plt.barh(years, chicago, left=[i+j for i,j in zip(new_york, los_angeles)], color=colors_ch, edgecolor='white', height=bar_height, label='Chicago')

# Adding labels and title
plt.xlabel('Number of Tourists (in thousands)')
plt.title('Annual Tourist Visits to Major Cities', pad=20)

# Adding numerical labels
for bar in bars_ny:
    width = bar.get_width()
    ax.text(width / 2, bar.get_y() + bar.get_height() / 2, '%d' % int(width), ha='center', va='center', color='white', fontsize=8)
for bar in bars_la:
    width = bar.get_width() + bar.get_x()
    ax.text(width - bar.get_width() / 2, bar.get_y() + bar.get_height() / 2, '%d' % int(width - bar.get_x()), ha='center', va='center', color='white', fontsize=8)
for bar in bars_ch:
    width = bar.get_width() + bar.get_x()
    ax.text(width - bar.get_width() / 2, bar.get_y() + bar.get_height() / 2, '%d' % int(width - bar.get_x()), ha='center', va='center', color='white', fontsize=8)

# Customizing the axes
plt.xlim(0, 3000)

# Adding legend
plt.legend(loc='upper right')

# Display the plot
plt.show()