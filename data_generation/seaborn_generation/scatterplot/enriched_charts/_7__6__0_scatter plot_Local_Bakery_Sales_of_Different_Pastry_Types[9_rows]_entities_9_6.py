
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

data = """
Country,Calories_Per_Serving,Fat_Content
Almond,576,50
Apple,52,0.2
Banana,96,0.3
Beef,250,15
Broccoli,55,0.6
Carrot,41,0.2
Chicken,239,14
Egg,155,11
Fish,206,12
Grapes,69,0.4
Lamb,294,21
Lettuce,15,0.2
Mango,60,0.4
Milk,42,1
Orange,43,0.2
Peach,39,0.3
Pork,242,14
Potato,77,0.1
Rice,130,0.3
Spinach,23,0.4
Strawberry,32,0.3
Tomato,18,0.2
Turkey,189,7
Watermelon,30,0.2
Yogurt,59,3.3
"""

df = pd.read_csv(StringIO(data))

plt.figure(figsize=(14, 8))
scatter = sns.scatterplot(
    data=df, 
    x="Calories_Per_Serving", 
    y="Fat_Content", 
    palette=["#FF5733", "#33C3FF", "#28B463", "#FFC300", "#C70039", "#900C3F"],
    edgecolor="w", s=100
)

scatter.set_title('Nutritional Content: Calories vs. Fat Content in Various Foods', fontsize=18, pad=20)
scatter.set_xlabel('Calories Per Serving', fontsize=14)
scatter.set_ylabel('Fat Content (g)', fontsize=14)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

sns.despine()

plt.show()