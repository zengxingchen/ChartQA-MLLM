
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Rainfall': [5, 7, 3, 6, 8, 2, 9]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create line plot
plt.figure(figsize=(12, 7))  # Width and height modifications
sns.lineplot(x='Day', y='Rainfall', data=df, color='#FF6347', linewidth=2.5)  # Custom color

# Annotations
for x, y in zip(df['Day'], df['Rainfall']):
    plt.text(x, y, f"{y} mm", color='black', fontsize=10, ha='center')

# Customize the Axes and Title
plt.title('Weekly Rainfall Trend', fontsize=20, pad=20)
plt.xlabel('Day', fontsize=15)
plt.ylabel('Rainfall (mm)', fontsize=15)
plt.xticks(rotation=45)
plt.grid(True)

# Show plot
plt.tight_layout()
plt.show()