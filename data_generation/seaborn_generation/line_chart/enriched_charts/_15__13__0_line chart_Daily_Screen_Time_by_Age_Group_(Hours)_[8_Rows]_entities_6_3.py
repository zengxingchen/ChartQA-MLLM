
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Day': [i for i in range(1, 32)],
    'Temperature': [
        15.0, 14.8, 15.2, 15.5, 15.8, 16.0, 16.3, 16.5, 16.7, 17.0, 
        17.2, 17.5, 17.8, 18.0, 18.5, 18.8, 19.0, 19.3, 19.5, 19.8, 
        20.0, 20.3, 20.5, 20.8, 21.0, 21.3, 21.5, 21.8, 22.0, 22.3, 22.5
    ]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 7))

sns.lineplot(x='Day', y='Temperature', data=df, color='#1E90FF')

for day, temp in zip(data['Day'], data['Temperature']):
    if day == 15:  
        plt.text(day, temp, f"{temp}°C", fontsize=9, ha='center')

plt.title('Daily Temperature Trend over a Month', fontsize=20, pad=20)
plt.xlabel('Day of the Month', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=14)

plt.show()