
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the DataFrame directly
data = pd.DataFrame({
    'Day': range(1, 32),
    'PageViews': [1200, 1300, 1250, 1400, 1350, 1450, 1500, 1600, 1550, 1650, 
                  1700, 1750, 1800, 1850, 1900, 1950, 2000, 2100, 2200, 2150,
                  2250, 2300, 2350, 2400, 2450, 2500, 2550, 2600, 2650, 2700, 2750]
})

plt.figure(figsize=(14, 7))
sns.set_theme(style="whitegrid")

# Creating an area chart
ax = sns.lineplot(data=data, x='Day', y='PageViews', color='#1f77b4')
ax.fill_between(data.Day, data.PageViews, color="#87CEEB", alpha=0.5)

# Annotating the highest page views
highest_views = data.PageViews.max()
highest_day = data.Day[data.PageViews.idxmax()]
plt.annotate(f'Highest\n{highest_views} views', xy=(highest_day, highest_views), xytext=(highest_day+2, highest_views+200),
             arrowprops=dict(facecolor='#FF5733', shrink=0.05))

# Adding chart title and labels
plt.title('Daily Page Views in January')
plt.xlabel('Day')
plt.ylabel('Page Views')

# Display the chart
plt.show()