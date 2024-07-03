
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Date': pd.date_range(start='2023-01-01', periods=31, freq='D'),
    'Rainfall': [50, 55, 60, 65, 70, 68, 75, 80, 85, 83, 
                 88, 92, 95, 100, 105, 110, 115, 118, 120, 125, 
                 130, 135, 133, 140, 145, 150, 155, 160, 165, 170, 175]
}

df = pd.DataFrame(data)

plt.figure(figsize=(18, 9))
sns.lineplot(data=df, x='Date', y='Rainfall', color='#2ca02c', lw=2)
plt.fill_between(df['Date'], 0, df['Rainfall'], color='#2ca02c', alpha=0.3)

plt.title('Monthly Rainfall in mm for January 2023', fontsize=20, pad=20)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Rainfall (mm)', fontsize=14)

plt.text(x=df['Date'][15], y=df['Rainfall'][15], s="Peak Rainfall", color='#ff7f0e', va='bottom', ha='right')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()