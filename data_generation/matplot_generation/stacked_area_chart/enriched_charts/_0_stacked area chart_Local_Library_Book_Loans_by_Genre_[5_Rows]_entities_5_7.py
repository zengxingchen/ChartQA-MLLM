
import matplotlib.pyplot as plt

# Define the data
years = list(range(2011, 2022))
electric_cars = [1000, 3000, 5000, 8000, 13000, 21000, 34000, 55000, 89000, 144000, 233000]
hybrid_cars = [15000, 17000, 20000, 23000, 25000, 30000, 35000, 40000, 45000, 50000, 55000]
fossil_fuel_cars = [500000, 495000, 485000, 470000, 450000, 420000, 380000, 330000, 250000, 150000, 70000]

# Start plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Plot stacked area chart
ax.stackplot(years, electric_cars, hybrid_cars, fossil_fuel_cars, colors=['#76FF03', '#FFD600', '#FF6D00'])

# Annotate specific points
ax.annotate('Rapid growth in Electric Cars', xy=(2020, 144000), xytext=(2015, 300000),
            arrowprops=dict(facecolor='#76FF03', shrink=0.05))

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Number of Cars')
plt.title('Car Sales by Type (2011-2021)')

# Show the plot
plt.show()