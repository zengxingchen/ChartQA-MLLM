
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Country': ['China', 'USA', 'India', 'Russia', 'Japan', 'Germany', 'Iran', 'South Korea', 'Saudi Arabia', 'Canada'],
    'CO2_Emissions': [11000, 5100, 2600, 1700, 1200, 800, 780, 650, 600, 580]
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 6))

sns.barplot(
    x='Country',
    y='CO2_Emissions',
    data=df,
    palette=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6','#c4e17f','#ff6666','#fcbdbd','#99e6e6'],
    dodge=False
)

plt.title('CO2 Emissions by Country')
plt.xlabel('Country')
plt.ylabel('CO2 Emissions (Mt)')

for patch in plt.gca().patches:
    patch.set_width(0.5)

plt.xticks(rotation=45)

plt.show()