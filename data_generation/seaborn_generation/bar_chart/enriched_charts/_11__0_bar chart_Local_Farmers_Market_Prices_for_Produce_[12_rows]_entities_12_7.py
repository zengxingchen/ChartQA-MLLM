
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Sport': ['Soccer', 'Basketball', 'Baseball', 'Tennis', 'Running', 'Cycling', 'Swimming', 'Gymnastics', 'Boxing', 'Wrestling', 'Golf', 'Skiing', 'Skating', 'Hiking', 'Surfing'],
    'Participants': [25, 40, 35, 22, 50, 30, 28, 15, 20, 18, 24, 17, 27, 34, 23]
}

df = pd.DataFrame(data)

plt.figure(figsize=(10, 14))
sns.barplot(x='Participants', y='Sport', data=df, palette=["#FF5733", "#33FF57", "#3357FF", "#F033FF", "#33FFF3", "#FFC733", "#FF3333", "#3FFF33", "#FF33FF", "#335FFF", "#33FFC7", "#FFF333", "#FF3399", "#C7FF33", "#5733FF"], linewidth=2.0)

plt.title('Number of Participants in Various Sports', fontsize=16, pad=20)
plt.xlabel('Participants', fontsize=14)
plt.ylabel('Sport', fontsize=14)
plt.grid(axis='x')

plt.show()