
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Country': ['France', 'Spain', 'USA', 'China', 'Italy', 'Turkey', 'Mexico', 'Germany', 'Thailand', 'UK', 
                'Japan', 'Austria', 'Greece', 'Malaysia', 'Russia', 'Canada', 'Netherlands', 'Poland', 
                'Saudi Arabia', 'South Korea', 'Switzerland', 'Australia', 'Brazil', 'South Africa'],
    'Number_of_Tourists_Million': [89.4, 83.7, 79.3, 65.7, 64.5, 51.2, 45.0, 39.6, 39.8, 36.3, 
                                   31.2, 30.8, 30.1, 26.1, 24.5, 22.1, 19.0, 18.4, 17.5, 17.2, 
                                   11.7, 9.4, 6.6, 5.0],
    'Travel_Expenditure_Billion': [211.0, 81.8, 254.0, 130.0, 44.2, 29.5, 24.6, 43.9, 61.0, 38.0, 
                                   41.1, 18.9, 17.7, 20.3, 8.9, 22.8, 18.6, 10.7, 22.4, 21.7, 
                                   20.8, 22.3, 6.0, 8.7]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 10))
scatterplot = sns.scatterplot(data=df, x='Number_of_Tourists_Million', y='Travel_Expenditure_Billion', 
                              palette=['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#FF69B4', '#8A2BE2', '#00CED1', '#FF4500'])

scatterplot.set_title('Number of Tourists vs. Travel Expenditure by Country')
scatterplot.set_xlabel('Number of Tourists (Million)')
scatterplot.set_ylabel('Travel Expenditure (Billion USD)')
plt.show()