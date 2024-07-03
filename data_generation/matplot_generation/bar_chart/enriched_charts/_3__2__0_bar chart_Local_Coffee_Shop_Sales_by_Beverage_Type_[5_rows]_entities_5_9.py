
import matplotlib.pyplot as plt

# Data
cities = [
    'New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego',
    'Dallas', 'San Jose', 'Austin', 'Jacksonville', 'San Francisco', 'Columbus', 'Fort Worth', 'Indianapolis',
    'Charlotte', 'Seattle', 'Denver', 'Washington', 'Boston', 'El Paso', 'Detroit', 'Nashville', 'Memphis',
    'Portland', 'Oklahoma City', 'Las Vegas', 'Louisville', 'Baltimore', 'Milwaukee', 'Albuquerque', 'Tucson',
    'Fresno', 'Sacramento', 'Kansas City', 'Long Beach', 'Mesa', 'Virginia Beach', 'Atlanta', 'Colorado Springs',
    'Raleigh', 'Omaha', 'Miami', 'Oakland', 'Minneapolis', 'Tulsa', 'Wichita', 'Arlington', 'Bakersfield',
    'New Orleans', 'Honolulu'
]
temperatures = [
    8.7, 18.7, 10.4, 20.6, 22.4, 12.8, 21.0, 18.0, 18.7, 15.5, 20.1, 21.5, 15.0, 12.4, 18.9, 12.0, 16.4,
    11.7, 11.5, 14.2, 11.1, 18.3, 10.1, 16.2, 17.4, 12.3, 16.3, 20.3, 14.6, 14.5, 9.3, 14.6, 20.7, 18.9,
    16.1, 13.4, 18.2, 21.8, 15.5, 17.0, 10.2, 16.5, 11.3, 24.6, 15.7, 8.3, 16.0, 13.3, 18.4, 19.2, 20.3,
    25.6
]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(15, 10))  # Adjusted figure size

# Plotting the horizontal bar chart
ax.barh(cities, temperatures, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']*5, height=0.7)  # Changed colors and bar height

# Customizing the plot (labels, title, etc.)
ax.set_xlabel('Temperature (°C)')
ax.set_title('Average Monthly Temperature in Major Cities', pad=20)
ax.set_xlim([0, 30])  # Adjusted to accommodate the maximum data point

# Display the plot
plt.tight_layout()
plt.show()