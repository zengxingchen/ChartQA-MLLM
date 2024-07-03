
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

data = """
Country,GDP_Per_Capita,Life_Expectancy
United States,62641,79
China,10261,76
Japan,40566,84
Germany,46476,81
India,2100,70
United Kingdom,42500,81
France,40449,82
Brazil,9000,76
Italy,35500,83
Canada,46300,82
South Korea,33850,83
Russia,11500,73
Australia,57500,83
Spain,29000,83
Mexico,9700,76
Indonesia,4135,72
Netherlands,52300,82
Saudi Arabia,23100,75
Turkey,11100,77
Switzerland,81450,83
Sweden,54700,83
Nigeria,2250,55
Argentina,10250,76
Poland,15100,78
Norway,75000,83
Egypt,3100,73
Belgium,47200,81
South Africa,6000,64
Colombia,5800,77
Thailand,7290,77
Iran,2800,76
Philippines,3500,71
Vietnam,2750,74
Bangladesh,2060,73
Pakistan,1500,67
Malaysia,11100,76
Chile,15100,80
Singapore,65500,84
Greece,22500,82
Portugal,22250,81
New Zealand,43200,82
Israel,44000,83
Ireland,83300,82
Austria,50900,82
Ukraine,3200,71
Hungary,16100,76
Romania,14200,75
Czech Republic,23900,79
Finland,49700,82
Denmark,62700,81
Ireland,83400,82
"""

df = pd.read_csv(StringIO(data))

plt.figure(figsize=(16, 10))
scatter = sns.scatterplot(
    data=df, 
    x="GDP_Per_Capita", 
    y="Life_Expectancy", 
    palette=sns.color_palette(["#FF5733", "#33C3FF"]),
    edgecolor="w", s=100
)

scatter.set_title('Economic Indicators: GDP Per Capita vs. Life Expectancy', fontsize=18, pad=20)
scatter.set_xlabel('GDP Per Capita (USD)', fontsize=14)
scatter.set_ylabel('Life Expectancy (Years)', fontsize=14)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

sns.despine()

plt.show()