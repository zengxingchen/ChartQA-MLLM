import pandas as pd
import matplotlib.pyplot as plt
import squarify

data = {
    'Country': ['United States', 'China', 'India', 'United Kingdom', 'Germany', 'Japan', 'France', 'Canada',
                'Italy', 'Australia', 'South Korea', 'Spain', 'Netherlands', 'Brazil', 'Switzerland', 'Sweden',
                'Russia', 'Israel', 'Belgium', 'Norway', 'Denmark', 'Finland', 'Ireland', 'New Zealand', 'Portugal'],
    'PublicationCount': [300, 280, 240, 230, 220, 200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
}

df = pd.DataFrame(data)

plt.figure(figsize=(20, 12))
colors = ["#e6194b", "#3cb44b", "#ffe119", "#4363d8", "#f58231", "#911eb4", "#46f0f0", "#f032e6", "#bcf60c",
          "#fabebe", "#008080", "#e6beff", "#9a6324", "#fffac8", "#800000", "#aaffc3", "#808000", "#ffd8b1",
          "#000075", "#808080", "#ffffff", "#000000", "#ff6666", "#66b3ff", "#99ff99"]

squarify.plot(sizes=df['PublicationCount'], label=df['Country'], color=colors, alpha=0.8)
plt.title('Research Publications by Country', fontsize=24, pad=20)
plt.axis('off')
plt.show()