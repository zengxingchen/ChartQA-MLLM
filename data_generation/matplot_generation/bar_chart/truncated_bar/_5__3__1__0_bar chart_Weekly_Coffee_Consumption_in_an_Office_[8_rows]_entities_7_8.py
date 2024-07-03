
import matplotlib.pyplot as plt

categories = ["Artificial Intelligence", "Quantum Computing", "Biotechnology", "Renewable Energy", "Space Exploration", "Nanotechnology", "Cybersecurity", "Robotics", "Virtual Reality", "3D Printing"]
percentages = [85, 75, 65, 55, 70, 60, 80, 78, 50, 40]

fig, ax = plt.subplots(figsize=(10, 12))

bars = ax.bar(categories, percentages, width=0.5, color=['#FF6347', '#4682B4', '#3CB371', '#FFD700', '#8A2BE2', '#A52A2A', '#DC143C', '#00CED1', '#FF4500', '#2E8B57'])

ax.set_title('Key Future Technologies Impacting Society', fontsize=20, pad=30)
ax.set_ylabel('Percentage (%)', fontsize=16)
ax.set_xlabel('Category', fontsize=16)

ax.yaxis.set_tick_params(labelsize=14)
ax.xaxis.set_tick_params(labelsize=14)

ax.set_ylim(30, 90)  # Setting y-axis limits to truncate the chart

for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 1, f'{height}%', va='bottom', ha='center', fontsize=12)

plt.tight_layout()
plt.show()