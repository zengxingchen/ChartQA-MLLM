
import matplotlib.pyplot as plt

# Your provided data
data = [
    {'Provider': 'ZypherNet', 'Download Speed (Mbps)': 250, 'Upload Speed (Mbps)': 15},
    {'Provider': 'QuickFiber', 'Download Speed (Mbps)': 500, 'Upload Speed (Mbps)': 50},
    {'Provider': 'SkyConnect', 'Download Speed (Mbps)': 350, 'Upload Speed (Mbps)': 20},
    {'Provider': 'Interlink', 'Download Speed (Mbps)': 450, 'Upload Speed (Mbps)': 25},
    {'Provider': 'DataStream', 'Download Speed (Mbps)': 600, 'Upload Speed (Mbps)': 100},
    {'Provider': 'NovaWave', 'Download Speed (Mbps)': 550, 'Upload Speed (Mbps)': 40},
    {'Provider': 'PulseBroadband', 'Download Speed (Mbps)': 300, 'Upload Speed (Mbps)': 35}
]

# Prepare lists for the scatter plot
providers = [item['Provider'] for item in data]
download_speeds = [item['Download Speed (Mbps)'] for item in data]
upload_speeds = [item['Upload Speed (Mbps)'] for item in data]

# Define unique colors and markers for each provider
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
markers = ['o', 's', '^', 'D', 'P', '*', 'X']

# Create scatter plot
plt.figure(figsize=(10, 6))

for i, provider in enumerate(providers):
    plt.scatter(download_speeds[i], upload_speeds[i], color=colors[i], marker=markers[i], s=100, label=provider)

# Titles and labels
plt.title('Internet Provider Speeds')
plt.xlabel('Download Speed (Mbps)')
plt.ylabel('Upload Speed (Mbps)')

# Annotation for each point with provider name
for i, provider in enumerate(providers):
    plt.annotate(provider, (download_speeds[i], upload_speeds[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Legend outside the plot area
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

# Show grid
plt.grid(True)

# Display the plot
plt.tight_layout()
plt.show()