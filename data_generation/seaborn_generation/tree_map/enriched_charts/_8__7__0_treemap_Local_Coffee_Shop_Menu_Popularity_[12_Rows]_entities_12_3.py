
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    'Country': ['Japan', 'Switzerland', 'Singapore', 'Australia', 'Spain', 
                'Iceland', 'Italy', 'Israel', 'Sweden', 'France', 
                'Norway', 'Canada', 'South Korea', 'New Zealand', 
                'Netherlands', 'Luxembourg', 'Germany', 'United Kingdom', 
                'Finland', 'Austria', 'Ireland', 'Belgium', 'Portugal', 
                'Denmark', 'United States'],
    'Life Expectancy': [84.2, 83.8, 83.6, 83.4, 83.2, 82.9, 82.8, 82.6, 
                        82.4, 82.3, 82.2, 82.1, 82.0, 81.8, 81.7, 81.5, 
                        81.4, 81.3, 81.1, 81.0, 80.9, 80.8, 80.6, 80.5, 78.9]
}

df = pd.DataFrame(data)

colors = ['#e6194B', '#3cb44b', '#ffe119', '#4363d8', '#f58231', 
          '#911eb4', '#42d4f4', '#f032e6', '#bfef45', '#fabed4', 
          '#469990', '#dcbeff', '#9A6324', '#fffac8', '#800000', 
          '#aaffc3', '#808000', '#ffd8b1', '#000075', '#a9a9a9', 
          '#000000', '#ff4500', '#2e8b57', '#ff6347', '#4169e1']

plt.figure(figsize=(20, 12))
squarify.plot(sizes=df['Life Expectancy'], label=df['Country'], color=colors, alpha=0.8)
plt.title('Life Expectancy by Country - 2023')
plt.axis('off')
plt.show()