
import matplotlib.pyplot as plt

# Data
data = {
    'Country': ['USA', 'China', 'Japan', 'Germany', 'India', 'Brazil', 'Russia', 'Mexico', 'France', 'UK', 'Italy', 'Canada', 'South Korea', 'Australia', 'Iran', 'Turkey', 'Indonesia', 'Netherlands', 'Saudi Arabia', 'Switzerland'],
    'Education Spending (% of GDP)': [5.0, 4.1, 3.5, 4.8, 3.1, 6.0, 4.7, 5.2, 5.5, 5.7, 4.0, 5.8, 5.1, 5.0, 3.7, 4.3, 3.6, 5.6, 5.1, 5.3],
    'Internet Usage (% of Population)': [89, 60, 92, 87, 42, 70, 80, 65, 85, 94, 73, 95, 96, 88, 53, 76, 40, 94, 93, 94],
    'Literacy Rate (%)': [99, 96, 99, 99, 74, 92, 99, 94, 99, 99, 99, 99, 99, 99, 85, 96, 92, 99, 95, 99]
}

# Create figure and axis
fig, ax = plt.subplots(figsize=(16, 10))

# Scatter plot for each country
for i in range(len(data['Country'])):
    ax.scatter(data['Internet Usage (% of Population)'][i], data['Literacy Rate (%)'][i], 
               s=data['Education Spending (% of GDP)'][i] * 100,  # Bubble sizes
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
ax.set_title("Countries' Spending on Education, Internet Usage, and Literacy Rates", pad=20)
ax.set_xlabel('Internet Usage (% of Population)')
ax.set_ylabel('Literacy Rate (%)')

# Grid and legend
ax.grid(True)
ax.legend(title='Countries', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()