
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Country': ['United States', 'China', 'Germany', 'Norway', 'France', 'United Kingdom', 
                'Netherlands', 'Canada', 'Sweden', 'Italy', 'Japan', 'South Korea',
                'Australia', 'Brazil', 'India'],
    'Renewable Energy Investment (Billion USD)': [150, 350, 90, 60, 85, 75, 50, 95, 40, 65, 110, 70, 85, 40, 120],
    'Happiness Index': [7.8, 6.5, 7.2, 7.8, 7.1, 7.3, 7.5, 7.6, 7.9, 6.9, 6.8, 6.7, 7.7, 6.6, 5.8],
    'CO2 Reduction (Million Tonnes)': [80, 220, 50, 20, 45, 40, 18, 30, 15, 28, 55, 35, 32, 38, 70]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 12))
bubble_chart = sns.scatterplot(data=df, 
                               x='Happiness Index', 
                               y='Renewable Energy Investment (Billion USD)', 
                               size='CO2 Reduction (Million Tonnes)', 
                               hue='Country', 
                               palette=["#3498db", "#e74c3c", "#9b59b6", "#2ecc71", 
                                        "#f1c40f", "#e67e22", "#1abc9c", "#34495e",
                                        "#d35400", "#16a085", "#2980b9", "#c0392b",
                                        "#8e44ad", "#27ae60", "#f39c12"],
                               sizes=(50, 1500))

plt.title('Happiness Index vs Renewable Energy Investment and CO2 Reduction')
plt.xlabel('Happiness Index')
plt.ylabel('Renewable Energy Investment (Billion USD)')

bubble_chart.legend(loc='upper right', bbox_to_anchor=(1.25, 1), title='Country')

plt.show()