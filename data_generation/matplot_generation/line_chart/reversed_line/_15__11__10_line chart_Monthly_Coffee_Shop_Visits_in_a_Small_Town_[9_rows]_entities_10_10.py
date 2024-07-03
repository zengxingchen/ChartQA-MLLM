
import matplotlib.pyplot as plt

# Data from the provided chart table
data = [
    {'Month': 'January', 'Rock': 120, 'Classical': 150, 'Jazz': 130, 'Pop': 100, 'Hip-Hop': 110},
    {'Month': 'February', 'Rock': 115, 'Classical': 145, 'Jazz': 125, 'Pop': 105, 'Hip-Hop': 105},
    {'Month': 'March', 'Rock': 110, 'Classical': 140, 'Jazz': 120, 'Pop': 110, 'Hip-Hop': 100},
    {'Month': 'April', 'Rock': 105, 'Classical': 135, 'Jazz': 115, 'Pop': 115, 'Hip-Hop': 95},
    {'Month': 'May', 'Rock': 100, 'Classical': 130, 'Jazz': 110, 'Pop': 120, 'Hip-Hop': 90},
    {'Month': 'June', 'Rock': 95, 'Classical': 125, 'Jazz': 105, 'Pop': 125, 'Hip-Hop': 85},
    {'Month': 'July', 'Rock': 90, 'Classical': 120, 'Jazz': 100, 'Pop': 130, 'Hip-Hop': 80},
    {'Month': 'August', 'Rock': 85, 'Classical': 115, 'Jazz': 95, 'Pop': 135, 'Hip-Hop': 75},
    {'Month': 'September', 'Rock': 80, 'Classical': 110, 'Jazz': 90, 'Pop': 140, 'Hip-Hop': 70},
    {'Month': 'October', 'Rock': 75, 'Classical': 105, 'Jazz': 85, 'Pop': 145, 'Hip-Hop': 65},
    {'Month': 'November', 'Rock': 70, 'Classical': 100, 'Jazz': 80, 'Pop': 150, 'Hip-Hop': 60},
    {'Month': 'December', 'Rock': 65, 'Classical': 95, 'Jazz': 75, 'Pop': 155, 'Hip-Hop': 55}
]

# Extracting month names for the x-axis
months = [entry['Month'] for entry in data]

# Plotting each genre's trend
plt.figure(figsize=(14, 10))
genres = list(data[0].keys())[1:]  # Get genre names skipping the 'Month' key

# Line style settings and markers for each genre
line_styles = ['-', '--', '-.', ':']
markers = ['o', '^', 's', 'D', 'x']
colors = ['#ff6347', '#4682b4', '#32cd32', '#8a2be2', '#ff69b4']

for i, genre in enumerate(genres):
    values = [entry[genre] for entry in data]
    plt.plot(months, values, label=genre, linestyle=line_styles[i % len(line_styles)], marker=markers[i % len(markers)], color=colors[i % len(colors)])
    # Adding annotation for the last data point
    plt.text(months[-1], values[-1], f'{values[-1]}', fontsize=10, color=colors[i % len(colors)])

# Adding titles and labels
plt.title('Monthly Music Genre Popularity in Entertainment & Leisure', pad=20)
plt.xlabel('Month')
plt.ylabel('Popularity (in thousands)')

# Adding grid for readability
plt.grid(True)

# Adding a legend to identify the lines
plt.legend(title='Genres', loc='upper left', bbox_to_anchor=(1, 1))

# Invert the y-axis
plt.gca().invert_yaxis()

# Show the plot
plt.show()