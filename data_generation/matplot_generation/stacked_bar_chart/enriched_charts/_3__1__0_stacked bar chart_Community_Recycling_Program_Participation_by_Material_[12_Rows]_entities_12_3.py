
import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
math = [15, 25, 20, 18, 22, 30, 28, 35, 30, 25, 20, 15]
science = [20, 15, 22, 24, 17, 10, 18, 20, 22, 25, 15, 10]
english = [10, 18, 15, 12, 14, 20, 22, 18, 25, 20, 17, 10]
history = [12, 10, 17, 20, 19, 15, 16, 22, 20, 18, 10, 8]

bars_science = np.add(math, english).tolist()
bars_history = np.add(bars_science, science).tolist()

colors = ['#3498db', '#2ecc71', '#e74c3c', '#9b59b6']

fig, ax = plt.subplots(figsize=(10, 8))

ax.barh(months, math, color=colors[0], edgecolor='white', height=0.6, label='Math')
ax.barh(months, science, left=math, color=colors[1], edgecolor='white', height=0.6, label='Science')
ax.barh(months, english, left=bars_science, color=colors[2], edgecolor='white', height=0.6, label='English')
ax.barh(months, history, left=bars_history, color=colors[3], edgecolor='white', height=0.6, label='History')

for i, (math_val, sci_val, eng_val, hist_val) in enumerate(zip(math, science, english, history)):
    ax.text(math_val / 2, i, str(math_val), va='center', ha='center', color='black', fontsize=8)
    ax.text(math_val + sci_val / 2, i, str(sci_val), va='center', ha='center', color='black', fontsize=8)
    ax.text(math_val + sci_val + eng_val / 2, i, str(eng_val), va='center', ha='center', color='black', fontsize=8)
    ax.text(math_val + sci_val + eng_val + hist_val / 2, i, str(hist_val), va='center', ha='center', color='black', fontsize=8)

plt.title('Monthly Academic Performance', pad=20)
plt.xlabel('Scores')
plt.ylabel('Month')
plt.xticks(np.arange(0, 101, 10))
plt.legend(loc='lower right')
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.show()