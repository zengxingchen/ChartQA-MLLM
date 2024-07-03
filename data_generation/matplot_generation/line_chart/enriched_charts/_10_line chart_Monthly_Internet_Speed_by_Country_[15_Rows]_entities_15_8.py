
import matplotlib.pyplot as plt

# Data provided in the question
chart_data = [
    {'Month': 'January', 'Running (km)': 10, 'Swimming (km)': 2, 'Cycling (km)': 30, 'Walking (km)': 20},
    {'Month': 'February', 'Running (km)': 12, 'Swimming (km)': 2.5, 'Cycling (km)': 32, 'Walking (km)': 21},
    {'Month': 'March', 'Running (km)': 14, 'Swimming (km)': 3, 'Cycling (km)': 34, 'Walking (km)': 22},
    {'Month': 'April', 'Running (km)': 16, 'Swimming (km)': 3.5, 'Cycling (km)': 36, 'Walking (km)': 23},
    {'Month': 'May', 'Running (km)': 18, 'Swimming (km)': 4, 'Cycling (km)': 38, 'Walking (km)': 24},
    {'Month': 'June', 'Running (km)': 20, 'Swimming (km)': 4.5, 'Cycling (km)': 40, 'Walking (km)': 25},
    {'Month': 'July', 'Running (km)': 22, 'Swimming (km)': 5, 'Cycling (km)': 42, 'Walking (km)': 26},
    {'Month': 'August', 'Running (km)': 24, 'Swimming (km)': 5.5, 'Cycling (km)': 44, 'Walking (km)': 27},
    {'Month': 'September', 'Running (km)': 26, 'Swimming (km)': 6, 'Cycling (km)': 46, 'Walking (km)': 28},
    {'Month': 'October', 'Running (km)': 28, 'Swimming (km)': 6.5, 'Cycling (km)': 48, 'Walking (km)': 29},
    {'Month': 'November', 'Running (km)': 30, 'Swimming (km)': 7, 'Cycling (km)': 50, 'Walking (km)': 30},
    {'Month': 'December', 'Running (km)': 32, 'Swimming (km)': 7.5, 'Cycling (km)': 52, 'Walking (km)': 31}
]

# Extracting the data for plotting
months = [entry['Month'] for entry in chart_data]
running_km = [entry['Running (km)'] for entry in chart_data]
swimming_km = [entry['Swimming (km)'] for entry in chart_data]
cycling_km = [entry['Cycling (km)'] for entry in chart_data]
walking_km = [entry['Walking (km)'] for entry in chart_data]

# Plotting the data
plt.figure(figsize=(12, 8))

plt.plot(months, running_km, label='Running', marker='o', linestyle='-', color='#1f77b4')
plt.plot(months, swimming_km, label='Swimming', marker='s', linestyle='--', color='#ff7f0e')
plt.plot(months, cycling_km, label='Cycling', marker='^', linestyle='-.', color='#2ca02c')
plt.plot(months, walking_km, label='Walking', marker='d', linestyle=':', color='#d62728')

# Adding the title and labels
plt.title('Monthly Physical Activities Distance', fontsize=16, pad=20)
plt.xlabel('Month')
plt.ylabel('Distance (km)')
plt.xticks(rotation=45)  # Rotate the x-axis labels for better readability

# Adding annotations
for i, txt in enumerate(running_km):
    plt.annotate(txt, (months[i], running_km[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Adding a legend
plt.legend()

# Adjust layout to prevent clipping and show the plot
plt.tight_layout()
plt.show()