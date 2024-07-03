
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Month": ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"],
    "NumberOfTourists": [50, 65, 80, 95, 120, 150, 160, 155, 130, 110, 85, 60]
}
df = pd.DataFrame(data)
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

sns.set_style("whitegrid")

plt.figure(figsize=(14, 8))
area_chart = sns.lineplot(data=df, x='Month', y='NumberOfTourists', color="#1f77b4")

plt.fill_between(data['Month'], data['NumberOfTourists'], color="#aec7e8")

area_chart.set_title('Monthly Tourist Visits for 2023', fontsize=18)
area_chart.set_xlabel('Month', fontsize=12)
area_chart.set_ylabel('Number of Tourists (in thousands)', fontsize=12)

for i, tourists in enumerate(df['NumberOfTourists']):
    plt.text(df['Month'][i], tourists, str(tourists), horizontalalignment='center')

plt.tight_layout()
plt.show()