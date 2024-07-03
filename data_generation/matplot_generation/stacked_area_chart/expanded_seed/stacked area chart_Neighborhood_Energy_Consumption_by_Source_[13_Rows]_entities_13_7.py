
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Month': 'January', 'Solar': 230, 'Wind': 150, 'Hydro': 190, 'Natural Gas': 320, 'Coal': 210},
    {'Month': 'February', 'Solar': 210, 'Wind': 130, 'Hydro': 170, 'Natural Gas': 280, 'Coal': 180},
    {'Month': 'March', 'Solar': 240, 'Wind': 160, 'Hydro': 200, 'Natural Gas': 330, 'Coal': 220},
    {'Month': 'April', 'Solar': 260, 'Wind': 170, 'Hydro': 210, 'Natural Gas': 340, 'Coal': 230},
    {'Month': 'May', 'Solar': 280, 'Wind': 180, 'Hydro': 230, 'Natural Gas': 350, 'Coal': 250},
    {'Month': 'June', 'Solar': 290, 'Wind': 190, 'Hydro': 240, 'Natural Gas': 360, 'Coal': 260},
    {'Month': 'July', 'Solar': 310, 'Wind': 200, 'Hydro': 250, 'Natural Gas': 370, 'Coal': 270},
    {'Month': 'August', 'Solar': 300, 'Wind': 190, 'Hydro': 245, 'Natural Gas': 360, 'Coal': 265},
    {'Month': 'September', 'Solar': 270, 'Wind': 180, 'Hydro': 235, 'Natural Gas': 330, 'Coal': 240},
    {'Month': 'October', 'Solar': 260, 'Wind': 170, 'Hydro': 225, 'Natural Gas': 320, 'Coal': 230},
    {'Month': 'November', 'Solar': 250, 'Wind': 160, 'Hydro': 220, 'Natural Gas': 310, 'Coal': 220},
    {'Month': 'December', 'Solar': 240, 'Wind': 150, 'Hydro': 210, 'Natural Gas': 300, 'Coal': 210},
    {'Month': 'January (Next Year)', 'Solar': 230, 'Wind': 150, 'Hydro': 190, 'Natural Gas': 290, 'Coal': 200}
]

# Prepare the data for plotting
months = [entry['Month'] for entry in data]
solar = [entry['Solar'] for entry in data]
wind = [entry['Wind'] for entry in data]
hydro = [entry['Hydro'] for entry in data]
natural_gas = [entry['Natural Gas'] for entry in data]
coal = [entry['Coal'] for entry in data]

# Plot stacked area chart
plt.stackplot(months, solar, wind, hydro, natural_gas, coal,
              labels=['Solar', 'Wind', 'Hydro', 'Natural Gas', 'Coal'],
              colors=['#ffcc00', '#1e90ff', '#00cc99', '#d62728', '#9467bd'],
              alpha=0.8)

# Customize the plot
plt.xticks(rotation=45, ha="right")
plt.xlabel('Month')
plt.ylabel('Energy Production (GWh)')
plt.title('Monthly Energy Production by Source')
plt.legend(loc='upper left')
plt.tight_layout()  # Adjust the plot to ensure everything fits without overlap

# Show the plot
plt.show()