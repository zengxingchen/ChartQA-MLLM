
import matplotlib.pyplot as plt

# Define the data
data = [
    {'Year': 2010, 'Average Screen Size (inches)': 3.5},
    {'Year': 2011, 'Average Screen Size (inches)': 3.7},
    {'Year': 2012, 'Average Screen Size (inches)': 4.1},
    {'Year': 2013, 'Average Screen Size (inches)': 4.3},
    {'Year': 2014, 'Average Screen Size (inches)': 4.5},
    {'Year': 2015, 'Average Screen Size (inches)': 4.7},
    {'Year': 2016, 'Average Screen Size (inches)': 5.0},
    {'Year': 2017, 'Average Screen Size (inches)': 5.2},
    {'Year': 2018, 'Average Screen Size (inches)': 5.5},
    {'Year': 2019, 'Average Screen Size (inches)': 5.8},
    {'Year': 2020, 'Average Screen Size (inches)': 6.1},
    {'Year': 2021, 'Average Screen Size (inches)': 6.4}
]

# Extract years and average screen sizes
years = [item['Year'] for item in data]
avg_screen_sizes = [item['Average Screen Size (inches)'] for item in data]

# Define marker sizes based on screen size (for illustration purposes)
marker_sizes = [size ** 2 * 10 for size in avg_screen_sizes]

# Generate scatter plot
plt.scatter(years, avg_screen_sizes, s=marker_sizes, alpha=0.6, c=range(len(years)), cmap='viridis')

# Title and labels
plt.title('Average Screen Size Over Years')
plt.xlabel('Year')
plt.ylabel('Average Screen Size (inches)')

# Add year annotations to each point
for i, txt in enumerate(years):
    plt.annotate(txt, (years[i], avg_screen_sizes[i]), xytext=(5, 5), textcoords='offset points')

# Add a colorbar for the color scale
plt.colorbar(label='Year Index')

# Show the plot
plt.show()