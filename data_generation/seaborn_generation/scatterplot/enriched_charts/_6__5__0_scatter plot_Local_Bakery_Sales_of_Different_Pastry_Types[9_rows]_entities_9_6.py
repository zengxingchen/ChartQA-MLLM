
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

data = """
Category,Time_Spent,Number_of_Activities
Beach,50,4
Mountain,70,3
City_Tour,100,6
Adventure_Sports,200,2
Museums,150,5
Hiking,120,3
Camping,90,4
Wildlife_Safari,180,1
Cruise,240,2
Road_Trip,130,6
Sightseeing,160,5
Festivals,140,4
Theater,110,3
Concerts,170,4
Amusement_Parks,200,2
Historical_Sites,150,6
Cultural_Events,130,3
Shopping,180,5
Photography,100,4
Food_Tasting,160,6
"""

df = pd.read_csv(StringIO(data))

plt.figure(figsize=(14, 8))
scatter = sns.scatterplot(
    data=df, 
    x="Time_Spent", 
    y="Number_of_Activities", 
    palette=sns.color_palette(["#FF6347", "#4682B4", "#32CD32", "#FFD700", "#FF69B4"]),
    edgecolor="k", s=150
)

scatter.set_title('Travel & Adventure: Time Spent vs. Number of Activities', fontsize=20, pad=20)
scatter.set_xlabel('Time Spent (hours)', fontsize=16)
scatter.set_ylabel('Number of Activities', fontsize=16)

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

sns.despine()

plt.show()