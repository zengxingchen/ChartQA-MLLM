
import matplotlib.pyplot as plt

# Data provided
chart_data = [
    {'City': 'New York', 'Public Transit': '56%', 'Bicycle': '10%', 'Walk': '10%', 'Car': '20%', 'Others': '4%'},
    {'City': 'Los Angeles', 'Public Transit': '28%', 'Bicycle': '2%', 'Walk': '3%', 'Car': '65%', 'Others': '2%'},
    {'City': 'San Francisco', 'Public Transit': '33%', 'Bicycle': '15%', 'Walk': '10%', 'Car': '35%', 'Others': '7%'},
    {'City': 'Chicago', 'Public Transit': '50%', 'Bicycle': '7%', 'Walk': '6%', 'Car': '34%', 'Others': '3%'},
    {'City': 'Miami', 'Public Transit': '20%', 'Bicycle': '1%', 'Walk': '5%', 'Car': '70%', 'Others': '4%'},
    {'City': 'Seattle', 'Public Transit': '21%', 'Bicycle': '8%', 'Walk': '12%', 'Car': '54%', 'Others': '5%'},
    {'City': 'Boston', 'Public Transit': '35%', 'Bicycle': '7%', 'Walk': '15%', 'Car': '38%', 'Others': '5%'},
    {'City': 'Austin', 'Public Transit': '15%', 'Bicycle': '3%', 'Walk': '2%', 'Car': '75%', 'Others': '5%'},
    {'City': 'Denver', 'Public Transit': '23%', 'Bicycle': '6%', 'Walk': '5%', 'Car': '60%', 'Others': '6%'},
    {'City': 'Washington D.C.', 'Public Transit': '38%', 'Bicycle': '5%', 'Walk': '12%', 'Car': '40%', 'Others': '5%'},
    {'City': 'Atlanta', 'Public Transit': '15%', 'Bicycle': '1%', 'Walk': '2%', 'Car': '79%', 'Others': '3%'},
    {'City': 'Portland', 'Public Transit': '25%', 'Bicycle': '12%', 'Walk': '15%', 'Car': '43%', 'Others': '5%'}
]

# Extracting cities and converting percentages to numeric values
cities = [data['City'] for data in chart_data]
transit_modes = ['Public Transit', 'Bicycle', 'Walk', 'Car', 'Others']
percentages = {mode: [int(data[mode].strip('%')) for data in chart_data] for mode in transit_modes}

# Creating the stacked bar chart
fig, ax = plt.subplots(figsize=(10, 8))

bar_width = 0.35
r = range(len(cities))
colors = ['skyblue', 'limegreen', 'gold', 'tomato', 'purple']  # Example of diversified color palette

bottoms = [0] * len(cities)
for i, mode in enumerate(transit_modes):
    ax.bar(cities, percentages[mode], width=bar_width, label=mode, color=colors[i], bottom=bottoms)
    # Update the bottoms for the next stack
    bottoms = [bottoms[j] + percentages[mode][j] for j in range(len(cities))]

# Customizing the plot
ax.set_xlabel('City')
ax.set_ylabel('Percentage')
ax.set_title('Mode of Transport Distribution by City')
ax.legend(title="Modes of Transport", bbox_to_anchor=(1.05, 1), loc='upper left')

# Annotate the percentages on the bars
for i, city in enumerate(cities):
    for j, mode in enumerate(transit_modes):
        height = sum([percentages[tm][i] for tm in transit_modes[:j]])
        percentage_val = percentages[mode][i]
        if percentage_val > 0:  # Only annotate non-zero values
            ax.text(i, height + percentage_val/2, f"{percentage_val}%", ha='center', va='center')

ax.set_xticks(r)
ax.set_xticklabels(cities, rotation=45, ha='right')

# Display the plot
plt.tight_layout()
plt.show()