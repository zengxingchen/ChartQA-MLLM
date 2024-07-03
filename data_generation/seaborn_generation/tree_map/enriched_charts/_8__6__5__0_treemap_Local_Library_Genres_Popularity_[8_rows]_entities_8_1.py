
import pandas as pd
import matplotlib.pyplot as plt
import squarify

data = {
    'Continent': ['Asia', 'Asia', 'Asia', 'Asia', 'Asia', 'Europe', 'Europe', 'Europe', 'Europe', 'Europe',
                  'Africa', 'Africa', 'Africa', 'Africa', 'Africa', 'Americas', 'Americas', 'Americas', 'Americas',
                  'Americas', 'Oceania', 'Oceania', 'Oceania', 'Oceania', 'Oceania', 'Asia', 'Europe', 'Africa', 'Americas', 'Oceania'],
    'Country': ['China', 'India', 'Japan', 'South Korea', 'Indonesia', 'Germany', 'United Kingdom',
                'France', 'Italy', 'Russia', 'Nigeria', 'South Africa', 'Egypt', 'Algeria', 'Morocco',
                'United States', 'Brazil', 'Canada', 'Mexico', 'Argentina', 'Australia', 'New Zealand',
                'Papua New Guinea', 'Fiji', 'Samoa', 'Saudi Arabia', 'Spain', 'Kenya', 'Chile', 'Micronesia'],
    'Biodiversity Index': [85, 80, 70, 65, 95, 75, 70, 80, 78, 85, 90, 85, 70, 65, 75, 88, 95, 82, 78, 80, 85, 90, 95, 75, 70, 65, 80, 85, 80, 75]
}

df = pd.DataFrame(data)

plt.figure(figsize=(24, 14))
colors = ["#FF5733", "#33FF57", "#3357FF", "#FF33A8", "#A833FF", "#FF8C33",
          "#33FF8C", "#8C33FF", "#FF3333", "#33FFA8", "#FF33FF", "#33A8FF",
          "#8CFF33", "#A8FF33", "#FF5733", "#33FF57", "#5733FF", "#FF33A8",
          "#33FF33", "#5733FF", "#FF33A8", "#33FF57", "#8C33FF", "#FF33FF", "#33A8FF",
          "#A833FF", "#33FF8C", "#8CFF33", "#FF5733", "#33FF33"]

squarify.plot(sizes=df['Biodiversity Index'], label=df['Country'], color=colors, alpha=0.8)
plt.title('Biodiversity Distribution by Country and Continent', fontsize=24, y=1.05)
plt.axis('off')
plt.show()