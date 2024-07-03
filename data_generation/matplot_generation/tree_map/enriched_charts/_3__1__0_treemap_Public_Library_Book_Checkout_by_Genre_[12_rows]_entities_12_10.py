
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    'Category': ['Music', 'Music', 'Music', 'Music', 'Music', 'Music', 'Music', 'Music', 'Music', 
                 'Music', 'Performing Arts', 'Performing Arts', 'Performing Arts', 'Performing Arts',
                 'Performing Arts', 'Performing Arts', 'Performing Arts', 'Performing Arts'],
    'Subcategory': ['Pop', 'Rock', 'Hip Hop', 'Classical', 'Jazz', 'Country', 'EDM', 'Reggae', 
                    'Latin', 'Folk', 'Theater', 'Dance', 'Opera', 'Circus', 'Stand-up Comedy', 
                    'Ballet', 'Magic Shows', 'Street Performance'],
    'Popularity (in million)': [3300, 2500, 2000, 800, 700, 600, 550, 400, 350, 300, 1200, 1100, 
                                500, 450, 400, 350, 300, 250]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 12))
colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4',
          '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff',
          '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1']

squarify.plot(sizes=df['Popularity (in million)'], label=df['Subcategory'], color=colors, alpha=0.8)
plt.title('Popularity of Music & Performing Arts Genres', fontsize=18)
plt.axis('off')

plt.show()