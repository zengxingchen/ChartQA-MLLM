
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"],
    "Vegetarian": [5.2, 4.8, 5.0, 4.5, 4.6, 4.7, 4.4, 4.9, 4.8, 4.7],
    "Vegan": [3.1, 2.9, 3.0, 2.6, 2.7, 2.8, 2.5, 3.0, 2.9, 2.8],
    "Pescatarian": [4.0, 3.8, 4.1, 3.5, 3.6, 3.7, 3.4, 3.9, 3.8, 3.7],
    "Gluten-Free": [2.7, 2.6, 2.8, 2.4, 2.5, 2.6, 2.3, 2.8, 2.7, 2.6],
    "Keto": [3.9, 3.6, 3.7, 3.4, 3.3, 3.5, 3.2, 3.6, 3.5, 3.4]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(16, 12))

bar_height = 0.15

r1 = range(len(df))
r2 = [x + bar_height for x in r1]
r3 = [x + bar_height for x in r2]
r4 = [x + bar_height for x in r3]
r5 = [x + bar_height for x in r4]

ax.barh(r1, df['Vegetarian'], color='#FF6347', edgecolor='white', height=bar_height, label='Vegetarian')
ax.barh(r2, df['Vegan'], color='#4682B4', edgecolor='white', height=bar_height, label='Vegan')
ax.barh(r3, df['Pescatarian'], color='#32CD32', edgecolor='white', height=bar_height, label='Pescatarian')
ax.barh(r4, df['Gluten-Free'], color='#FFD700', edgecolor='white', height=bar_height, label='Gluten-Free')
ax.barh(r5, df['Keto'], color='#8A2BE2', edgecolor='white', height=bar_height, label='Keto')

ax.set_xlabel('Average Daily Meal Preferences', fontsize=15)
ax.set_ylabel('City', fontsize=15)
ax.set_title('Average Daily Meal Preferences by Diet and City', fontsize=18)

ax.set_yticks([r + 2*bar_height for r in range(len(r1))])
ax.set_yticklabels(df['City'])

ax.legend(loc='upper right', bbox_to_anchor=(1,1))
plt.tight_layout()
plt.show()