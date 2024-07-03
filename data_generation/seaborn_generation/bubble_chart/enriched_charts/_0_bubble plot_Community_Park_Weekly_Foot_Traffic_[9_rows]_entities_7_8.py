
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {
    'Country': ['USA', 'USA', 'China', 'China', 'India', 'India', 'Germany', 'Germany', 'Brazil', 'Brazil', 'France', 'France'],
    'VehicleType': ['Cars', 'Trucks', 'Cars', 'Trucks', 'Cars', 'Trucks', 'Cars', 'Trucks', 'Cars', 'Trucks', 'Cars', 'Trucks'],
    'NumberOfVehicles': [250000, 120000, 300000, 150000, 180000, 80000, 95000, 40000, 85000, 30000, 70000, 20000],
    'CO2Emissions': [370, 540, 450, 625, 280, 410, 330, 380, 300, 360, 310, 350]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create the bubble chart
plt.figure(figsize=(14, 10))
bubble_plot = sns.scatterplot(data=df, x='Country', y='CO2Emissions', size='NumberOfVehicles', hue='VehicleType',
                              sizes=(100, 2000), alpha=0.7, palette=["#FF5733", "#33C1FF"])

# Customize legend and axis labels
bubble_plot.legend(title='Vehicle Type', loc='upper left')
plt.xlabel('Country')
plt.ylabel('CO2 Emissions (g/km)')
plt.title('CO2 Emissions by Vehicle Type in Different Countries')

# Show the plot
plt.show()