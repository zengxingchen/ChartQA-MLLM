
import matplotlib.pyplot as plt

# Table data provided above
data = {
    'Country': ['USA', 'China', 'Japan', 'Germany', 'India', 'Brazil', 'Russia', 'Mexico', 'France', 'UK', 'Italy', 'Canada', 'South Korea', 'Australia', 'Iran', 'Turkey', 'Indonesia', 'Netherlands', 'Saudi Arabia', 'Switzerland'],
    'Population (millions)': [331, 1439, 126, 83, 1380, 213, 144, 129, 65, 68, 60, 38, 51, 25, 84, 84, 273, 17, 35, 8.6],
    'Life Expectancy (years)': [78.5, 76.9, 84.6, 81.2, 69.7, 75.9, 72.7, 75.1, 82.5, 81.2, 83.6, 82.3, 83.3, 83.2, 76.7, 77.7, 71.5, 82.1, 75.0, 83.8],
    'GDP (billions)': [21000, 14722, 5060, 3846, 2875, 1434, 1579, 1158, 2715, 2827, 1908, 1646, 1642, 1393, 609, 720, 1058, 913, 793, 703]
}

# Create figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Scatter plot for each country
for i in range(len(data['Country'])):
    ax.scatter(data['Population (millions)'][i], data['Life Expectancy (years)'][i], 
               s=data['GDP (billions)'][i]/10,  # Bubble sizes
               label='{}'.format(data['Country'][i]),
               alpha=0.6, edgecolors='w',
               linewidth=2)

# Custom colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF3357',
          '#FF33FF', '#33FFFF', '#FFFF33', '#B535FF', '#FF5733',
          '#4B8B3B', '#F67E7D', '#843B62', '#16A085', '#2980B9',
          '#F1C40F', '#D35400', '#7D3C98', '#C39BD3', '#7FB3D5']

# Apply the colors to the scatter plot
for i, dot in enumerate(ax.collections):
    dot.set_facecolor(colors[i % len(colors)])

# Title and labels
ax.set_title('Bubble Chart: Country Population, Life Expectancy, and GDP')
ax.set_xlabel('Population (millions)')
ax.set_ylabel('Life Expectancy (years)')

# Grid and legend
ax.grid(True)
ax.legend(title='Countries')

plt.tight_layout()
plt.show()