
import matplotlib.pyplot as plt
import numpy as np

# Data
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
reading = [3, 4, 2, 3, 2, 1, 1]
writing = [2, 3, 3, 2, 3, 1, 2]
math = [3, 2, 3, 3, 4, 2, 2]
science = [2, 3, 4, 3, 2, 2, 1]
history = [1, 2, 2, 3, 1, 2, 3]
art = [1, 2, 1, 2, 3, 3, 2]
pe = [2, 1, 1, 2, 1, 4, 3]

# Normalize data to sum up to 100%
total = [read + write + m + sci + his + a + p for read, write, m, sci, his, a, p in zip(reading, writing, math, science, history, art, pe)]
reading = np.array(reading) / total * 100
writing = np.array(writing) / total * 100
math = np.array(math) / total * 100
science = np.array(science) / total * 100
history = np.array(history) / total * 100
art = np.array(art) / total * 100
pe = np.array(pe) / total * 100

fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.5

# Plotting
bars1 = ax.bar(days, reading, width=bar_width, color='#1f77b4', edgecolor='white', label='Reading')
bars2 = ax.bar(days, writing, width=bar_width, bottom=reading, color='#ff7f0e', edgecolor='white', label='Writing')
bars3 = ax.bar(days, math, width=bar_width, bottom=reading + writing, color='#2ca02c', edgecolor='white', label='Math')
bars4 = ax.bar(days, science, width=bar_width, bottom=reading + writing + math, color='#d62728', edgecolor='white', label='Science')
bars5 = ax.bar(days, history, width=bar_width, bottom=reading + writing + math + science, color='#9467bd', edgecolor='white', label='History')
bars6 = ax.bar(days, art, width=bar_width, bottom=reading + writing + math + science + history, color='#8c564b', edgecolor='white', label='Art')
bars7 = ax.bar(days, pe, width=bar_width, bottom=reading + writing + math + science + history + art, color='#e377c2', edgecolor='white', label='PE')

# Customizing the plot
ax.set_ylabel('Percentage of Time Spent')
ax.set_title('Weekly Study Routine Distribution')
ax.legend(loc='upper right')

# Display the chart
plt.tight_layout()
plt.show()