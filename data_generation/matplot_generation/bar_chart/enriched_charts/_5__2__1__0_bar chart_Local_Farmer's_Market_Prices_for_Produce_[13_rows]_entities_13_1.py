
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"],
    "Infrastructure Investment": [12.5, 11.8, 10.9, 9.8, 9.4, 9.2, 8.7, 8.3, 7.9, 7.5],
    "Healthcare Expenditure": [8.3, 7.9, 7.6, 7.3, 7.0, 6.8, 6.5, 6.2, 6.0, 5.7],
    "Education Funding": [9.2, 8.5, 8.1, 7.8, 7.4, 7.1, 6.8, 6.4, 6.1, 5.8],
    "Defense Budget": [7.6, 6.9, 6.7, 6.3, 6.1, 5.9, 5.7, 5.5, 5.3, 5.1],
    "Research & Development": [8.7, 8.1, 7.8, 7.4, 7.1, 6.8, 6.5, 6.2, 5.9, 5.6]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(14, 10))

bar_width = 0.15

r1 = range(len(df))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]
r4 = [x + bar_width for x in r3]
r5 = [x + bar_width for x in r4]

ax.bar(r1, df['Infrastructure Investment'], color='#1f77b4', edgecolor='white', width=bar_width, label='Infrastructure Investment')
ax.bar(r2, df['Healthcare Expenditure'], color='#ff7f0e', edgecolor='white', width=bar_width, label='Healthcare Expenditure')
ax.bar(r3, df['Education Funding'], color='#2ca02c', edgecolor='white', width=bar_width, label='Education Funding')
ax.bar(r4, df['Defense Budget'], color='#d62728', edgecolor='white', width=bar_width, label='Defense Budget')
ax.bar(r5, df['Research & Development'], color='#9467bd', edgecolor='white', width=bar_width, label='Research & Development')

ax.set_xlabel('City', fontsize=15)
ax.set_ylabel('Billions USD', fontsize=15)
ax.set_title('Government Budget Allocation by City', fontsize=18, pad=20)

ax.set_xticks([r + 2*bar_width for r in range(len(r1))])
ax.set_xticklabels(df['City'])

ax.set_ylim(5, 13)

ax.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.tight_layout()
plt.show()