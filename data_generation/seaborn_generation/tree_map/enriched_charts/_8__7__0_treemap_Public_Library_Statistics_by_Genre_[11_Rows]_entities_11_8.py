
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Create a data frame with new data
df = pd.DataFrame({
    'category': ['Music', 'Music', 'Music', 'Music', 'Music', 'Music', 'Music', 'Music', 
                 'Performing Arts', 'Performing Arts', 'Performing Arts', 'Performing Arts', 
                 'Performing Arts', 'Performing Arts', 'Performing Arts', 'Performing Arts', 
                 'Instruments', 'Instruments', 'Instruments', 'Instruments', 
                 'Instruments', 'Instruments', 'Instruments', 'Instruments', 
                 'Festivals', 'Festivals', 'Festivals', 'Festivals', 
                 'Festivals', 'Festivals', 'Festivals', 'Festivals'],
    'sub_category': ['Rock', 'Jazz', 'Classical', 'Pop', 'Hip Hop', 'Country', 'Electronic', 'Folk', 
                     'Theater', 'Dance', 'Opera', 'Circus', 
                     'Mime', 'Stand-up Comedy', 'Magic Shows', 'Street Performances', 
                     'Guitar', 'Piano', 'Violin', 'Drums', 
                     'Flute', 'Saxophone', 'Trumpet', 'Harp', 
                     'Music Festivals', 'Dance Festivals', 'Theater Festivals', 'Street Festivals', 
                     'Folk Festivals', 'Cultural Festivals', 'Opera Festivals', 'Comedy Festivals'],
    'value': [2200, 1800, 1500, 1400, 1300, 1200, 1100, 1000, 
              2000, 1700, 1600, 900, 
              800, 700, 600, 500, 
              2500, 2400, 2300, 2200, 
              2100, 2000, 1900, 1800, 
              2700, 2600, 2500, 2400, 
              2300, 2200, 2100, 2000]
})

# Create a color list
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', 
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', 
          '#bcbd22', '#17becf', '#1f77b4', '#ff7f0e', 
          '#2ca02c', '#d62728', '#9467bd', '#8c564b', 
          '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', 
          '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', 
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', 
          '#bcbd22', '#17becf', '#1f77b4', '#ff7f0e']

# Plot
plt.figure(figsize=(20, 10))
squarify.plot(sizes=df['value'], label=df['sub_category'], color=colors, alpha=.7)
plt.title('Prevalence of Music & Performing Arts Categories', fontsize=23)
plt.axis('off')
plt.show()