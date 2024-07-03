
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Viewers': [320, 400, 450, 380, 420, 470, 440, 510, 490, 530, 550, 600]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create line plot
plt.figure(figsize=(14, 8))  # Width and height modifications
sns.lineplot(x='Month', y='Viewers', data=df, 
             color='#1f77b4', linewidth=2.5)  # Custom color

# Annotations
for x, y in zip(df['Month'], df['Viewers']):
    plt.text(x, y, f"{y} viewers", color='black', fontsize=10, ha='center')

# Customize the Axes and Title
plt.title('Monthly Viewership Data for TV Show X', fontsize=20, pad=20)
plt.xlabel('Month', fontsize=15)
plt.ylabel('Viewers (thousands)', fontsize=15)
plt.xticks(rotation=45)
plt.grid(True)

# Show plot
plt.tight_layout()
plt.show()