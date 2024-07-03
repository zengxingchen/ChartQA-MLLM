
import matplotlib.pyplot as plt

# Extracted data from the provided table
data = [
    {'Year': 2018, 'Smart Speakers': 47, 'Smart Thermostats': 18, 'Home Security Systems': 29, 'Video Doorbells': 11, 'Population (Millions)': 128.45, 'Average Devices per Household': 1.3},
    {'Year': 2019, 'Smart Speakers': 56, 'Smart Thermostats': 24, 'Home Security Systems': 34, 'Video Doorbells': 17, 'Population (Millions)': 128.58, 'Average Devices per Household': 1.7},
    {'Year': 2020, 'Smart Speakers': 68, 'Smart Thermostats': 29, 'Home Security Systems': 40, 'Video Doorbells': 24, 'Population (Millions)': 128.7, 'Average Devices per Household': 2.1},
    {'Year': 2021, 'Smart Speakers': 79, 'Smart Thermostats': 35, 'Home Security Systems': 47, 'Video Doorbells': 32, 'Population (Millions)': 128.85, 'Average Devices per Household': 2.6},
    {'Year': 2022, 'Smart Speakers': 87, 'Smart Thermostats': 41, 'Home Security Systems': 53, 'Video Doorbells': 39, 'Population (Millions)': 129.0, 'Average Devices per Household': 3.0}
]

# Prepare data for plotting
years = [d['Year'] for d in data]
smart_speakers = [d['Smart Speakers'] for d in data]
smart_thermostats = [d['Smart Thermostats'] for d in data]
home_security_systems = [d['Home Security Systems'] for d in data]
video_doorbells = [d['Video Doorbells'] for d in data]
average_devices = [d['Average Devices per Household'] for d in data]
population = [d['Population (Millions)'] for d in data]

# Create a color map based on the years
colors = plt.cm.viridis((years - min(years)) / (max(years) - min(years)))

# Generate bubble sizes based on the Average Devices per Household (scaled for better visualization)
bubble_sizes = [avg_dev * 100 for avg_dev in average_devices]

# Create the bubble chart
plt.figure(figsize=(10, 6))
plt.scatter(years, smart_speakers, s=bubble_sizes, c=colors, alpha=0.6, edgecolors='w', linewidth=1, label='Smart Speakers')
plt.scatter(years, smart_thermostats, s=bubble_sizes, c=colors, alpha=0.6, edgecolors='w', linewidth=1, label='Smart Thermostats')
plt.scatter(years, home_security_systems, s=bubble_sizes, c=colors, alpha=0.6, edgecolors='w', linewidth=1, label='Home Security Systems')
plt.scatter(years, video_doorbells, s=bubble_sizes, c=colors, alpha=0.6, edgecolors='w', linewidth=1, label='Video Doorbells')

# Add labels and title
plt.title('Smart Home Devices Sales with Average Devices per Household (Bubble Size)')
plt.xlabel('Year')
plt.ylabel('Units Sold (Millions)')
plt.xticks(years)
plt.legend(loc='upper left')

# Colorbar to show the mapping of color to year
sm = plt.cm.ScalarMappable(cmap=plt.cm.viridis, norm=plt.Normalize(min(years),max(years)))
sm.set_array([])
plt.colorbar(sm, label='Year', ticks=years)

# Show the plot
plt.tight_layout()
plt.show()