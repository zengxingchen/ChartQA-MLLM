
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Country': ['USA', 'China', 'Japan', 'Germany', 'India', 'UK', 'France', 'Italy', 'Brazil', 
                'Canada', 'Russia', 'South Korea', 'Australia', 'Spain', 'Mexico', 'Indonesia', 
                'Netherlands', 'Saudi Arabia', 'Turkey', 'Switzerland'],
    'GDP': [21427700, 14342903, 5081770, 3845630, 2875142, 2825208, 2715518, 2000938, 1444736, 
            1736426, 1483496, 1630566, 1392687, 1248904, 1260140, 1058400, 909887, 792966, 
            720101, 824799],
    'UnemploymentRate': [5.2, 4.8, 2.8, 3.5, 6.2, 4.6, 7.9, 9.5, 13.4, 5.9, 5.8, 4.0, 4.2, 15.5, 
                         4.5, 6.5, 4.1, 6.4, 12.9, 4.2]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 12))
sns.scatterplot(data=df, x='GDP', y='UnemploymentRate', 
                palette=['#1f77b4', '#ff7f0e'], 
                s=150)  # Adjusted marker size

plt.title('Relationship between GDP and Unemployment Rate in Various Countries', fontsize=20, pad=25)
plt.xlabel('GDP (in billions $)', fontsize=16)
plt.ylabel('Unemployment Rate (%)', fontsize=16)

plt.show()