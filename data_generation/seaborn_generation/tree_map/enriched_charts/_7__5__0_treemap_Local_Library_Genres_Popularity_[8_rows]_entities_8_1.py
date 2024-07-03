
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import squarify

# Creating a DataFrame from the provided dataset
data = {
    'Continent': ['Asia', 'Asia', 'Asia', 'Asia', 'Asia', 'Europe', 'Europe', 'Europe', 'Europe', 'Europe',
                  'Africa', 'Africa', 'Africa', 'Africa', 'Africa', 'Americas', 'Americas', 'Americas', 'Americas',
                  'Americas', 'Oceania', 'Oceania', 'Oceania', 'Oceania', 'Oceania'],
    'Country': ['China', 'India', 'Japan', 'South Korea', 'Indonesia', 'Germany', 'United Kingdom',
                'France', 'Italy', 'Russia', 'Nigeria', 'South Africa', 'Egypt', 'Algeria', 'Morocco',
                'United States', 'Brazil', 'Canada', 'Mexico', 'Argentina', 'Australia', 'New Zealand',
                'Papua New Guinea', 'Fiji', 'Samoa'],
    'Expenditure': [25400, 18700, 23000, 19000, 11000, 45000, 32000, 28000, 25000, 20000,
                    15000, 12000, 10000, 9000, 8000, 60000, 28000, 27000, 21000, 18000,
                    30000, 20000, 10000, 8000, 5000]
}

df = pd.DataFrame(data)

# Plotting the treemap
plt.figure(figsize=(26, 16))
colors = ["#FF5733", "#33FF57", "#3357FF", "#FF33A6", "#FF8C33", "#33FF8C",
          "#8C33FF", "#FF3333", "#33FF33", "#3333FF", "#FF5733", "#33FF57",
          "#3357FF", "#FF33A6", "#FF8C33", "#33FF8C", "#8C33FF", "#FF3333",
          "#33FF33", "#3333FF", "#FF5733", "#33FF57", "#3357FF", "#FF33A6", "#FF8C33"]

# Using squarify to plot treemap
squarify.plot(sizes=df['Expenditure'], label=df['Country'], color=colors, alpha=0.8)
plt.title('Art & Design Expenditure by Country', fontsize=28, y=1.05)
plt.axis('off')
plt.show()