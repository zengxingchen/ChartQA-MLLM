
import matplotlib.pyplot as plt

# Data
countries = ['Norway', 'Finland', 'South Korea', 'Japan', 'United States', 'Canada', 'Brazil', 'India', 'China', 'South Africa', 
             'Germany', 'France', 'United Kingdom', 'Australia', 'Mexico', 'Russia', 'Nigeria', 'Indonesia', 'Argentina', 'Turkey']
education_spending = [6.6, 7.2, 4.9, 3.2, 5.0, 5.7, 5.6, 3.8, 4.0, 6.2, 
                      4.8, 5.4, 5.2, 5.3, 5.3, 3.7, 5.6, 3.6, 5.0, 4.5]
literacy_rate = [99, 99, 98, 99, 99, 99, 93, 74, 97, 87, 
                 99, 99, 99, 99, 94, 99, 62, 95, 99, 97]
population = [5.4, 5.5, 51.2, 126.5, 331.0, 38.0, 212.5, 1380.0, 1395.0, 59.3, 
              83.2, 65.2, 67.8, 25.6, 127.6, 144.5, 206.0, 273.5, 45.1, 84.2]

# Normalize the population data to use as bubble sizes
max_population = max(population)
bubble_sizes = [(p / max_population) * 1000 for p in population]

# Plot
plt.figure(figsize=(18, 10))  # Adjusted width and height of the chart
plt.scatter(education_spending, literacy_rate, s=bubble_sizes,
            color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', 
                   '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'],
            alpha=0.7)

# Additional Customization
plt.title('Education Spending vs. Literacy Rate by Country', fontsize=15)
plt.xlabel('Education Spending (% of GDP)', fontsize=12)
plt.ylabel('Literacy Rate (%)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True)

# Annotating the country names
for i, country in enumerate(countries):
    plt.text(education_spending[i], literacy_rate[i], country, ha='center', va='center', fontsize=9)

# Show the plot
plt.tight_layout()
plt.show()