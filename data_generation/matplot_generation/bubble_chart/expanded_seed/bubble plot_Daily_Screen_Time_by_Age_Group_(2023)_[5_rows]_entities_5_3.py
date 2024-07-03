
import matplotlib.pyplot as plt

# Given data
data = [
    {'Age Group': '0-18', 'Average Screen Time (hours/day)': 7.5, 'Population (millions)': 73, 'Country': 'USA'},
    {'Age Group': '19-30', 'Average Screen Time (hours/day)': 8.8, 'Population (millions)': 42, 'Country': 'USA'},
    {'Age Group': '31-45', 'Average Screen Time (hours/day)': 6.9, 'Population (millions)': 38, 'Country': 'USA'},
    {'Age Group': '46-60', 'Average Screen Time (hours/day)': 5.7, 'Population (millions)': 37, 'Country': 'USA'},
    {'Age Group': '60+ ', 'Average Screen Time (hours/day)': 4.6, 'Population (millions)': 20, 'Country': 'USA'}
]

# Extracting age groups and corresponding screen times, populations and country codes for color coding
age_groups = [entry['Age Group'] for entry in data]
screen_times = [entry['Average Screen Time (hours/day)'] for entry in data]
populations = [entry['Population (millions)'] for entry in data]
countries = [entry['Country'] for entry in data]

# Colors: Here we just assign 'blue' to all entries since we only have one country - USA
colors = ['blue' for country in countries]

# Bubble size: A list comprehension that multiplies each population value by a factor to scale the bubble sizes
sizes = [population * 10 for population in populations]  # You can adjust the factor for better visualization

# Create a bubble chart
plt.figure(figsize=(10, 6))
bubble = plt.scatter(age_groups, screen_times, s=sizes, c=colors, alpha=0.5)

# Adding titles and labels
plt.title('Average Screen Time by Age Group in the USA')
plt.xlabel('Age Group')
plt.ylabel('Average Screen Time (hours/day)')

# Add a grid for better readability
plt.grid(True)

# Show the bubble sizes with a legend
for population in set(populations):
    plt.scatter([], [], c='k', alpha=0.5, s=population * 10,
                label=str(population) + ' million')

plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Population (millions)')

# Show the bubble chart
plt.show()