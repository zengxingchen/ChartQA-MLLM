
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Attendance': [50, 45, 70, 80, 120, 150, 200, 180, 160, 140, 100, 90]
}

# Create DataFrame
df = pd.DataFrame(data)

# Adjusting the aesthetics
sns.set_theme(style="whitegrid")

# Create the plot
plt.figure(figsize=(16, 8))
lineplot = sns.lineplot(x='Month', y='Attendance', data=df, marker='o', linewidth=2.5,
                        color='#1f77b4')

# Customize the axes and title
plt.xticks(rotation=45)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Attendance', fontsize=14)
plt.title('Monthly Attendance in Music & Performing Arts Events (2023)', fontsize=20, pad=20)

# Annotating the data points
for x, y in zip(df['Month'], df['Attendance']):
    plt.text(x, y, y, ha='center', va='bottom', fontsize=10)

# Show the plot
plt.show()