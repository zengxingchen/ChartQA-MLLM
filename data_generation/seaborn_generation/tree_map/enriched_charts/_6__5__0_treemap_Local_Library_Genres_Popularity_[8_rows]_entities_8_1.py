
import pandas as pd
import seaborn as sns
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
    'GDP': [14342903, 2875142, 5081770, 1655608, 1053126, 3845630, 2826441, 2715518, 2073860, 1483494,
            448120, 368135, 302256, 169988, 119040, 21433226, 2055502, 1736424, 1220357, 449663,
            1392687, 204913, 24975, 5470, 884, 793000, 1357301, 98632, 294186, 396]
}

df = pd.DataFrame(data)

plt.figure(figsize=(28, 16))
colors = ["#FF5733", "#33FF57", "#3357FF", "#FF33A8", "#A833FF", "#FF8C33",
          "#33FF8C", "#8C33FF", "#FF3333", "#33FFA8", "#FF33FF", "#33A8FF",
          "#8CFF33", "#A8FF33", "#FF5733", "#33FF57", "#5733FF", "#FF33A8",
          "#33FF33", "#5733FF", "#FF33A8", "#33FF57", "#8C33FF", "#FF33FF", "#33A8FF",
          "#A833FF", "#33FF8C", "#8CFF33", "#FF5733", "#33FF33"]

squarify.plot(sizes=df['GDP'], label=df['Country'], color=colors, alpha=0.8)
plt.title('GDP Distribution by Country and Continent', fontsize=24, y=1.05)
plt.axis('off')
plt.show()