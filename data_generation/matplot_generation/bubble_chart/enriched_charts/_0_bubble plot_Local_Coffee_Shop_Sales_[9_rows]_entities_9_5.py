
import matplotlib.pyplot as plt

# Data for the chart - can be written directly as CSV as provided above
data = {
    'Country': ['China', 'India', 'United States', 'Indonesia', 'Brazil', 'Pakistan', 'Nigeria', 'Bangladesh', 'Russia', 
                'Mexico', 'Japan', 'Ethiopia', 'Philippines', 'Egypt', 'Vietnam', 'DR Congo', 'Turkey', 'Iran', 'Germany',
                'Thailand', 'France', 'United Kingdom', 'Italy', 'South Africa', 'Myanmar', 'South Korea', 'Colombia', 
                'Spain', 'Ukraine', 'Tanzania'],
    'Population (millions)': [1398, 1326, 329, 267, 211, 206, 200, 163, 146, 127, 126, 115, 108, 100, 96, 89, 82, 82, 
                               83, 69, 67, 66, 60, 58, 54, 51, 50, 47, 44, 56],
    'GDP (billions)': [14342, 2875, 21433, 1059, 1839, 284, 448, 317, 1680, 1198, 5050, 95, 376, 303, 261, 47, 754, 458, 
                       3846, 543, 2715, 2827, 2003, 351, 76, 1646, 324, 1393, 153, 62],
    'GDP per Capita': [10254, 2169, 65118, 3969, 8712, 1380, 2235, 1942, 11510, 9437, 40039, 826, 3481, 3030, 2721, 528, 
                       9195, 5585, 46349, 7870, 40537, 42834, 33383, 6052, 1407, 32294, 6474, 29638, 3477, 1107]
}

# Create the figure and the axes
fig, ax = plt.subplots(figsize=(16, 9))  # Reasonable change in width and height

# Scatter plot sizes
sizes = [p/10 for p in data['Population (millions)']]

# Scatter plot
scatter = ax.scatter(x=data['GDP per Capita'], y=data['GDP (billions)'], s=sizes, 
                     c=[(p/20000, g/27000, 0.5) for p, g in zip(data['Population (millions)'], data['GDP (billions)'])],
                     alpha=0.6, edgecolors='w', linewidth=2)

# Title and labels
ax.set_title('GDP vs Population and GDP per Capita of countries', fontsize=18)
ax.set_xlabel('GDP per Capita', fontsize=14)
ax.set_ylabel('GDP in Billions', fontsize=14)

# Add country names as annotation to each data point
for i, txt in enumerate(data['Country']):
    ax.annotate(txt, (data['GDP per Capita'][i], data['GDP (billions)'][i]), fontsize=8, ha='center')

# Show plot
plt.show()