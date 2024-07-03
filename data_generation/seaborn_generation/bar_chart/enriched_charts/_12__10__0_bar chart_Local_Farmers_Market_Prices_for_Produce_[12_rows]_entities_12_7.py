
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Sport': ['Basketball', 'Soccer', 'Tennis', 'Swimming', 'Running', 'Cycling', 'Boxing', 'Gymnastics', 'Skiing', 'Baseball', 'Hockey', 'Rowing', 'Volleyball', 'Rugby', 'Golf', 'Badminton', 'Cricket', 'Skateboarding', 'Surfing'],
    'Average_Score': [85, 78, 90, 82, 88, 74, 81, 87, 79, 83, 77, 86, 80, 76, 84, 80, 79, 77, 82]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 10))
sns.barplot(x='Sport', y='Average_Score', data=df, palette=["#FF6347", "#4682B4", "#FFD700", "#32CD32", "#8A2BE2", "#FF69B4", "#B22222", "#5F9EA0", "#FF4500", "#DA70D6", "#7FFF00", "#DC143C", "#00FFFF", "#D2691E", "#6495ED", "#FF8C00", "#9932CC", "#8B4513", "#00FA9A"], linewidth=1.2, width=0.6)

plt.title('Average Scores in Different Sports', fontsize=18, pad=20)
plt.xlabel('Sport', fontsize=14)
plt.ylabel('Average Score', fontsize=14)
plt.xticks(rotation=45)
plt.grid(axis='y')

plt.show()