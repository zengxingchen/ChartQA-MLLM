
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030']
fruits = [200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500]
vegetables = [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]
dairy = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250]

# Plot
fig, ax = plt.subplots(figsize=(14, 10))

ax.bar(years, fruits, color='#FF6347', edgecolor='white', width=0.6, label='Fruits')
ax.bar(years, vegetables, bottom=fruits, color='#3CB371', edgecolor='white', width=0.6, label='Vegetables')
ax.bar(years, dairy, bottom=[i + j for i, j in zip(fruits, vegetables)], color='#1E90FF', edgecolor='white', width=0.6, label='Dairy')

# Labels and Title
ax.set_ylabel('Annual Revenue (in Millions)')
ax.set_title('Annual Revenue from Different Food Categories (2015-2030)', pad=20)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Numerical Labels
for i in range(len(years)):
    ax.text(i, fruits[i] / 2, str(fruits[i]), ha='center', va='center', color='white', fontweight='bold')
    ax.text(i, fruits[i] + vegetables[i] / 2, str(vegetables[i]), ha='center', va='center', color='white', fontweight='bold')
    ax.text(i, fruits[i] + vegetables[i] + dairy[i] / 2, str(dairy[i]), ha='center', va='center', color='white', fontweight='bold')

# Display the plot
plt.tight_layout()
plt.show()