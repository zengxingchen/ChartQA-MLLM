
import matplotlib.pyplot as plt

# Table data provided above
data = {
    'Sport': ['Soccer', 'Cricket', 'Basketball', 'Tennis', 'Golf', 'Baseball', 'American Football', 'Rugby', 'Ice Hockey', 'Badminton', 'Table Tennis', 'Volleyball', 'Swimming', 'Athletics', 'Boxing', 'Cycling', 'Skiing', 'MMA', 'Snooker', 'Esports'],
    'Popularity (millions)': [4000, 2500, 2400, 1500, 1200, 500, 450, 200, 150, 300, 875, 900, 1000, 800, 400, 450, 135, 500, 500, 1000],
    'Avg. Duration (mins)': [90, 360, 48, 180, 240, 210, 60, 80, 60, 60, 30, 90, 60, 30, 36, 240, 150, 25, 90, 60],
    'Annual Revenue (billions)': [50, 6.8, 6.6, 6.4, 11, 11.5, 12, 2.4, 4.8, 1.1, 1.5, 2.6, 4.2, 3.5, 1.6, 3.2, 1.2, 1.5, 0.9, 1.4]
}

# Create figure and axis
fig, ax = plt.subplots(figsize=(16, 9))

# Scatter plot for each sport
for i in range(len(data['Sport'])):
    ax.scatter(data['Popularity (millions)'][i], data['Avg. Duration (mins)'][i], 
               s=data['Annual Revenue (billions)'][i]*20,  # Bubble sizes
               label='{}'.format(data['Sport'][i]),
               alpha=0.6, edgecolors='w',
               linewidth=1.5)

# Custom colors
colors = ['#FF4500', '#FFD700', '#8A2BE2', '#7FFF00', '#DC143C', 
          '#00FFFF', '#FF1493', '#FFD700', '#8A2BE2', '#32CD32', 
          '#00CED1', '#FF69B4', '#7FFFD4', '#FF6347', '#4682B4', 
          '#ADFF2F', '#FF00FF', '#D2691E', '#9400D3', '#00BFFF']

# Apply the colors to the scatter plot
for i, dot in enumerate(ax.collections):
    dot.set_facecolor(colors[i % len(colors)])

# Title and labels
ax.set_title('Bubble Chart: Sports Popularity, Duration, and Revenue', pad=20)
ax.set_xlabel('Popularity (millions)')
ax.set_ylabel('Avg. Duration (mins)')

# Grid and legend
ax.grid(True)
ax.legend(title='Sports', loc='upper right')

plt.tight_layout()
plt.show()