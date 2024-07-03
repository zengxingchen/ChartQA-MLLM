
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Topic': ['Aristotle', 'Plato', 'Socrates', 'Confucius', 'Kant', 'Nietzsche', 'Descartes', 'Locke', 'Hume', 'Hegel', 
              'Rousseau', 'Marx', 'Sartre', 'Camus', 'Voltaire'],
    'Value': [75, 85, 90, 70, 80, 88, 78, 82, 76, 84, 79, 83, 77, 81, 86]
}

df = pd.DataFrame(data)

f, ax = plt.subplots(figsize=(12, 6))

palette = ['#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600', '#665191', 
           '#a05195', '#d45087', '#f95d6a', '#ff7c43', '#ffa600', '#bc5090', 
           '#003f5c', '#58508d', '#ffa600']

sns.barplot(x='Topic', y='Value', data=df, palette=palette, ax=ax)

ax.set(ylim=(0, 100), xlabel="Philosopher", ylabel="Influence Score")
ax.set_title('Influence Scores of Various Philosophers')

for container in ax.containers:
    ax.bar_label(container, label_type='edge', padding=3)

plt.show()