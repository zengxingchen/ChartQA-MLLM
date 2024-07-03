
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    'Topic': ['Ancient Civilizations Documentary', 'Renaissance Art Workshop', 'World War II History Lecture', 'Archaeological Dig Simulation', 'Medieval History Fair', 
              'Modern Art Exhibition', 'Greek Mythology Reading', 'Famous Historical Trials Discussion', 'Ancient Literature Class', 'Historical Sites Virtual Tour', 
              'Historic Costume Design Workshop', 'Victorian Era Society Talk', 'Historical Documentaries Film Festival', 'War History Trivia Night', 'Colonial America Reenactment', 
              'Ancient Egypt Presentation', 'Cultural Heritage Conservation Workshop', 'Revolutionary War Debate', 'History of Science Seminar', 'Ancient Philosophers Seminar'],
    'Views': [3200, 4600, 8900, 7200, 5400, 
              7800, 3600, 6200, 4900, 8500,
              4300, 3900, 9700, 5100, 5600,
              6300, 8800, 6800, 7600, 5900]
}

df = pd.DataFrame(data)

plt.figure(figsize=(20,16))

colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0', 
          '#ffb3e6','#c4e17f','#ffdb58','#ffab9a','#d0e1f9',
          '#c6eff7','#d2d0f5','#f6a4b3','#c6b79b','#f4dcae',
          '#c6f5d3','#ffd1c1','#b0efeb','#f7dcb1','#c1f5c6']

squarify.plot(sizes=df['Views'], label=df['Topic'], color=colors, alpha=0.8)

plt.title('Popularity of History & Archaeology Events', fontsize=24, pad=40)
plt.axis('off')

plt.show()