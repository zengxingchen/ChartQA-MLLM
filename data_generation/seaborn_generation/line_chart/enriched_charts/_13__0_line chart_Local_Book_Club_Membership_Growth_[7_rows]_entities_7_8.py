
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Visitors': [150, 180, 240, 300, 420, 380, 450, 470, 390, 320, 280, 210]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create line plot
plt.figure(figsize=(16, 9))  # Width and height modifications
sns.lineplot(x='Month', y='Visitors', data=df, 
             color='#FF6347', linewidth=2.5)  # Custom color

# Annotations
for x, y in zip(df['Month'], df['Visitors']):
    plt.text(x, y, f"{y} visitors", color='black', fontsize=10, ha='center')

# Customize the Axes and Title
plt.title('Monthly Visitors to Museum Y', fontsize=20)
plt.xlabel('Month', fontsize=15)
plt.ylabel('Number of Visitors', fontsize=15)
plt.xticks(rotation=45)
plt.grid(True)

# Show plot
plt.tight_layout()
plt.show()