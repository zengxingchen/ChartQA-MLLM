
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    'Hours_Slept': [7, 6.5, 7.2, 8, 7.5, 6.8, 7, 7.3, 8.1, 6.9, 7.4, 7.6, 6.7, 7.8, 8.2, 6.4, 7.3, 7.5, 6.6, 7.1, 8, 7.2, 6.8, 7.9, 7.1, 7.6, 6.5, 8, 7.3, 7.7, 6.9]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(12, 6))
plt.fill_between(df['Day'], df['Hours_Slept'], color='#4682B4', alpha=0.7)
plt.plot(df['Day'], df['Hours_Slept'], color='#1E90FF')

# Annotations
for i in range(len(df)):
    plt.text(df['Day'][i], df['Hours_Slept'][i] + 0.1, str(df['Hours_Slept'][i]), ha='center', va='bottom', fontsize=8)

# Title and labels
plt.title('Daily Hours of Sleep Over a Month', fontsize=16, pad=20)
plt.xlabel('Day of the Month', fontsize=14)
plt.ylabel('Hours Slept', fontsize=14)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()