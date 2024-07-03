
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    'Hours_Exercised': [1.5, 2, 1.8, 2.5, 2.2, 1.9, 2.3, 2.1, 2.6, 1.7, 2.4, 2.8, 1.6, 2.7, 3, 1.4, 2.5, 2.6, 1.5, 2.2, 2.3, 2.1, 1.9, 2.4, 1.8, 2.5, 1.7, 2.6, 2.3, 2.2, 1.9]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(14, 7))
plt.fill_between(df['Day'], df['Hours_Exercised'], color='#FFA07A', alpha=0.7)
plt.plot(df['Day'], df['Hours_Exercised'], color='#FF6347')

# Annotations
for i in range(len(df)):
    plt.text(df['Day'][i], df['Hours_Exercised'][i] + 0.1, str(df['Hours_Exercised'][i]), ha='center', va='bottom', fontsize=8)

# Title and labels
plt.title('Daily Exercise Hours Over a Month', fontsize=16, pad=20)
plt.xlabel('Day of the Month', fontsize=14)
plt.ylabel('Hours Exercised', fontsize=14)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()