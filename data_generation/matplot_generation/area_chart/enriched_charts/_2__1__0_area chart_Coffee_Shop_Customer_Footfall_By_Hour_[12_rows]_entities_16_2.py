
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Day': list(range(1, 31)),
    'Steps': [4000, 4500, 4800, 5000, 5300, 5500, 5700, 6000, 6200, 6400, 6600, 6800, 7000, 7200, 7400, 7600, 7800, 8000, 8200, 8400, 8600, 8800, 9000, 9200, 9400, 9600, 9800, 10000, 10200, 10400]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 10))
plt.fill_between(df['Day'], df['Steps'], color='#1f77b4', alpha=0.7)
plt.plot(df['Day'], df['Steps'], color='#ff7f0e', linewidth=2)

plt.title('Daily Step Count Over a Month', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Day', fontsize=14)
plt.ylabel('Steps', fontsize=14)

max_steps = df['Steps'].max()
max_day = df['Day'][df['Steps'].idxmax()]
plt.annotate(f'Highest: {max_steps}', xy=(max_day, max_steps), xytext=(max_day+1, max_steps+500),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)

plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend(['Step Count'], loc='upper right')

plt.show()