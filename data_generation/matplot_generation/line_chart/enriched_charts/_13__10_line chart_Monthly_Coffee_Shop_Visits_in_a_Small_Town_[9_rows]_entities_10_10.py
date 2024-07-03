
import matplotlib.pyplot as plt

# Data from the provided chart table
data = [
    {'Month': 'January', 'Social Media Usage': 300, 'Online Shopping': 250, 'Streaming Services': 280, 'E-Learning Platforms': 220, 'Telemedicine': 200},
    {'Month': 'February', 'Social Media Usage': 310, 'Online Shopping': 260, 'Streaming Services': 290, 'E-Learning Platforms': 230, 'Telemedicine': 210},
    {'Month': 'March', 'Social Media Usage': 320, 'Online Shopping': 270, 'Streaming Services': 300, 'E-Learning Platforms': 240, 'Telemedicine': 220},
    {'Month': 'April', 'Social Media Usage': 330, 'Online Shopping': 280, 'Streaming Services': 310, 'E-Learning Platforms': 250, 'Telemedicine': 230},
    {'Month': 'May', 'Social Media Usage': 340, 'Online Shopping': 290, 'Streaming Services': 320, 'E-Learning Platforms': 260, 'Telemedicine': 240},
    {'Month': 'June', 'Social Media Usage': 350, 'Online Shopping': 300, 'Streaming Services': 330, 'E-Learning Platforms': 270, 'Telemedicine': 250},
    {'Month': 'July', 'Social Media Usage': 360, 'Online Shopping': 310, 'Streaming Services': 340, 'E-Learning Platforms': 280, 'Telemedicine': 260},
    {'Month': 'August', 'Social Media Usage': 370, 'Online Shopping': 320, 'Streaming Services': 350, 'E-Learning Platforms': 290, 'Telemedicine': 270},
    {'Month': 'September', 'Social Media Usage': 380, 'Online Shopping': 330, 'Streaming Services': 360, 'E-Learning Platforms': 300, 'Telemedicine': 280},
    {'Month': 'October', 'Social Media Usage': 390, 'Online Shopping': 340, 'Streaming Services': 370, 'E-Learning Platforms': 310, 'Telemedicine': 290}
]

# Extracting month names for the x-axis
months = [entry['Month'] for entry in data]

# Plotting each technology's trend
plt.figure(figsize=(16, 8))
technologies = list(data[0].keys())[1:]  # Get technology names skipping the 'Month' key

# Line style settings and markers for each technology
line_styles = ['-', '--', '-.', ':', '-']
markers = ['o', '^', 's', 'D', 'x']
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#57FF33']

for i, tech in enumerate(technologies):
    values = [entry[tech] for entry in data]
    plt.plot(months, values, label=tech, linestyle=line_styles[i % len(line_styles)], marker=markers[i % len(markers)], color=colors[i % len(colors)])
    plt.text(months[-1], values[-1], f'{values[-1]}', fontsize=10, color=colors[i % len(colors)])

# Adding titles and labels
plt.title('Monthly Digital Platform Usage Trends', pad=20)
plt.xlabel('Month')
plt.ylabel('Usage (in million hours)')

# Adding grid for readability
plt.grid(True)

# Adding a legend to identify the lines
plt.legend(title='Digital Platforms', loc='upper left', bbox_to_anchor=(1, 1))

# Show the plot
plt.show()