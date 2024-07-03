
import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Renewable Energy': [300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 520],
    'Electric Vehicles': [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260],
    'Smart Homes': [75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130],
}

# Create a dataframe
df = pd.DataFrame(data)

# Define x-axis based on 'Month'
x = df['Month']

# Plot using specific color codes
plt.figure(figsize=(16, 10))
plt.stackplot(x, df['Renewable Energy'], df['Electric Vehicles'], df['Smart Homes'], 
              colors=['#1f77b4', '#ff7f0e', '#2ca02c'])

# Adding title and labels
plt.title('Monthly Investment in Green Technologies', pad=20)
plt.xlabel('Month')
plt.ylabel('Investment (in millions USD)')

# Add annotations for 'Smart Homes' for the month of January and December
plt.annotate('Smart Homes in January', xy=(0, df['Renewable Energy'][0] + df['Electric Vehicles'][0]), 
             xytext=(0, 600), arrowprops=dict(facecolor='black', arrowstyle='->'))
             
plt.annotate('Smart Homes in December', xy=(11, df['Renewable Energy'][11] + df['Electric Vehicles'][11] + df['Smart Homes'][11]), 
             xytext=(11, 950), arrowprops=dict(facecolor='black', arrowstyle='->'))

# Display legend
plt.legend(['Renewable Energy', 'Electric Vehicles', 'Smart Homes'], loc='upper left')

# Display the figure
plt.show()