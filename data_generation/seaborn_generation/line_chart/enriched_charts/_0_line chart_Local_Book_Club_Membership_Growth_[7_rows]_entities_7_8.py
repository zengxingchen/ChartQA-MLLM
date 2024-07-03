
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Temperature': [5, 7, 10, 14, 18, 22, 25, 24, 20, 15, 10, 6]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create line plot
plt.figure(figsize=(14, 8))  # Width and height modifications
sns.lineplot(x='Month', y='Temperature', data=df, 
             color='#1B9E77', linewidth=2.5)  # Custom color

# Annotations
for x, y in zip(df['Month'], df['Temperature']):
    plt.text(x, y, f"{y}°C", color='black', fontsize=10, ha='center')

# Customize the Axes and Title
plt.title('Average Monthly Temperature in City X', fontsize=20)
plt.xlabel('Month', fontsize=15)
plt.ylabel('Temperature (°C)', fontsize=15)
plt.xticks(rotation=45)
plt.grid(True)

# Show plot
plt.tight_layout()
plt.show()