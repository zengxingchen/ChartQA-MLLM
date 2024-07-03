
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Sales': [100, 120, 150, 170, 200, 180, 210, 220, 200, 230, 250, 270]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create line plot
plt.figure(figsize=(12, 6))  # Width and height modifications
sns.lineplot(x='Month', y='Sales', data=df, 
             color='#FF5733', linewidth=2.5)  # Custom color

# Annotations
for x, y in zip(df['Month'], df['Sales']):
    plt.text(x, y, f"{y} units", color='black', fontsize=10, ha='center')

# Customize the Axes and Title
plt.title('Monthly Sales Data for Product Y', fontsize=20)
plt.xlabel('Month', fontsize=15)
plt.ylabel('Sales (units)', fontsize=15)
plt.xticks(rotation=45)
plt.grid(True)

# Show plot
plt.tight_layout()
plt.show()