
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
    'Country': ['United States', 'China', 'Japan', 'Germany', 'India', 'United Kingdom',
                'France', 'Brazil', 'Italy', 'Canada', 'South Korea', 'Russia',
                'Australia', 'Mexico', 'Indonesia', 'Netherlands', 'Saudi Arabia',
                'Turkey', 'Switzerland', 'Taiwan'],
    'Stress Level': [5.5, 6.2, 7.3, 4.2, 6.8, 5.0, 4.0, 6.0, 4.5, 4.7, 7.0, 6.3, 4.3, 6.5, 6.7, 3.9, 6.0, 6.1, 3.8, 6.4],
    'Work Hours (per week)': [40, 45, 50, 38, 48, 39, 35, 44, 36, 37, 52, 46, 38, 48, 49, 34, 44, 45, 33, 46],
    'Leisure Time (per week)': [15, 10, 8, 18, 12, 17, 20, 14, 19, 18, 9, 12, 18, 13, 11, 21, 13, 12, 22, 12]
})

plt.figure(figsize=(16, 10))

for i in range(len(data)):
    plt.scatter(data['Work Hours (per week)'][i], data['Leisure Time (per week)'][i], 
                s=data['Stress Level'][i]*50, 
                alpha=0.6, 
                c=f'#{int(255*(data["Stress Level"][i]/10)):02x}0000')

plt.xlabel('Work Hours per Week')
plt.ylabel('Leisure Time per Week (in hours)')
plt.title('Work Hours vs Leisure Time and Stress Levels in Various Countries')

plt.show()