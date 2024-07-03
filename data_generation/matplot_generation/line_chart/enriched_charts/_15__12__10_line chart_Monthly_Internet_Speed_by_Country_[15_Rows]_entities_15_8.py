
import matplotlib.pyplot as plt

# Data provided in the question
chart_data = [
    {'Month': 'January', 'Astronomy Observations (hours)': 2, 'Stargazing (hours)': 1, 'Astrophotography (hours)': 3, 'Cosmology Studies (hours)': 4},
    {'Month': 'February', 'Astronomy Observations (hours)': 3, 'Stargazing (hours)': 2, 'Astrophotography (hours)': 4, 'Cosmology Studies (hours)': 5},
    {'Month': 'March', 'Astronomy Observations (hours)': 4, 'Stargazing (hours)': 3, 'Astrophotography (hours)': 5, 'Cosmology Studies (hours)': 6},
    {'Month': 'April', 'Astronomy Observations (hours)': 5, 'Stargazing (hours)': 4, 'Astrophotography (hours)': 6, 'Cosmology Studies (hours)': 7},
    {'Month': 'May', 'Astronomy Observations (hours)': 6, 'Stargazing (hours)': 5, 'Astrophotography (hours)': 7, 'Cosmology Studies (hours)': 8},
    {'Month': 'June', 'Astronomy Observations (hours)': 7, 'Stargazing (hours)': 6, 'Astrophotography (hours)': 8, 'Cosmology Studies (hours)': 9},
    {'Month': 'July', 'Astronomy Observations (hours)': 8, 'Stargazing (hours)': 7, 'Astrophotography (hours)': 9, 'Cosmology Studies (hours)': 10},
    {'Month': 'August', 'Astronomy Observations (hours)': 7, 'Stargazing (hours)': 6, 'Astrophotography (hours)': 8, 'Cosmology Studies (hours)': 9},
    {'Month': 'September', 'Astronomy Observations (hours)': 6, 'Stargazing (hours)': 5, 'Astrophotography (hours)': 7, 'Cosmology Studies (hours)': 8},
    {'Month': 'October', 'Astronomy Observations (hours)': 5, 'Stargazing (hours)': 4, 'Astrophotography (hours)': 6, 'Cosmology Studies (hours)': 7},
    {'Month': 'November', 'Astronomy Observations (hours)': 4, 'Stargazing (hours)': 3, 'Astrophotography (hours)': 5, 'Cosmology Studies (hours)': 6},
    {'Month': 'December', 'Astronomy Observations (hours)': 3, 'Stargazing (hours)': 2, 'Astrophotography (hours)': 4, 'Cosmology Studies (hours)': 5}
]

# Extracting the data for plotting
months = [entry['Month'] for entry in chart_data]
astronomy_observations = [entry['Astronomy Observations (hours)'] for entry in chart_data]
stargazing = [entry['Stargazing (hours)'] for entry in chart_data]
astrophotography = [entry['Astrophotography (hours)'] for entry in chart_data]
cosmology_studies = [entry['Cosmology Studies (hours)'] for entry in chart_data]

# Plotting the data
plt.figure(figsize=(16, 8))

plt.plot(months, astronomy_observations, label='Astronomy Observations', marker='o', linestyle='-', color='#4a90e2')
plt.plot(months, stargazing, label='Stargazing', marker='s', linestyle='--', color='#50e3c2')
plt.plot(months, astrophotography, label='Astrophotography', marker='^', linestyle='-.', color='#f5a623')
plt.plot(months, cosmology_studies, label='Cosmology Studies', marker='d', linestyle=':', color='#e94e77')

# Adding the title and labels
plt.title('Monthly Time Spent on Astronomy & Space Exploration Activities', fontsize=16, pad=20)
plt.xlabel('Month')
plt.ylabel('Time (hours)')
plt.xticks(rotation=45)  # Rotate the x-axis labels for better readability

# Adding annotations
for i, txt in enumerate(astronomy_observations):
    plt.annotate(txt, (months[i], astronomy_observations[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Invert the y-axis
plt.gca().invert_yaxis()

# Adding a legend
plt.legend(loc='upper left')

# Adjust layout to prevent clipping and show the plot
plt.tight_layout()
plt.show()