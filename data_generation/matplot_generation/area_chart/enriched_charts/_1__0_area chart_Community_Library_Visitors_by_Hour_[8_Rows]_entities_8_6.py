
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Temperature': [5, 7, 10, 13, 18, 21, 24, 23, 19, 14, 9, 6]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(12, 8))
plt.fill_between(df['Month'], df['Temperature'], color='#1f77b4', alpha=0.6)
plt.plot(df['Month'], df['Temperature'], color='#1f77b4')

# Add title and labels
plt.title('Average Monthly Temperature', fontsize=16, pad=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=14)

# Add annotation
for i, temp in enumerate(df['Temperature']):
    plt.text(i, temp + 0.5, f'{temp}°C', ha='center')

plt.grid(True)
plt.show()