
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Temperature': [5.2, 6.0, 9.3, 12.8, 16.5, 19.1, 21.4, 21.0, 17.8, 13.2, 8.5, 5.7]
}

df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(12, 6))
plt.fill_between(df['Month'], df['Temperature'], color='#66c2a5', alpha=0.7)
plt.plot(df['Month'], df['Temperature'], color='#3288bd', marker='o', markersize=5)

# Titles and labels
plt.title('Average Monthly Temperatures for the Year', fontsize=16, pad=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=14)

# Annotations
for i, txt in enumerate(df['Temperature']):
    plt.annotate(f"{txt}°C", (df['Month'][i], df['Temperature'][i]), textcoords="offset points", xytext=(0,5), ha='center')

plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("average_monthly_temperatures.png")
plt.show()