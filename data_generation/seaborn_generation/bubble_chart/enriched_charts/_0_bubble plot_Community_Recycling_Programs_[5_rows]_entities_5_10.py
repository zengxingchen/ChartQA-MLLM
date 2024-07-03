
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Dataframe creation from the provided table data
data = {
    'Country': ['United States', 'China', 'Japan', 'Germany', 'India',
                'United Kingdom', 'France', 'Brazil', 'Italy', 'Canada',
                'Russia', 'South Korea', 'Spain', 'Australia', 'Mexico',
                'Indonesia', 'Netherlands', 'Saudi Arabia', 'Turkey', 'Switzerland'],
    'GDP': [21433226, 14342903, 5081770, 3845630, 2875142,
            2827114, 2715518, 1839767, 2001241, 1736426,
            1709824, 1642381, 1419042, 1392687, 1220695,
            1119190, 907050, 793689, 754041, 703082],
    'Population': [328200000, 1393000000, 126500000, 83100000, 1353000000,
                   66650000, 67060000, 209500000, 60500000, 37590000,
                   145900000, 51270000, 46940000, 25460000, 127600000,
                   267700000, 17180000, 34270000, 83430000, 8585000],
    'LifeExpectancy': [78.9, 76.7, 84.6, 81.0, 69.7,
                       81.2, 82.5, 75.9, 83.4, 81.9,
                       72.7, 83.0, 83.4, 83.3, 75.1,
                       71.5, 81.9, 75.1, 75.8, 83.7],
    'Region': ['North America', 'Asia', 'Asia', 'Europe', 'Asia',
               'Europe', 'Europe', 'South America', 'Europe', 'North America',
               'Europe/Asia', 'Asia', 'Europe', 'Oceania', 'North America',
               'Asia', 'Europe', 'Asia', 'Asia/Europe', 'Europe']
}

df = pd.DataFrame(data)

# Bubble chart with seaborn
plt.figure(figsize=(14, 8))
bubble = sns.scatterplot(data=df, x="GDP", y="LifeExpectancy", size="Population", 
                         hue="Country", palette=sns.color_palette(["#FF5733", "#33FF57", "#3357FF", "#FF33A7", "#FF8333",
                                                                  "#33FFF5", "#8333FF", "#33FF8A", "#F5FF33", "#A733FF",
                                                                  "#FF333E", "#33C1FF", "#3CFF33", "#FF9E33", "#A0FF33",
                                                                  "#33D4FF", "#FF3380", "#5AFF33", "#FFB833", "#8D33FF"]),
                         sizes=(100, 2000), alpha=0.7, edgecolor="w", linewidth=0.5)

# Adjust the legend
bubble.legend(loc='upper left', bbox_to_anchor=(1.05, 1), borderaxespad=0)

# Titles and labels
plt.title('GDP, Population, and Life Expectancy of 20 Largest Economies', fontsize=18)
plt.xlabel('Gross Domestic Product (GDP) in US$ Billion', fontsize=12)
plt.ylabel('Life Expectancy in Years', fontsize=12)

plt.show()