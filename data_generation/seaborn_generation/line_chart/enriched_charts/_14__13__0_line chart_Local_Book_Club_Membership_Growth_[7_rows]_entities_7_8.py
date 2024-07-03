
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Temperature': [15, 17, 16, 20, 22, 19, 23]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create line plot
plt.figure(figsize=(14, 8))  # Width and height modifications
sns.lineplot(x='Day', y='Temperature', data=df, color='#4682B4', linewidth=2.5)  # Custom color

# Annotations
for x, y in zip(df['Day'], df['Temperature']):
    plt.text(x, y, f"{y}°C", color='black', fontsize=10, ha='center')

# Customize the Axes and Title
plt.title('Weekly Temperature Trend', fontsize=20)
plt.xlabel('Day', fontsize=15)
plt.ylabel('Temperature (°C)', fontsize=15)
plt.xticks(rotation=45)
plt.grid(True)

# Show plot
plt.tight_layout()
plt.show()