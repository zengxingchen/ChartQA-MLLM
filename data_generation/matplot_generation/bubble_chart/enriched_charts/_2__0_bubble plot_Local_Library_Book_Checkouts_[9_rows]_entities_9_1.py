
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
    'Country': ['United States', 'China', 'Japan', 'Germany', 'India', 'United Kingdom',
                'France', 'Brazil', 'Italy', 'Canada', 'South Korea', 'Russia',
                'Australia', 'Mexico', 'Indonesia', 'Netherlands', 'Saudi Arabia',
                'Turkey', 'Switzerland', 'Taiwan', 'Argentina', 'Nigeria', 'South Africa',
                'Egypt', 'Thailand', 'Sweden', 'Norway', 'Vietnam', 'Philippines', 'Malaysia',
                'Colombia', 'Singapore'],
    'GDP (Billions)': [21433, 14343, 5082, 3861, 2875, 2827, 2716, 1847, 2001,
                       1643, 1631, 1699, 1393, 1218, 1119, 914, 793, 761, 703, 602,
                       518, 448, 351, 302, 495, 540, 403, 261, 356, 365, 282, 372],
    'Population (Millions)': [331, 1439, 126, 83, 1380, 67, 65, 212, 60, 38, 51, 146,
                              25, 129, 273, 17, 35, 84, 9, 24, 45, 206, 59, 104, 70,
                              10, 5, 97, 109, 32, 51, 6],
    'Happiness Score': [7.3, 5.1, 5.9, 7.0, 3.9, 7.2, 6.5, 6.0, 6.8, 7.1, 5.9, 5.5,
                        7.3, 6.5, 5.3, 7.4, 6.4, 5.2, 7.6, 6.4, 6.2, 4.9, 4.8, 4.7,
                        6.0, 7.5, 7.6, 5.4, 6.1, 6.3, 6.0, 7.2]
})

plt.figure(figsize=(16, 10))

for i in range(len(data)):
    plt.scatter(data['GDP (Billions)'][i], data['Population (Millions)'][i], 
                s=data['Happiness Score'][i]*100, 
                alpha=0.5, 
                c=f'#{int(data["Happiness Score"][i]*25):02x}{50:02x}{100:02x}')

plt.xlabel('GDP in Billions USD')
plt.ylabel('Population in Millions')
plt.title('Global Happiness, GDP, and Population Statistics 2020')
plt.show()