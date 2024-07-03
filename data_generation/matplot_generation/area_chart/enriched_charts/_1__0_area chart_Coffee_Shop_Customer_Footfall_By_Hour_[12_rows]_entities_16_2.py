
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Day': list(range(1, 31)),
    'Calories': [2200, 2100, 2250, 2300, 2150, 2200, 2400, 2500, 2450, 2350, 2400, 2300, 2250, 2100, 2150, 2250, 2200, 2300, 2400, 2450, 2500, 2350, 2250, 2300, 2400, 2450, 2500, 2350, 2200, 2150]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(12, 8))
plt.fill_between(df['Day'], df['Calories'], color='#FF5733', alpha=0.7)
plt.plot(df['Day'], df['Calories'], color='#C70039', linewidth=2)

# Title and labels
plt.title('Daily Caloric Intake Over a Month', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Day', fontsize=14)
plt.ylabel('Calories', fontsize=14)

# Annotation
max_calories = df['Calories'].max()
max_day = df['Day'][df['Calories'].idxmax()]
plt.annotate(f'Highest: {max_calories}', xy=(max_day, max_calories), xytext=(max_day+2, max_calories+100),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)

# Grid and legend
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend(['Caloric Intake'], loc='upper left')

plt.show()