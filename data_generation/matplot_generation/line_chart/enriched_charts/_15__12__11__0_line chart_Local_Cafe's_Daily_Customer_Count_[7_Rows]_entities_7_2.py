
import matplotlib.pyplot as plt
import pandas as pd

# Data points
dates = pd.date_range(start="2024-01-01", end="2024-01-31")
music_played = [120, 150, 100, 160, 180, 140, 190, 200, 180, 210, 230, 240, 260, 280, 300, 310, 320, 300, 340, 360, 380, 390, 400, 420, 440, 450, 470, 490, 500, 510, 530]

# Create the plot
plt.figure(figsize=(16, 8))
plt.plot(dates, music_played, marker='o', linestyle='-', color='#2E8B57')

# Annotate the highest and lowest music played points
plt.annotate('Highest\n530 minutes', xy=(dates[-1], 530), xytext=(dates[-5], 500),
             arrowprops=dict(facecolor='#8B0000', shrink=0.05), color='#8B0000')
plt.annotate('Lowest\n100 minutes', xy=(dates[2], 100), xytext=(dates[5], 140),
             arrowprops=dict(facecolor='#8B0000', shrink=0.05), color='#8B0000')

# Title and labels
plt.title('Daily Music Played in January 2024', pad=20)
plt.xlabel('Date')
plt.ylabel('Music Played (minutes)')

# Customize the grid
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.gca().invert_yaxis()

# Show the plot
plt.show()