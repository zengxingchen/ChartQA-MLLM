
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Sport': ['Soccer', 'Basketball', 'Tennis', 'Swimming', 'Cycling', 'Running', 'Boxing', 
              'Gymnastics', 'Skiing', 'Surfing', 'Skateboarding', 'Volleyball', 'Rugby', 'Baseball', 'Hockey'],
    'Score': [90, 85, 80, 78, 83, 88, 77, 84, 82, 81, 79, 86, 75, 87, 89]
}

df = pd.DataFrame(data)

f, ax = plt.subplots(figsize=(8, 10))

palette = ['#00429d', '#4771b2', '#73a2c6', '#9ecae1', '#c6dbef', '#deebf7', 
           '#f7fbff', '#ffeda0', '#feb24c', '#fd8d3c', '#fc4e2a', '#e31a1c', 
           '#bd0026', '#800026', '#6a51a3']

sns.barplot(y='Sport', x='Score', data=df, palette=palette, ax=ax)

ax.set(xlim=(0, 100), xlabel="Popularity Score", ylabel="Sport")
ax.set_title('Popularity Scores of Various Sports')

for container in ax.containers:
    ax.bar_label(container, label_type='edge', padding=3)

plt.show()