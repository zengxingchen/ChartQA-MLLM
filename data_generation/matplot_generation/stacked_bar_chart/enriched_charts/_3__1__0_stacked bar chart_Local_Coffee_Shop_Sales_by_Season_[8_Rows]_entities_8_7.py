
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030']
reading = [200, 250, 270, 300, 320, 350, 380, 400, 420, 450, 480, 500, 530, 550, 580, 600]
writing = [150, 170, 190, 220, 240, 260, 290, 310, 340, 360, 390, 410, 440, 460, 490, 510]
debating = [100, 120, 150, 170, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420]
researching = [180, 210, 230, 250, 270, 300, 330, 350, 370, 400, 430, 450, 480, 500, 530, 550]

# Plot
fig, ax = plt.subplots(figsize=(16, 12))

ax.barh(years, reading, color='#FF9999', edgecolor='white', height=0.7, label='Reading')
ax.barh(years, writing, left=reading, color='#99FF99', edgecolor='white', height=0.7, label='Writing')
ax.barh(years, debating, left=[i + j for i, j in zip(reading, writing)], color='#9999FF', edgecolor='white', height=0.7, label='Debating')
ax.barh(years, researching, left=[i + j + k for i, j, k in zip(reading, writing, debating)], color='#FFCC99', edgecolor='white', height=0.7, label='Researching')

# Labels and Title
ax.set_xlabel('Number of Participants')
ax.set_title('Annual Participation in Literary Activities (2015-2030)', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1))

# Display the plot
plt.yticks(rotation=45)
plt.tight_layout()
plt.show()