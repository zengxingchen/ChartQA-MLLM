
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030']
running = [500, 600, 700, 800, 850, 900, 950, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800]
swimming = [300, 320, 350, 370, 400, 430, 460, 490, 520, 550, 580, 610, 640, 670, 700, 730]
cycling = [150, 180, 200, 220, 250, 270, 290, 310, 330, 360, 380, 400, 420, 450, 470, 490]

# Plot
fig, ax = plt.subplots(figsize=(14, 10))

ax.bar(years, running, color='#FF5733', edgecolor='white', width=0.7, label='Running')
ax.bar(years, swimming, bottom=running, color='#33FF57', edgecolor='white', width=0.7, label='Swimming')
ax.bar(years, cycling, bottom=[i + j for i, j in zip(running, swimming)], color='#3357FF', edgecolor='white', width=0.7, label='Cycling')

# Labels and Title
ax.set_ylabel('Number of Participants')
ax.set_title('Annual Participation in Different Sports Activities (2015-2030)', pad=20)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Display the plot
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()