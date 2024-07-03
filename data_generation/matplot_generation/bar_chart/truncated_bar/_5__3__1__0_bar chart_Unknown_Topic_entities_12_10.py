
import matplotlib.pyplot as plt

# Table data represented as lists
countries = ['USA', 'China', 'India', 'Germany', 'Brazil', 'UK', 'France', 'Japan', 'Australia', 'Canada', 'South Korea', 'Italy']
years = ['2020', '2021', '2022', '2023']
values = [
    [600, 620, 640, 660],
    [550, 570, 590, 610],
    [400, 420, 440, 460],
    [350, 360, 370, 380],
    [300, 310, 320, 330],
    [280, 290, 300, 310],
    [260, 270, 280, 290],
    [240, 250, 260, 270],
    [220, 230, 240, 250],
    [200, 210, 220, 230],
    [180, 190, 200, 210],
    [160, 170, 180, 190]
]

colors = ['#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF33A6', 
          '#33FFF6', '#F633FF', '#F6FF33', '#33A6FF', '#A6FF33',
          '#FF8C33', '#A6FF33']

# Setting the size of the plot
plt.figure(figsize=(10, 12))

# Creating a vertical bar chart
for i, year in enumerate(years):
    plt.bar(countries, [values[j][i] for j in range(len(countries))], color=colors, edgecolor='grey', width=0.2, bottom=[sum(values[j][:i]) for j in range(len(countries))], label=year)

# Customizing the plot
plt.ylabel('Values (in thousands)')
plt.title('Annual Value by Country', pad=20)
plt.ylim(100, max([sum(v) for v in values]) + 100)  # Adjusting y-axis limits for better clarity
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Adding a grid for the y-axis
plt.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left')

# Display the plot
plt.show()