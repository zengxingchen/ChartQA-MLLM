
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import squarify

data = {
    'Country': ['United States', 'China', 'Japan', 'Germany', 'United Kingdom', 'India', 'France', 'South Korea',
                'Italy', 'Australia', 'Brazil', 'Canada', 'Russia', 'Saudi Arabia', 'Spain', 'Turkey', 'Netherlands',
                'Israel', 'Switzerland', 'Mexico', 'Sweden', 'Indonesia', 'Belgium', 'Thailand', 'Nigeria', 'Poland',
                'Norway', 'United Arab Emirates', 'Argentina', 'Denmark', 'Ireland'],
    'Expenditure': [811, 293, 49, 47, 46, 44, 43, 33, 32, 30, 28, 26, 23, 21, 19, 17, 16, 15, 14, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
}

df = pd.DataFrame(data)

plt.figure(figsize=(28, 16))
colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0", "#ffb3e6",
          "#c2f0c2", "#ff6666", "#66ff66", "#6666ff", "#ffb366", "#b3b3cc",
          "#ff99ff", "#ffccff", "#ccccff", "#ff6666", "#ff9999", "#66b3ff",
          "#99ff99", "#ffcc99", "#c2c2f0", "#ffb3e6", "#c2f0c2", "#ff6666",
          "#66ff66", "#6666ff", "#ffb366", "#b3b3cc", "#ff99ff", "#ffccff", "#ccccff"]

squarify.plot(sizes=df['Expenditure'], label=df['Country'], color=colors, alpha=0.8)
plt.title('Military Expenditure by Country (in billion USD)', fontsize=26)
plt.axis('off')
plt.show()