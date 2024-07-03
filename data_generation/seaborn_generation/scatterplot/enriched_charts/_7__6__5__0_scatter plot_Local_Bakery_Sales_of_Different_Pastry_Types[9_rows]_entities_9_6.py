
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

data = """
Exercise_Type,Exercise_Duration,Stress_Level
Yoga,30,3
Running,60,6
Cycling,45,5
Swimming,90,4
Gym_Workout,75,7
Hiking,120,3
Meditation,20,2
Dance,50,5
Pilates,40,4
Boxing,60,8
CrossFit,80,7
Basketball,70,6
Football,90,7
Tennis,55,5
Badminton,35,4
Aerobics,50,6
Weightlifting,65,7
Walking,40,3
Zumba,45,5
Rock_Climbing,110,8
"""

df = pd.read_csv(StringIO(data))

plt.figure(figsize=(16, 9))
scatter = sns.scatterplot(
    data=df, 
    x="Exercise_Duration", 
    y="Stress_Level", 
    palette=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"],
    edgecolor="k", s=150
)

scatter.set_title('Health & Psychology: Exercise Duration vs. Stress Level', fontsize=22, pad=30)
scatter.set_xlabel('Exercise Duration (minutes)', fontsize=18)
scatter.set_ylabel('Stress Level', fontsize=18)

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

sns.despine()

plt.show()