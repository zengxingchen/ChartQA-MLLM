
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Country': ['China', 'United States', 'India', 'Russia', 'Japan', 'Germany', 'South Korea', 'Iran', 'Canada', 'Saudi Arabia'],
    'CO2 Emissions (Million Metric Tons)': [10150, 5400, 2650, 1700, 1150, 800, 650, 600, 550, 500]
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 6))

sns.barplot(
    x='Country',
    y='CO2 Emissions (Million Metric Tons)',
    data=df,
    palette=[
        '#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#33FFF6', 
        '#FF33FF', '#FFBD33', '#C70039', '#900C3F', '#581845'
    ],
    linewidth=1.5,
    edgecolor='black'
)

for bar in plt.gca().patches:
    bar.set_width(0.6)

plt.ylabel('CO2 Emissions (Million Metric Tons)')
plt.xlabel('Country')
plt.title('CO2 Emissions by Country in 2023')
plt.xticks(rotation=45)

plt.show()