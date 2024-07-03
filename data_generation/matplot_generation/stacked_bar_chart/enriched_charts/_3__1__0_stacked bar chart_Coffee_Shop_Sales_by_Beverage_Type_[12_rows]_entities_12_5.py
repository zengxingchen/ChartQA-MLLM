
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
painting = [8000, 9500, 10500, 12000, 13000, 14500, 16000]
music = [12000, 13500, 15000, 16500, 18000, 19500, 21000]
writing = [10000, 11000, 12500, 14000, 15500, 17000, 18500]
dancing = [5000, 6000, 7000, 8000, 9000, 10000, 11000]

# Plot
fig, ax = plt.subplots(figsize=(14, 8))  # Change width and height of the chart

ax.barh(years, painting, color='#4B0082', edgecolor='white', height=0.5)
ax.barh(years, music, left=painting, color='#FF4500', edgecolor='white', height=0.5)
ax.barh(years, writing, left=[i+j for i,j in zip(painting, music)], color='#FFD700', edgecolor='white', height=0.5)
ax.barh(years, dancing, left=[i+j+k for i,j,k in zip(painting, music, writing)], color='#32CD32', edgecolor='white', height=0.5)

for index, (p, m, w, d) in enumerate(zip(painting, music, writing, dancing)):
    ax.text(p / 2, index, str(p), va='center', ha='center', color='white', fontweight='bold')
    ax.text(p + m / 2, index, str(m), va='center', ha='center', color='white', fontweight='bold')
    ax.text(p + m + w / 2, index, str(w), va='center', ha='center', color='white', fontweight='bold')
    ax.text(p + m + w + d / 2, index, str(d), va='center', ha='center', color='white', fontweight='bold')

ax.set_xlabel('Number of Participants')
ax.set_title('Participation in Arts & Music from 2015 to 2021', pad=20)
ax.set_yticks(years)
ax.set_xlim(0, 75000)  # Adjust to accommodate the sum of the data points

plt.show()