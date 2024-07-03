import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
steps = [4000, 4500, 4800, 5000, 5300, 5600, 5900, 6100, 5800, 5500, 5200, 4900]

plt.figure(figsize=(14, 8))
plt.fill_between(months, steps, color='#FF69B4')

plt.title('Monthly Steps Count for Health & Fitness', fontsize=18, pad=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Steps Count', fontsize=14)

highest_steps_idx = steps.index(max(steps))
plt.annotate('Peak Steps', xy=(months[highest_steps_idx], steps[highest_steps_idx]), 
             xytext=(months[highest_steps_idx], steps[highest_steps_idx]+500),
             arrowprops=dict(facecolor='#32CD32', shrink=0.05))

plt.xticks(rotation=45)
plt.yticks(range(0, max(steps)+1000, 1000))
plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()