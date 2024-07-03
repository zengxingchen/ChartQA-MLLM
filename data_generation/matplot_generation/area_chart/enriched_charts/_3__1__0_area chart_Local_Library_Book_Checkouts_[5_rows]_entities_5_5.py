
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    'Exercise_Duration': [30, 45, 50, 60, 55, 40, 50, 70, 65, 60, 55, 50, 45, 70, 75, 60, 55, 50, 65, 70, 60, 50, 55, 65, 60, 50, 55, 60, 70, 75, 80]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(14, 8))
plt.fill_between(df['Day'], df['Exercise_Duration'], color='#FF6347', alpha=0.7)
plt.plot(df['Day'], df['Exercise_Duration'], color='#FF4500')

# Annotations
for i in range(len(df)):
    plt.text(df['Day'][i], df['Exercise_Duration'][i] + 1, str(df['Exercise_Duration'][i]), ha='center', va='bottom', fontsize=8)

# Title and labels
plt.title('Daily Exercise Duration Over a Month', fontsize=18, pad=20)
plt.xlabel('Day of the Month', fontsize=14)
plt.ylabel('Exercise Duration (minutes)', fontsize=14)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()