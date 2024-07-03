
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Day': list(range(1, 31)),
    'Steps': [5000, 7000, 6500, 8000, 7200, 7500, 8200, 8400, 7900, 8100, 8800, 8600, 9000, 9400, 9200, 9500, 9300, 9700, 9400, 9100, 9500, 9300, 9600, 9900, 9700, 10000, 9800, 9600, 10200, 10400]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(14, 9))
plt.fill_between(df['Day'], df['Steps'], color='#1f77b4', alpha=0.7)
plt.plot(df['Day'], df['Steps'], color='#ff7f0e', linewidth=2)

# Title and labels
plt.title('Daily Steps Over a Month', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Day', fontsize=14)
plt.ylabel('Steps', fontsize=14)

# Annotation
max_steps = df['Steps'].max()
max_day = df['Day'][df['Steps'].idxmax()]
plt.annotate(f'Highest: {max_steps}', xy=(max_day, max_steps), xytext=(max_day+2, max_steps+500),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)

# Grid and legend
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend(['Daily Steps'], loc='upper left')

plt.show()