
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

data = """
Topic,Number_of_Articles,Number_of_Readers
Ancient_Civilizations,50,10000
Medieval_History,30,8000
Renaissance_Art,25,7000
Industrial_Revolution,40,9500
Modern_History,60,12000
Archaeological_Discoveries,35,9000
Cultural_Anthropology,45,11000
Historical_Figures,55,10500
Military_History,20,6000
World_War_II,50,10000
Ancient_Monuments,28,7500
Colonial_History,22,6700
History_of_Science,33,9200
Historical_Literature,27,7400
Political_History,48,10800
Economic_History,37,9500
Art_History,42,10000
Religious_History,30,8000
Historiography,18,5800
Public_History,25,7200
Social_History,39,9000
Oral_History,32,8600
Historical_Methodology,21,6500
Historians_and_Scholarship,26,7800
"""

df = pd.read_csv(StringIO(data))

plt.figure(figsize=(18, 10))
scatter = sns.scatterplot(
    data=df, 
    x="Number_of_Articles", 
    y="Number_of_Readers", 
    palette=["#e41a1c", "#377eb8", "#4daf4a", "#984ea3", "#ff7f00", "#ffff33", "#a65628", "#f781bf", "#999999", "#66c2a5", "#fc8d62", "#8da0cb", "#e78ac3", "#a6d854", "#ffd92f", "#e5c494", "#b3b3b3"],
    edgecolor="k", s=200
)

scatter.set_title('Popular Topics in History & Archaeology: Number of Articles vs. Number of Readers', fontsize=22, pad=30)
scatter.set_xlabel('Number of Articles', fontsize=18)
scatter.set_ylabel('Number of Readers', fontsize=18)

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

sns.despine()

plt.show()