
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Age Group": ["16-24", "25-34", "35-44", "45-54", "55-64", "65+"],
    "Cardio": [4.0, 3.8, 3.5, 3.2, 2.8, 2.5],
    "Strength": [2.5, 2.8, 3.0, 3.3, 3.5, 3.8],
    "Flexibility": [3.0, 2.7, 2.5, 2.2, 2.0, 1.8],
    "Balance": [2.0, 2.2, 2.5, 2.7, 3.0, 3.2]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(10, 12))

bar_height = 0.2

indices = df.index
r1 = range(len(indices))
r2 = [x + bar_height for x in r1]
r3 = [x + bar_height for x in r2]
r4 = [x + bar_height for x in r3]

ax.barh(r1, df['Cardio'], color='#1E90FF', edgecolor='white', height=bar_height, label='Cardio')
ax.barh(r2, df['Strength'], color='#32CD32', edgecolor='white', height=bar_height, label='Strength')
ax.barh(r3, df['Flexibility'], color='#FFD700', edgecolor='white', height=bar_height, label='Flexibility')
ax.barh(r4, df['Balance'], color='#FF4500', edgecolor='white', height=bar_height, label='Balance')

ax.set_xlabel('Average Hours Per Week', fontsize=15)
ax.set_ylabel('Age Group', fontsize=15)
ax.set_title('Average Weekly Exercise Hours by Age Group and Type', fontsize=18)

ax.set_yticks([r + bar_height for r in range(len(r1))])
ax.set_yticklabels(df['Age Group'])
ax.invert_yaxis()

ax.legend(loc='upper right')
plt.tight_layout()
plt.show()