
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    'Calories_Intake': [2200, 2100, 2300, 2000, 2500, 2400, 2150, 2350, 2450, 2250, 2150, 2300, 2400, 2250, 2500, 2100, 2200, 2350, 2450, 2300, 2100, 2500, 2350, 2400, 2150, 2300, 2250, 2500, 2400, 2200, 2300]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(16, 8))
plt.fill_between(df['Day'], df['Calories_Intake'], color='#87CEFA', alpha=0.7)
plt.plot(df['Day'], df['Calories_Intake'], color='#1E90FF')

# Annotations
for i in range(len(df)):
    plt.text(df['Day'][i], df['Calories_Intake'][i] + 30, str(df['Calories_Intake'][i]), ha='center', va='bottom', fontsize=8)

# Title and labels
plt.title('Daily Caloric Intake Over a Month', fontsize=18, pad=25)
plt.xlabel('Day of the Month', fontsize=14)
plt.ylabel('Calories Intake', fontsize=14)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()