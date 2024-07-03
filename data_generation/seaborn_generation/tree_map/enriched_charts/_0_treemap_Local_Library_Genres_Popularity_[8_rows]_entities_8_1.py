
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import squarify

# Creating a DataFrame from the provided dataset
data = {
    'Continent': ['Asia', 'Asia', 'Asia', 'Asia', 'Asia', 'Europe', 'Europe', 'Europe', 'Europe', 'Europe',
                  'Africa', 'Africa', 'Africa', 'Africa', 'Africa', 'Americas', 'Americas', 'Americas', 'Americas',
                  'Americas', 'Oceania', 'Oceania', 'Oceania', 'Oceania', 'Oceania'],
    'Country': ['China', 'India', 'Indonesia', 'Pakistan', 'Bangladesh', 'Russia', 'Germany', 'United Kingdom',
                'France', 'Italy', 'Nigeria', 'Ethiopia', 'Egypt', 'DR Congo', 'Tanzania', 'United States', 'Brazil',
                'Mexico', 'Colombia', 'Argentina', 'Australia', 'Papua New Guinea', 'New Zealand', 'Fiji', 'Samoa'],
    'Population': [1439323776, 1380004385, 273523615, 220892340, 164689383, 145934462, 83783942, 67886011, 65273511,
                   60461826, 206139589, 114963588, 102334404, 89561403, 59734218, 331002651, 212559417, 128932753,
                   50882891, 45195774, 25499884, 8947024, 4822233, 896445, 198414]
}

df = pd.DataFrame(data)

# Plotting the treemap
plt.figure(figsize=(20, 12))
colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0", "#ffb3e6",
          "#c4e17f", "#76dd1f", "#ffb367", "#ffdaa9", "#6fa8dc", "#d5a6bd",
          "#cfe2f3", "#d9d2e9", "#d0e0e3", "#c9daf8", "#cfe2f3", "#f4cccc",
          "#ea9999", "#6aa84f", "#b6d7a8", "#a4c2f4", "#9fc5e8", "#6d9eeb"]

# Using squarify to plot treemap
squarify.plot(sizes=df['Population'], label=df['Country'], color=colors, alpha=0.7)
plt.title('Population Distribution by Country', fontsize=24)
plt.axis('off')
plt.show()