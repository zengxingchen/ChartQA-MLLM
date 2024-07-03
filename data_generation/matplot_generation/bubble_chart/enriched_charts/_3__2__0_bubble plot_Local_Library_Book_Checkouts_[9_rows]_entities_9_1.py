
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
    'Country': ['United States', 'China', 'Japan', 'Germany', 'India', 'United Kingdom',
                'France', 'Brazil', 'Italy', 'Canada', 'South Korea', 'Russia',
                'Australia', 'Mexico', 'Indonesia', 'Netherlands', 'Saudi Arabia',
                'Turkey', 'Switzerland', 'Taiwan', 'Argentina', 'Nigeria', 'South Africa',
                'Egypt', 'Thailand', 'Sweden', 'Norway', 'Vietnam', 'Philippines', 'Malaysia',
                'Colombia', 'Singapore'],
    'Books Published': [300000, 500000, 200000, 150000, 1000000, 120000, 110000, 90000, 80000,
                        70000, 60000, 85000, 75000, 50000, 40000, 45000, 20000, 30000, 35000, 
                        25000, 15000, 5000, 8000, 6000, 12000, 22000, 18000, 17000, 14000, 
                        13000, 10000, 16000],
    'Population (Millions)': [331, 1439, 126, 83, 1380, 67, 65, 212, 60, 38, 51, 146,
                              25, 129, 273, 17, 35, 84, 9, 24, 45, 206, 59, 104, 70,
                              10, 5, 97, 109, 32, 51, 6],
    'Literacy Rate': [99, 96, 99, 99, 74, 99, 99, 93, 99, 99, 99, 96, 99, 95, 95, 99, 95, 95,
                      99, 99, 98, 62, 87, 71, 94, 99, 99, 94, 98, 95, 95, 97]
})

plt.figure(figsize=(18, 12))

for i in range(len(data)):
    plt.scatter(data['Books Published'][i], data['Population (Millions)'][i], 
                s=data['Literacy Rate'][i]*50, 
                alpha=0.6, 
                c=f'#{int(data["Literacy Rate"][i]*2):02x}{100:02x}{150:02x}')

plt.xlabel('Books Published')
plt.ylabel('Population in Millions')
plt.title('Literacy, Population, and Books Published by Country', pad=20)
plt.show()