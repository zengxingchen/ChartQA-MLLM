
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Time': ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', 
             '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', 
             '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00', 
             '24:00'],
    'Brightness': [5.0, 6.2, 7.5, 8.0, 6.8, 7.1, 8.4, 9.0, 7.8, 8.2, 9.5, 10.0, 9.3, 
                   8.7, 9.1, 10.2, 11.0, 10.5, 9.8, 10.0, 11.3, 12.0, 11.5, 10.8, 11.0]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(14, 8))
plt.fill_between(df['Time'], df['Brightness'], color='#1f77b4', alpha=0.6)

# Title and labels
plt.title('Brightness of Celestial Object Over Time', fontsize=16, loc='left')
plt.xlabel('Time', fontsize=12)
plt.ylabel('Brightness (Magnitude)', fontsize=12)

# Annotations
plt.annotate('Peak Brightness', xy=('21:00', 12.0), xytext=('17:00', 13),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12, color='black')

# Adjustments
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()