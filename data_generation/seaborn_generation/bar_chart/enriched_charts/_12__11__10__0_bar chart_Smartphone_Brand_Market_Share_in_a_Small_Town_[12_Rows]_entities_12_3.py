
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Disorder': ['Anxiety', 'Depression', 'Bipolar', 'Schizophrenia', 'OCD', 'PTSD', 
                 'Eating Disorders', 'ADHD', 'Autism', 'Substance Abuse', 'Personality Disorders'],
    'Prevalence': [18.1, 6.7, 2.8, 1.1, 1.2, 3.6, 5.0, 4.4, 1.7, 7.7, 9.1]
}

df = pd.DataFrame(data)

f, ax = plt.subplots(figsize=(12, 6))

palette = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', 
           '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#ffbb78']

sns.barplot(x='Disorder', y='Prevalence', data=df, palette=palette, ax=ax, width=0.6)

ax.set(ylim=(0, 20), xlabel="Mental Health Disorder", ylabel="Prevalence (%)")
ax.set_title('Prevalence of Mental Health Disorders in the Population', fontsize=16, pad=20)

for container in ax.containers:
    ax.bar_label(container, label_type='edge', padding=3, fontsize=10)

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()