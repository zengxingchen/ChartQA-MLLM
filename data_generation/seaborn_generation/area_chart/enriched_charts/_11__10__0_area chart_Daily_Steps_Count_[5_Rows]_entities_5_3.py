
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'City': ['Tokyo', 'Delhi', 'Shanghai', 'São Paulo', 'Mumbai', 'Beijing', 'Cairo', 'Dhaka', 'Mexico City', 'Osaka', 'Karachi', 'Chongqing', 'Istanbul', 'Buenos Aires', 'Kolkata', 'Kinshasa', 'Lagos', 'Manila', 'Rio de Janeiro', 'Guangzhou'],
    'Population (Thousands)': [9273, 16787, 26317, 12107, 20181, 19612, 20076, 19633, 9201, 8840, 15400, 30165, 15067, 15600, 14800, 15053, 14880, 13939, 6748, 18613]
}

df = pd.DataFrame(data)

colors = ["#4c72b0"]

plt.figure(figsize=(14, 10))
ax = sns.lineplot(x='City', y='Population (Thousands)', data=df, color=colors[0])
ax.fill_between(df['City'], df['Population (Thousands)'], color=colors[0], alpha=0.3)

for j, point in df.iterrows():
    ax.text(point['City'], point['Population (Thousands)'], str(point['Population (Thousands)']), 
            ha='center', va='bottom', rotation=90, fontsize=8)

ax.set_title('Population of Major Cities Around the World (Thousands)', fontsize=20)
ax.set_xlabel('City', fontsize=14)
ax.set_ylabel('Population (Thousands)', fontsize=14)

plt.xticks(rotation=90)
plt.tight_layout()
plt.show()