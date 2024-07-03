import pandas as pd
import matplotlib.pyplot as plt
import squarify

data = {
    'Continent': ['Asia', 'Asia', 'Asia', 'Asia', 'Asia', 'Europe', 'Europe', 'Europe', 'Europe', 'Europe', 'Africa', 'Africa', 'Africa', 'Africa', 'Africa', 'Americas', 'Americas', 'Americas', 'Americas', 'Americas', 'Oceania', 'Oceania', 'Oceania', 'Oceania', 'Oceania', 'Europe', 'Africa', 'Americas', 'Asia'],
    'Country': ['China', 'India', 'Indonesia', 'Pakistan', 'Bangladesh', 'Russia', 'Germany', 'United Kingdom', 'France', 'Italy', 'Nigeria', 'Ethiopia', 'Egypt', 'DR Congo', 'Tanzania', 'United States', 'Brazil', 'Mexico', 'Colombia', 'Argentina', 'Australia', 'Papua New Guinea', 'New Zealand', 'Fiji', 'Samoa', 'Spain', 'Kenya', 'Canada', 'Japan'],
    'Population': [1439323776, 1380004385, 273523615, 220892340, 164689383, 145934462, 83783942, 67886011, 65273511, 60461826, 206139589, 114963588, 102334404, 89561403, 59734218, 331002651, 212559417, 128932753, 50882891, 45195774, 25499884, 8947024, 4822233, 896445, 198414, 46754778, 53771296, 37742154, 126476461]
}

df = pd.DataFrame(data)

plt.figure(figsize=(24, 14))
colors = ["#FF5733", "#33FF57", "#3357FF", "#FF33A6", "#A633FF", "#FF5733", "#33FF57", "#3357FF", "#FF33A6", "#A633FF",
          "#FF5733", "#33FF57", "#3357FF", "#FF33A6", "#A633FF", "#FF5733", "#33FF57", "#3357FF", "#FF33A6", "#A633FF",
          "#FF5733", "#33FF57", "#3357FF", "#FF33A6", "#A633FF", "#FF5733", "#33FF57", "#3357FF", "#FF33A6"]

squarify.plot(sizes=df['Population'], label=df['Country'], color=colors, alpha=0.8)
plt.title('Population Distribution by Country and Continent', fontsize=26, pad=30)
plt.axis('off')
plt.show()