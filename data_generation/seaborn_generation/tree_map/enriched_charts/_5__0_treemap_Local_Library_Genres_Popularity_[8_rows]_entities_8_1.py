
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
    'GDP': [14342903, 2875142, 5081770, 1655608, 1053126, 3845630, 2826441, 2715518, 2073860, 1483494,
            448120, 368135, 302256, 169988, 119040, 21433226, 2055502, 1736424, 1220357, 449663,
            1392687, 204913, 24975, 5470, 884]
}

df = pd.DataFrame(data)

# Plotting the treemap
plt.figure(figsize=(24, 14))
colors = ["#FF6F61", "#6B5B95", "#88B04B", "#F7CAC9", "#92A8D1", "#955251",
          "#B565A7", "#009B77", "#DD4124", "#D65076", "#45B8AC", "#EFC050",
          "#5B5EA6", "#9B2335", "#DFCFBE", "#55B4B0", "#E15D44", "#7FCDCD",
          "#BC243C", "#C3447A", "#98B4D4", "#FFBF00", "#6A5ACD", "#D4A017", "#9370DB"]

# Using squarify to plot treemap
squarify.plot(sizes=df['GDP'], label=df['Country'], color=colors, alpha=0.8)
plt.title('GDP Distribution by Country', fontsize=24, y=1.05)
plt.axis('off')
plt.show()