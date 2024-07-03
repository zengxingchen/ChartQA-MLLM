
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Day': list(range(1, 32)),
    'Revenue': [1500, 1800, 1700, 2100, 1900, 2000, 2200, 2300, 2500, 2400, 
                2600, 2800, 2700, 2900, 3000, 3200, 3100, 3300, 3500, 3400, 
                3600, 3700, 3800, 4000, 3900, 4100, 4200, 4300, 4500, 4400, 4600]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(16, 10))
plt.fill_between(df['Day'], df['Revenue'], color='#2ca02c', alpha=0.7)
plt.plot(df['Day'], df['Revenue'], color='#d62728', linewidth=2)

# Title and labels
plt.title('Monthly Revenue Over a Period', fontsize=18, fontweight='bold', pad=25)
plt.xlabel('Day', fontsize=15)
plt.ylabel('Revenue ($)', fontsize=15)

# Annotation
max_revenue = df['Revenue'].max()
max_day = df['Day'][df['Revenue'].idxmax()]
plt.annotate(f'Highest: ${max_revenue}', xy=(max_day, max_revenue), xytext=(max_day+2, max_revenue+200),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=13)

# Grid and legend
plt.grid(True, which='both', linestyle='--', linewidth=0.6)
plt.legend(['Daily Revenue'], loc='upper right')

plt.show()