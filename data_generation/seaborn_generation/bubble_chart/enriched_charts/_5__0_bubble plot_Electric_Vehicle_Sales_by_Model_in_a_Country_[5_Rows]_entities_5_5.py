
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Country': ['United States', 'China', 'Germany', 'United Kingdom', 'France', 'Japan', 
                'Canada', 'Australia', 'India', 'Brazil', 'Russia', 'South Korea'],
    'Investment (Billion $)': [1500, 1200, 700, 600, 550, 800, 400, 300, 500, 350, 200, 450],
    'Market Capitalization (Billion $)': [25000, 18000, 3500, 3000, 2800, 4000, 2000, 1500, 2200, 1200, 900, 2100],
    'Dividend Yield (%)': [1.5, 1.3, 2.0, 3.2, 2.8, 2.1, 3.0, 4.5, 1.1, 4.0, 5.0, 1.6]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 9))
bubble_chart = sns.scatterplot(data=df, 
                               x='Investment (Billion $)', 
                               y='Market Capitalization (Billion $)', 
                               size='Dividend Yield (%)', 
                               hue='Country', 
                               palette=["#1f78b4", "#33a02c", "#e31a1c", "#ff7f00", 
                                        "#6a3d9a", "#b15928", "#a6cee3", "#b2df8a",
                                        "#fb9a99", "#fdbf6f", "#cab2d6", "#ffff99"],
                               sizes=(100, 2000))

plt.title('Global Investment vs Market Capitalization and Dividend Yield', pad=20)
plt.xlabel('Investment (Billion $)')
plt.ylabel('Market Capitalization (Billion $)')

bubble_chart.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Country')

plt.show()