
import matplotlib.pyplot as plt

data = {
    'Category': ['Electric', 'Hybrid', 'Gasoline', 'Diesel', 'Hydrogen', 'Biofuel', 'Natural Gas', 
                 'Biodiesel', 'Solar', 'Ethanol', 'Methanol', 'Propane', 'Nuclear', 'Compressed Air'],
    'CO2 Emissions (g/km)': [0, 50, 150, 130, 20, 90, 110, 80, 0, 70, 60, 100, 10, 0],
    'Efficiency (MPG)': [100, 60, 25, 30, 70, 40, 35, 45, 150, 50, 55, 37, 80, 120],
    'Eco Rating': [95, 90, 70, 75, 85, 80, 78, 82, 98, 79, 81, 77, 97, 96]
}

size = [value * 10 for value in data['Eco Rating']]

plt.figure(figsize=(18, 12))

scatter = plt.scatter(data['CO2 Emissions (g/km)'], data['Efficiency (MPG)'], 
                      s=size, alpha=0.6, 
                      c=['#FF6347', '#4682B4', '#FFD700', '#32CD32', '#6A5ACD', '#FF4500', '#1E90FF', 
                         '#9ACD32', '#FFDAB9', '#B0E0E6', '#BA55D3', '#7FFF00', '#D2691E', '#F0E68C'])

plt.title('Vehicle Fuel Types: Emissions and Efficiency', pad=20)
plt.xlabel('CO2 Emissions (g/km)')
plt.ylabel('Efficiency (MPG)')

for index, category in enumerate(data['Category']):
    plt.text(data['CO2 Emissions (g/km)'][index], data['Efficiency (MPG)'][index], 
             category, fontsize=9, ha='center', va='center')

plt.grid(True)
plt.show()