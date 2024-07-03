
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
running = [120, 150, 170, 200, 220, 240, 260, 280, 300, 320, 340, 360]
cycling = [80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]
swimming = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]

fig, ax = plt.subplots(figsize=(16, 12))
ax.stackplot(months, running, cycling, swimming, colors=['#1f77b4', '#ff7f0e', '#2ca02c'])

ax.set_title('Monthly Fitness Activities in 2023', fontsize=20, fontweight='bold', pad=30)
ax.set_xlabel('Month', fontsize=16)
ax.set_ylabel('Hours Spent', fontsize=16)

for i in range(len(months)):
    total_hours = running[i] + cycling[i] + swimming[i]
    ax.text(i, total_hours, f"{total_hours:,}", ha='center', va='bottom', fontsize=10)

plt.legend(['Running', 'Cycling', 'Swimming'], loc='upper left', fontsize=14)
plt.tight_layout()
plt.show()