
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
    'Country': ['United States', 'Mexico', 'New Zealand', 'Australia', 'United Kingdom',
                'Canada', 'Germany', 'France', 'Italy', 'Spain', 'Brazil', 'Argentina',
                'China', 'India', 'Russia', 'Japan', 'South Korea', 'Saudi Arabia',
                'Turkey', 'South Africa', 'Sweden', 'Norway', 'Netherlands', 'Belgium',
                'Switzerland', 'Austria', 'Denmark', 'Finland', 'Ireland', 'Portugal', 'Greece'],
    'Population (Millions)': [331, 129, 5, 25, 67, 38, 83, 65, 60, 47, 212, 45, 1439, 1380, 146, 126, 51, 35, 84, 60, 10, 5, 17, 11, 9, 9, 6, 5, 5, 10, 11],
    'Average Calorie Intake (kcal)': [3770, 3460, 3240, 3340, 3400, 3480, 3560, 3260, 3100, 3150, 3000, 3150, 3060, 2450, 3270, 2760, 2990, 3010, 2850, 2990, 3400, 3600, 3300, 3250, 3380, 3260, 3390, 3350, 3400, 3150, 3200],
    'Obesity Rate (%)': [36.2, 28.9, 30.8, 29.0, 27.8, 29.4, 22.3, 21.6, 19.9, 23.8, 22.1, 28.3, 6.2, 3.9, 23.1, 4.3, 5.3, 33.7, 32.1, 28.3, 20.6, 21.1, 20.4, 22.2, 18.8, 19.9, 20.5, 20.8, 25.3, 21.4, 24.9],
    'Literacy Rate (%)': [99, 95, 99, 99, 99, 99, 99, 99, 99, 99, 92, 99, 97, 74, 99, 99, 99, 97, 96, 87, 99, 99, 99, 99, 99, 99, 99, 99, 99, 96, 97]
})

plt.figure(figsize=(14, 8))

for i in range(len(data)):
    plt.scatter(data['Average Calorie Intake (kcal)'][i], data['Obesity Rate (%)'][i], 
                s=data['Population (Millions)'][i]*3, 
                alpha=0.6, 
                c=[(data['Literacy Rate (%)'][i]/100, 0.2, 0.8)])

plt.xlabel('Average Calorie Intake (kcal)')
plt.ylabel('Obesity Rate (%)')
plt.title('Education & Learning: Obesity Rate vs Average Calorie Intake by Country')

plt.show()