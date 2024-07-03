
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034],
    'AI': [15, 20, 25, 30, 35, 40, 45, 50, 55, 60],
    'Robotics': [40, 35, 30, 25, 20, 15, 10, 5, 0, 0],
    'Quantum Computing': [25, 20, 15, 10, 5, 0, 0, 0, 0, 0],
    'Blockchain': [20, 15, 10, 5, 0, 0, 0, 0, 0, 0],
    'Biotechnology': [15, 10, 5, 0, 0, 0, 0, 0, 0, 0]
}

df = pd.DataFrame(data)

totals = df.iloc[:, 1:].sum(axis=1)
df_normalized = df.copy()
df_normalized.iloc[:, 1:] = df.iloc[:, 1:].div(totals, 0) * 100

fig, ax = plt.subplots(figsize=(10, 14))
bar_width = 0.6

ax.bar(df['Year'], df_normalized['AI'], color='#FF5733', edgecolor='white', width=bar_width, label='AI')
ax.bar(df['Year'], df_normalized['Robotics'], bottom=df_normalized['AI'], color='#33FF57', edgecolor='white', width=bar_width, label='Robotics')
ax.bar(df['Year'], df_normalized['Quantum Computing'], bottom=df_normalized['AI'] + df_normalized['Robotics'], color='#3357FF', edgecolor='white', width=bar_width, label='Quantum Computing')
ax.bar(df['Year'], df_normalized['Blockchain'], bottom=df_normalized['AI'] + df_normalized['Robotics'] + df_normalized['Quantum Computing'], color='#FF33FF', edgecolor='white', width=bar_width, label='Blockchain')
ax.bar(df['Year'], df_normalized['Biotechnology'], bottom=df_normalized['AI'] + df_normalized['Robotics'] + df_normalized['Quantum Computing'] + df_normalized['Blockchain'], color='#FFFF33', edgecolor='white', width=bar_width, label='Biotechnology')

ax.set_title('Future Technologies (2025-2034)', fontsize=16)
ax.set_ylabel('Percentage (%)', fontsize=14)
ax.set_xlabel('Year', fontsize=14)
ax.legend(loc='upper left')

plt.show()