
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Time': ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', 
             '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', 
             '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00', 
             '24:00'],
    'Heart_Rate': [62, 65, 63, 64, 62, 61, 60, 64, 70, 75, 72, 71, 69, 68, 70, 72, 
                   74, 73, 75, 76, 74, 73, 72, 70, 68]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(16, 9))
plt.fill_between(df['Time'], df['Heart_Rate'], color='#ff7f0e', alpha=0.6)

# Title and labels
plt.title('Heart Rate Over Time', fontsize=18, loc='center')
plt.xlabel('Time', fontsize=14)
plt.ylabel('Heart Rate (bpm)', fontsize=14)

# Annotations
plt.annotate('Highest Heart Rate', xy=('19:00', 76), xytext=('15:00', 78),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12, color='black')

# Adjustments
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()