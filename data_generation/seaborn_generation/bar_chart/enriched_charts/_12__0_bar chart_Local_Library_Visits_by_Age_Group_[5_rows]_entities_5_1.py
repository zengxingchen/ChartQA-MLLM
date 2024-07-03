import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'City': [
        'Tokyo', 'New York', 'Berlin', 'Sydney', 'Toronto', 
        'Paris', 'Moscow', 'Dubai', 'Singapore', 'Los Angeles', 
        'Hong Kong', 'Buenos Aires', 'Mexico City', 'Beijing', 'Cape Town'
    ],
    'Average Temperature (°C)': [
        16.5, 12.6, 10.5, 18.3, 9.2, 
        11.7, 5.8, 27.2, 26.9, 18.6, 
        23.6, 16.2, 15.9, 12.1, 17.1
    ]
}
df = pd.DataFrame(data)

sns.set(style="whitegrid")
plt.figure(figsize=(10, 8))

barplot = sns.barplot(
    x="City",
    y="Average Temperature (°C)",
    data=df,
    palette=[
        '#FF6347', '#4682B4', '#8A2BE2', '#5F9EA0', '#D2691E', 
        '#FF7F50', '#6495ED', '#DC143C', '#00CED1', '#FFD700', 
        '#ADFF2F', '#4B0082', '#FF4500', '#2E8B57', '#DAA520'
    ]
)

barplot.set_title('Average Annual Temperature by City', fontsize=16)
barplot.set(xlabel="City", ylabel="Average Temperature (°C)")

for bar in barplot.containers[0]:
    bar.set_width(0.6)

barplot.bar_label(barplot.containers[0], fmt='%.1f', fontsize=10, padding=5)

plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()