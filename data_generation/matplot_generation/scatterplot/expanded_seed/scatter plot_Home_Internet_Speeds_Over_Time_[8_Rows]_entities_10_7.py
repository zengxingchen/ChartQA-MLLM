
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Month': 'January', 'Download Speed (Mbps)': 50, 'Upload Speed (Mbps)': 10},
    {'Month': 'February', 'Download Speed (Mbps)': 55, 'Upload Speed (Mbps)': 11},
    {'Month': 'March', 'Download Speed (Mbps)': 60, 'Upload Speed (Mbps)': 12},
    {'Month': 'April', 'Download Speed (Mbps)': 50, 'Upload Speed (Mbps)': 10},
    {'Month': 'May', 'Download Speed (Mbps)': 65, 'Upload Speed (Mbps)': 13},
    {'Month': 'June', 'Download Speed (Mbps)': 70, 'Upload Speed (Mbps)': 14},
    {'Month': 'July', 'Download Speed (Mbps)': 75, 'Upload Speed (Mbps)': 15},
    {'Month': 'August', 'Download Speed (Mbps)': 80, 'Upload Speed (Mbps)': 16},
    {'Month': 'September', 'Download Speed (Mbps)': 85, 'Upload Speed (Mbps)': 17},
    {'Month': 'October', 'Download Speed (Mbps)': 78, 'Upload Speed (Mbps)': 16}
]

# Extracting months, download speeds, and upload speeds
months = [item['Month'] for item in data]
download_speeds = [item['Download Speed (Mbps)'] for item in data]
upload_speeds = [item['Upload Speed (Mbps)'] for item in data]

# Setting up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Creating a scatter plot with diversified visual encoding
# Scatter points will be color-coded by download speed and size-coded by upload speed
colors = download_speeds
sizes = [upload * 20 for upload in upload_speeds] # Multiply by 20 for better visual difference in size

scatter = ax.scatter(download_speeds, upload_speeds, c=colors, s=sizes, cmap='viridis', alpha=0.6, edgecolors='w')

# Adding a color bar
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Download Speed (Mbps)')

# Adding labels for each point to show the corresponding month
for i, month in enumerate(months):
    ax.annotate(month, (download_speeds[i], upload_speeds[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Labeling the axes
ax.set_xlabel('Download Speed (Mbps)')
ax.set_ylabel('Upload Speed (Mbps)')
ax.set_title('Internet Speeds by Month')

# Display the plot
plt.show()