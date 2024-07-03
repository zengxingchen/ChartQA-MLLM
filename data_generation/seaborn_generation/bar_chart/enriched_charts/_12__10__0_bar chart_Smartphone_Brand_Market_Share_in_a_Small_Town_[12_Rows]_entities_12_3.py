
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Destination': ['Paris', 'New York', 'Tokyo', 'Sydney', 'Rome', 'Barcelona', 
                    'London', 'Dubai', 'Bangkok', 'Hong Kong', 'Cape Town', 
                    'Istanbul', 'Rio de Janeiro', 'Amsterdam', 'Venice'],
    'Popularity Score': [92, 88, 95, 90, 85, 87, 93, 89, 86, 91, 84, 83, 82, 94, 81]
}

df = pd.DataFrame(data)

f, ax = plt.subplots(figsize=(14, 8))

palette = ['#3498db', '#e74c3c', '#2ecc71', '#9b59b6', '#f1c40f', '#e67e22', 
           '#1abc9c', '#34495e', '#d35400', '#c0392b', '#8e44ad', '#2c3e50', 
           '#7f8c8d', '#2980b9', '#27ae60']

sns.barplot(y='Destination', x='Popularity Score', data=df, palette=palette, ax=ax, 
            orient='h', dodge=False)

ax.set(xlim=(0, 100), xlabel="Popularity Score", ylabel="Destination")
ax.set_title('Popularity Scores of Travel Destinations', pad=20)

for container in ax.containers:
    ax.bar_label(container, label_type='edge', padding=3)

plt.show()