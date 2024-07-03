
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': list(range(1995, 2025)),
    'Exoplanets_Discovered': [1, 5, 4, 8, 12, 9, 14, 20, 24, 30, 34, 25, 22, 28, 36, 45, 50, 55, 60, 70, 65, 72, 80, 85, 90, 95, 100, 110, 115, 120]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 10))
plt.fill_between(df['Year'], df['Exoplanets_Discovered'], color='#2ca02c', alpha=0.7)
plt.plot(df['Year'], df['Exoplanets_Discovered'], color='#d62728', linewidth=2)

plt.title('Exoplanets Discovered Over the Years', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Exoplanets Discovered', fontsize=14)

max_exoplanets = df['Exoplanets_Discovered'].max()
max_year = df['Year'][df['Exoplanets_Discovered'].idxmax()]
plt.annotate(f'Highest: {max_exoplanets}', xy=(max_year, max_exoplanets), xytext=(max_year+1, max_exoplanets+10),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)

plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend(['Exoplanets Discovered'], loc='upper left')

plt.show()