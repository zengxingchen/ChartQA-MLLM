
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Day': list(range(1, 31)),
    'Steps': [
        5500, 6500, 7000, 6800, 7200, 7500, 8000, 8200, 7800, 7900,
        8400, 8600, 9000, 9200, 9500, 9100, 9300, 9700, 10000, 10500,
        11000, 10800, 11500, 12000, 11800, 12200, 12500, 12700, 13000, 13500
    ]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 8))
plt.fill_between(df['Day'], df['Steps'], color='#3498DB', alpha=0.6)
plt.plot(df['Day'], df['Steps'], color='#1F618D')

plt.title('Daily Step Count for June 2024', fontsize=18, pad=25)
plt.xlabel('Day', fontsize=15)
plt.ylabel('Steps', fontsize=15)

for i, steps in enumerate(df['Steps']):
    plt.text(i + 1, steps + 200, f'{steps}', ha='center')

plt.grid(True)
plt.show()