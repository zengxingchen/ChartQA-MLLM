
import matplotlib.pyplot as plt

# Data
countries = ['United States', 'China', 'Japan', 'Germany', 'India', 'United Kingdom', 'France', 'Italy', 'Brazil', 'Canada', 'Russia', 'South Korea', 'Australia', 'Spain', 'Mexico', 'Indonesia', 'Netherlands', 'Saudi Arabia', 'Turkey', 'Switzerland']
gdp = [21.43, 14.34, 5.08, 3.86, 2.87, 2.83, 2.71, 2.00, 1.84, 1.74, 1.64, 1.63, 1.39, 1.39, 1.27, 1.12, 0.91, 0.79, 0.76, 0.72]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(10, 15))  # Changed figure size

# Plotting the horizontal bar chart
ax.barh(countries, gdp, color=['#1F77B4', '#FF7F0E', '#2CA02C', '#D62728', '#9467BD', '#8C564B', '#E377C2', '#7F7F7F', '#BCBD22', '#17BECF', '#1F77B4', '#FF7F0E', '#2CA02C', '#D62728', '#9467BD', '#8C564B', '#E377C2', '#7F7F7F', '#BCBD22', '#17BECF'], height=0.6)  # Changed colors and bar height

# Customizing the plot (labels, title, etc.)
ax.set_xlabel('GDP (in trillion USD)')
ax.set_title('GDP of the Largest Economies in the World')
ax.set_xlim([0.7, 22])  # Adjusted to start y-axis from a specific value

# Display the plot
plt.tight_layout()
plt.show()