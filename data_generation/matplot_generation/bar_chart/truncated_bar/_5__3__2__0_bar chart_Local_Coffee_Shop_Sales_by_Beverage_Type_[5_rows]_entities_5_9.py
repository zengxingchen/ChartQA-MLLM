
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
incomes = [
    4500, 4200, 4000, 4800, 3900, 4100, 4700, 4300, 4400, 5000, 4600, 3800, 5100, 4100, 4300, 3950, 4200,
    4950, 4850, 5050, 4700, 3800, 4000, 4350, 3900, 4600, 3900, 4100, 3950, 4200, 4000, 3850, 3900, 4050,
    4400, 4100, 4250, 3950, 4050, 4600, 4400, 4500, 4000, 4500, 4700, 4450, 3850, 3900, 4200, 3950, 4300,
    4900
]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(10, 15))

# Plotting the vertical bar chart
ax.bar(cities, incomes, color=['#4B0082', '#800080', '#FF6347', '#4682B4', '#5F9EA0', '#DAA520', '#D2691E', '#FF4500', '#8B4513', '#B22222']*5, width=0.7)

# Customizing the plot (labels, title, etc.)
ax.set_ylabel('Average Monthly Income (USD)')
ax.set_title('Average Monthly Income in Major Cities', pad=20)
ax.set_ylim([3500, 5200])

# Rotate x-axis labels for better readability
plt.xticks(rotation=90)

# Display the plot
plt.tight_layout()
plt.show()