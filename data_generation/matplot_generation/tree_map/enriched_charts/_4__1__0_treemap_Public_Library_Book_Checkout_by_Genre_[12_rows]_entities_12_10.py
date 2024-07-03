
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    'Continent': ['North America', 'North America', 'North America', 'Europe', 'Europe', 'Europe', 'Europe', 'Europe',
                  'Asia', 'Asia', 'Asia', 'South America', 'South America', 'Africa', 'Oceania'],
    'League': ['NFL', 'MLB', 'NBA', 'English Premier League', 'La Liga', 'Bundesliga', 'Serie A', 'Ligue 1',
               'IPL', 'CSL', 'K League', 'Brazilian Serie A', 'Argentinian Primera Division', 
               'South African Premier Division', 'A-League'],
    'Annual Revenue (in billion USD)': [16, 10, 8, 6.5, 5, 4.5, 3.5, 2.5, 6, 1.5, 1, 1.2, 0.8, 0.5, 0.4]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 12))
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF', '#33FFA6',
          '#FF8C33', '#8C33FF', '#FF3333', '#33FFBD', '#FF3333', '#FF3333',
          '#FF3333', '#FF3333', '#FF3333']
squarify.plot(sizes=df['Annual Revenue (in billion USD)'], label=df['League'], color=colors, alpha=0.7)
plt.title('Annual Revenue of Top Sports Leagues Worldwide', fontsize=18)
plt.axis('off')

plt.show()