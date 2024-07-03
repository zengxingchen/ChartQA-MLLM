
import matplotlib.pyplot as plt
import pandas as pd

# Creating a DataFrame from the provided table data
data = pd.DataFrame({
    'Country': ['United States', 'China', 'Japan', 'Germany', 'India', 'United Kingdom',
                'France', 'Brazil', 'Italy', 'Canada', 'South Korea', 'Russia',
                'Australia', 'Mexico', 'Indonesia', 'Netherlands', 'Saudi Arabia',
                'Turkey', 'Switzerland', 'Taiwan'],
    'GDP (Billions)': [21433, 14343, 5082, 3861, 2875, 2827, 2716, 1847, 2001,
                       1643, 1631, 1699, 1393, 1218, 1119, 914, 793, 761, 703, 602],
    'Population (Millions)': [331, 1439, 126, 83, 1380, 67, 65, 212, 60, 38, 51, 146,
                              25, 129, 273, 17, 35, 84, 9, 24],
    'Happiness Score': [7.3, 5.1, 5.9, 7.0, 3.9, 7.2, 6.5, 6.0, 6.8, 7.1, 5.9, 5.5,
                        7.3, 6.5, 5.3, 7.4, 6.4, 5.2, 7.6, 6.4]
})

# Setting chart dimensions
plt.figure(figsize=(14, 8))

# Creating the bubble chart
for i in range(len(data)):
    plt.scatter(data['GDP (Billions)'][i], data['Population (Millions)'][i], 
                s=data['Happiness Score'][i]*100, 
                alpha=0.5, 
                c=[(data['Happiness Score'][i]/10, 0.2, 0.4)])

# Adding labels and a title
plt.xlabel('GDP in Billions USD')
plt.ylabel('Population in Millions')
plt.title('World Happiness, GDP and Population Statistics 2020')

# Display the plot
plt.show()