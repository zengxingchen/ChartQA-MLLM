
import matplotlib.pyplot as plt

# Data
cities = ['Tokyo', 'Delhi', 'Shanghai', 'São Paulo', 'Mexico City', 'Cairo', 'Dhaka', 'Mumbai', 'Beijing', 'Osaka', 'Karachi', 'Chongqing', 'Istanbul', 'Buenos Aires', 'Kolkata', 'Lagos', 'Kinshasa', 'Manila', 'Tianjin', 'Rio de Janeiro', 'Guangzhou', 'Lahore', 'Shenzhen', 'Bangalore', 'Moscow', 'Paris', 'Jakarta', 'London', 'Lima', 'Bangkok']
population = [37400068, 28514000, 25582000, 21650000, 21581000, 20076000, 19578000, 19430000, 19618000, 19281000, 14910000, 16382376, 15029231, 14967000, 14680000, 14368000, 14256000, 14010000, 13714500, 13635000, 13500000, 13290000, 12810000, 12764000, 12506468, 11020000, 10560000, 9304016, 10300000, 10310000]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(15, 10))  # Changed figure size

# Plotting the bar chart
ax.bar(cities, population, color=['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF7', '#A133FF', '#FFA133', '#33FFB5', '#A1FF33', '#5733FF', '#FF3385', '#33A1FF', '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF7', '#A133FF', '#FFA133', '#33FFB5', '#A1FF33', '#5733FF', '#FF3385', '#33A1FF', '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF7', '#A133FF'], width=0.6)  # Changed colors and bar width

# Customizing the plot (labels, title, etc.)
ax.set_ylabel('Population')
ax.set_title('Population of the Largest Cities in the World')
ax.set_ylim([0, 40000000])  # Adjusted to accommodate the maximum data point
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability

# Display the plot
plt.tight_layout()
plt.show()