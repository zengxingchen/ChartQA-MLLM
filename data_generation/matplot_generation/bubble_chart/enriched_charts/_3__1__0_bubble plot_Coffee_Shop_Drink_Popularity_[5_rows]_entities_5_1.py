
import matplotlib.pyplot as plt

data = {
    'Country': ['USA', 'China', 'Japan', 'Germany', 'India', 'Brazil', 'Russia', 'Mexico', 'France', 'UK', 'Italy', 'Canada', 'South Korea', 'Australia', 'Spain', 'Turkey', 'Argentina', 'Indonesia', 'Netherlands', 'Saudi Arabia', 'Switzerland'],
    'Food Consumption (kg/year)': [120, 65, 55, 85, 50, 90, 75, 100, 70, 80, 60, 95, 55, 85, 65, 75, 85, 50, 70, 85, 60],
    'Obesity Rate (%)': [36.2, 6.2, 4.3, 22.3, 3.9, 22.1, 23.1, 28.9, 21.6, 27.8, 19.9, 29.4, 5.8, 31.3, 23.8, 21.1, 28.3, 6.9, 20.4, 35.4, 19.5],
    'Physical Activity Rate (%)': [45, 50, 70, 60, 40, 55, 50, 40, 65, 55, 65, 50, 75, 60, 60, 45, 50, 35, 65, 40, 70]
}

fig, ax = plt.subplots(figsize=(18, 12))

for i in range(len(data['Country'])):
    ax.scatter(data['Obesity Rate (%)'][i], data['Physical Activity Rate (%)'][i], 
               s=data['Food Consumption (kg/year)'][i] * 5,  # Bubble sizes
               label='{}'.format(data['Country'][i]),
               alpha=0.6, edgecolors='w',
               linewidth=2)

colors = ['#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF3357',
          '#FF33FF', '#33FFFF', '#FFFF33', '#B535FF', '#FF5733',
          '#4B8B3B', '#F67E7D', '#843B62', '#16A085', '#2980B9',
          '#F1C40F', '#D35400', '#7D3C98', '#C39BD3', '#7FB3D5',
          '#2E4053']

for i, dot in enumerate(ax.collections):
    dot.set_facecolor(colors[i % len(colors)])

ax.set_title("Global Food Consumption, Obesity Rates, and Physical Activity Levels", pad=20)
ax.set_xlabel('Obesity Rate (%)')
ax.set_ylabel('Physical Activity Rate (%)')

ax.grid(True)
ax.legend(title='Countries', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()