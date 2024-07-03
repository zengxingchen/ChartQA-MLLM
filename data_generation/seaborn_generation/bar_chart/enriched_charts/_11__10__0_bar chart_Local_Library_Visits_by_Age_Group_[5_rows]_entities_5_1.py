
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'City': [
        'Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mexico City',
        'Cairo', 'Mumbai', 'Beijing', 'Dhaka', 'Osaka',
        'New York City', 'Karachi', 'Buenos Aires', 'Chongqing', 'Istanbul',
        'Kolkata', 'Manila', 'Lagos', 'Rio de Janeiro', 'Tianjin',
        'Kinshasa', 'Guangzhou', 'Los Angeles', 'Moscow'
    ],
    'Population': [
        37400068, 29399141, 26317104, 21846507, 21671908,
        20484965, 20185064, 20035455, 19577927, 19222665,
        18804000, 16459451, 14967000, 14838000, 14657434,
        14580600, 13923452, 13900000, 13458000, 13215000,
        13184435, 13080500, 12997400, 12537954
    ]
}
df = pd.DataFrame(data)

sns.set(style="whitegrid")
plt.figure(figsize=(12, 10))

barplot = sns.barplot(
    y="City",
    x="Population",
    data=df,
    palette=[
        '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
        '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
        '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
        '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
        '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'
    ],
    ci=None
)

barplot.set_title('Top Populated Cities in the World (2023)', fontsize=16, pad=20)
barplot.bar_label(barplot.containers[0], fmt='%.0f', fontsize=10)
barplot.set(xlabel="Population", ylabel="City")

for bar in barplot.containers[0]:
    bar.set_height(0.5)

plt.tight_layout()
plt.show()