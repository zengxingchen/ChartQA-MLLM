
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
              'September', 'October', 'November', 'December'],
    'Temperature': [30, 32, 45, 55, 65, 75, 85, 80, 70, 60, 50, 35]
}

df = pd.DataFrame(data)

month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
df['Month'] = pd.Categorical(df['Month'], categories=month_order, ordered=True)

plt.figure(figsize=(12, 6))

lineplot = sns.lineplot(x='Month', y='Temperature', data=df, color="#3498db", marker='o')

for i in range(df.shape[0]):
    plt.text(df['Month'][i], df['Temperature'][i] + 2, f"{df['Temperature'][i]}°F", 
             ha='center', va='bottom', fontsize=9, color='#2c3e50')

plt.title('Average Monthly Temperature in City XYZ', fontsize=18)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Temperature (°F)', fontsize=14)

plt.show()