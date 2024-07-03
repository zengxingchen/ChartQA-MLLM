
import matplotlib.pyplot as plt
import pandas as pd

# Creating a DataFrame from the provided table data
data = pd.DataFrame({
    'Country': ['United States', 'Mexico', 'New Zealand', 'Australia', 'United Kingdom',
                'Canada', 'Germany', 'France', 'Italy', 'Spain', 'Brazil', 'Argentina',
                'China', 'India', 'Russia', 'Japan', 'South Korea', 'Saudi Arabia',
                'Turkey', 'South Africa'],
    'Obesity Rate (%)': [36.2, 28.9, 30.8, 29.0, 27.8, 29.4, 22.3, 21.6, 19.9, 23.8,
                         22.1, 28.3, 6.2, 3.9, 23.1, 4.3, 5.3, 33.7, 32.1, 28.3],
    'Average Calorie Intake (kcal)': [3770, 3460, 3240, 3340, 3400, 3480, 3560, 3260, 3100, 3150,
                                      3000, 3150, 3060, 2450, 3270, 2760, 2990, 3010, 2850, 2990],
    'Life Expectancy (years)': [78.6, 75.1, 82.0, 82.9, 81.3, 82.3, 81.2, 82.6, 83.4, 83.3,
                                75.9, 76.5, 76.7, 69.4, 72.6, 84.5, 83.3, 75.0, 75.9, 64.1],
    'Population (Millions)': [331, 129, 5, 25, 67, 38, 83, 65, 60, 47, 212, 45, 1439, 1380, 146, 126, 51, 35, 84, 60]
})

# Setting chart dimensions
plt.figure(figsize=(16, 10))

# Creating the bubble chart
for i in range(len(data)):
    plt.scatter(data['Average Calorie Intake (kcal)'][i], data['Obesity Rate (%)'][i], 
                s=data['Population (Millions)'][i]*5, 
                alpha=0.6, 
                c=[(data['Life Expectancy (years)'][i]/100, 0.3, 0.6)])

# Adding labels and a title
plt.xlabel('Average Calorie Intake (kcal)')
plt.ylabel('Obesity Rate (%)')
plt.title('Food & Nutrition: Obesity Rate vs Average Calorie Intake by Country')

# Display the plot
plt.show()