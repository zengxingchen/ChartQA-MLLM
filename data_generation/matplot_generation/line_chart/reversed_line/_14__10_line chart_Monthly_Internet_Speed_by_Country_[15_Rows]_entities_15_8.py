
import matplotlib.pyplot as plt

# Data provided in the question
chart_data = [
    {'Month': 'January', 'Deforestation (hectares)': 5000, 'Air Pollution (AQI)': 75, 'Water Pollution (mg/L)': 8, 'Soil Erosion (tons/ha)': 1500},
    {'Month': 'February', 'Deforestation (hectares)': 5200, 'Air Pollution (AQI)': 72, 'Water Pollution (mg/L)': 7.5, 'Soil Erosion (tons/ha)': 1550},
    {'Month': 'March', 'Deforestation (hectares)': 5400, 'Air Pollution (AQI)': 70, 'Water Pollution (mg/L)': 7.2, 'Soil Erosion (tons/ha)': 1600},
    {'Month': 'April', 'Deforestation (hectares)': 5600, 'Air Pollution (AQI)': 68, 'Water Pollution (mg/L)': 7, 'Soil Erosion (tons/ha)': 1650},
    {'Month': 'May', 'Deforestation (hectares)': 5800, 'Air Pollution (AQI)': 65, 'Water Pollution (mg/L)': 6.8, 'Soil Erosion (tons/ha)': 1700},
    {'Month': 'June', 'Deforestation (hectares)': 6000, 'Air Pollution (AQI)': 63, 'Water Pollution (mg/L)': 6.5, 'Soil Erosion (tons/ha)': 1750},
    {'Month': 'July', 'Deforestation (hectares)': 6200, 'Air Pollution (AQI)': 60, 'Water Pollution (mg/L)': 6.2, 'Soil Erosion (tons/ha)': 1800},
    {'Month': 'August', 'Deforestation (hectares)': 6400, 'Air Pollution (AQI)': 58, 'Water Pollution (mg/L)': 6, 'Soil Erosion (tons/ha)': 1850},
    {'Month': 'September', 'Deforestation (hectares)': 6600, 'Air Pollution (AQI)': 55, 'Water Pollution (mg/L)': 5.8, 'Soil Erosion (tons/ha)': 1900},
    {'Month': 'October', 'Deforestation (hectares)': 6800, 'Air Pollution (AQI)': 53, 'Water Pollution (mg/L)': 5.5, 'Soil Erosion (tons/ha)': 1950},
    {'Month': 'November', 'Deforestation (hectares)': 7000, 'Air Pollution (AQI)': 50, 'Water Pollution (mg/L)': 5.2, 'Soil Erosion (tons/ha)': 2000},
    {'Month': 'December', 'Deforestation (hectares)': 7200, 'Air Pollution (AQI)': 48, 'Water Pollution (mg/L)': 5, 'Soil Erosion (tons/ha)': 2050}
]

# Extracting the data for plotting
months = [entry['Month'] for entry in chart_data]
deforestation_hectares = [entry['Deforestation (hectares)'] for entry in chart_data]
air_pollution_aqi = [entry['Air Pollution (AQI)'] for entry in chart_data]
water_pollution_mg = [entry['Water Pollution (mg/L)'] for entry in chart_data]
soil_erosion_tons = [entry['Soil Erosion (tons/ha)'] for entry in chart_data]

# Plotting the data
plt.figure(figsize=(14, 10))

plt.plot(months, deforestation_hectares, label='Deforestation', marker='o', linestyle='-', color='#1f78b4')
plt.plot(months, air_pollution_aqi, label='Air Pollution', marker='s', linestyle='--', color='#33a02c')
plt.plot(months, water_pollution_mg, label='Water Pollution', marker='^', linestyle='-.', color='#e31a1c')
plt.plot(months, soil_erosion_tons, label='Soil Erosion', marker='d', linestyle=':', color='#ff7f00')

# Adding the title and labels
plt.title('Monthly Environmental Issues Overview', fontsize=18, pad=20)
plt.xlabel('Month')
plt.ylabel('Impact Level')
plt.xticks(rotation=45)  # Rotate the x-axis labels for better readability

# Adding annotations
for i, txt in enumerate(deforestation_hectares):
    plt.annotate(txt, (months[i], deforestation_hectares[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Adding a legend
plt.legend()

# Adjust layout to prevent clipping and show the plot
plt.gca().invert_yaxis()  # Inverting the y-axis
plt.tight_layout()
plt.show()