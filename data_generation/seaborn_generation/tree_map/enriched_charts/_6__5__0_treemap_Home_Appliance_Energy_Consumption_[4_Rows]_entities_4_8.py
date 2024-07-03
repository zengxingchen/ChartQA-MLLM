
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    'Event': ['Satellite Launch', 'Astronomy Lecture', 'Meteor Shower Viewing', 'Space Museum Visit', 'Rocket Building Workshop',
              'Planetarium Show', 'Astrophotography Contest', 'Space Art Exhibition', 'Star Gazing Night', 'Mars Rover Simulation',
              'Space Quiz Competition', 'Alien Movie Screening', 'Telescope Workshop', 'Astronaut Meet & Greet', 'Comet Chasing',
              'Space Technology Fair', 'Lunar Eclipse Viewing', 'Space Camp', 'Black Hole Presentation', 'Astrobiology Seminar'],
    'Attendance': [5000, 12000, 8000, 15000, 7000, 
                   20000, 11000, 14000, 13000, 10000,
                   6000, 17000, 9000, 2500, 4000,
                   16000, 22000, 19000, 18000, 30000]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16,12))

colors = ['#3b5998', '#8b9dc3', '#dfe3ee', '#f7f7f7', '#ffffff', 
          '#ff6f61', '#6b5b95', '#feb236', '#d64161', '#ff7b25',
          '#4a7c59', '#d4ac6e', '#6b5b95', '#feb236', '#d64161',
          '#ff7b25', '#4a7c59', '#d4ac6e', '#ff6f61', '#8b9dc3']

squarify.plot(sizes=df['Attendance'], label=df['Event'], color=colors, alpha=0.8)

plt.title('Event Attendance in Astronomy & Space Exploration', fontsize=18, pad=20)
plt.axis('off')

plt.show()