
import matplotlib.pyplot as plt
import pandas as pd

# Generate data points
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Consumption of Renewable Energy': [50, 55, 60, 70, 80, 90, 85, 95, 100, 110, 105, 115],
    'Consumption of Non-Renewable Energy': [120, 130, 125, 140, 150, 160, 165, 170, 175, 180, 185, 190],
    'Consumption of Nuclear Energy': [30, 32, 35, 40, 45, 50, 52, 55, 60, 65, 67, 70]
}

df = pd.DataFrame(data)

# Set the figure size
plt.figure(figsize=(16, 8))

# Plotting the stacked area chart
plt.stackplot(df['Month'],
              df['Consumption of Renewable Energy'], df['Consumption of Non-Renewable Energy'], df['Consumption of Nuclear Energy'],
              labels=['Renewable Energy', 'Non-Renewable Energy', 'Nuclear Energy'],
              colors=['#FF6347', '#4682B4', '#32CD32'])

# Add title and labels
plt.title('Monthly Energy Consumption by Type', pad=20)
plt.xlabel('Month')
plt.ylabel('Energy Consumption (in units)')

# Add legend
plt.legend(loc='upper left')

# Annotate specific data points
for i, (mon, renew, non_renew, nuclear) in enumerate(zip(df['Month'], df['Consumption of Renewable Energy'], df['Consumption of Non-Renewable Energy'], df['Consumption of Nuclear Energy'])):
    if mon == 'December':
        plt.text(i, renew+non_renew+nuclear, f'{renew+non_renew+nuclear}', ha='center', va='bottom')

# Show the plot
plt.show()