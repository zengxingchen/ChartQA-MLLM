
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Define the data for the bubble chart in a DataFrame
data = {
    'Model': ['Civic', 'Accord', 'Camry', 'Corolla', 'Mustang', 'Charger',
              'Impreza', 'Forester', 'A4', 'Passat', 'Mazda3', 'CX-5', 
              'Veloster', 'Sonata'],
    'Horsepower': [100, 150, 170, 90, 300, 250, 152, 182, 188, 174, 186, 187, 201, 180],
    'Weight': [2500, 3200, 3300, 2400, 3400, 3600, 2900, 3200, 3450, 3285, 3075, 3525, 2800, 3250],
    'MPG': [33, 27, 30, 35, 15, 18, 26, 28, 24, 29, 27, 25, 30, 27],
    'Origin': ['#AA336A', '#AA336A', '#3355AA', '#3355AA', '#AA8F33', '#AA8F33',
               '#33AA72', '#33AA72', '#5555AA', '#5555AA', '#7733AA', '#7733AA',
               '#AA3377', '#AA3377']
}

df = pd.DataFrame(data)

# Set the size of the bubble chart
plt.figure(figsize=(10, 8))

# Create the bubble chart
bubble_chart = sns.scatterplot(data=df, x='Horsepower', y='MPG', 
                               size='Weight', hue='Origin', 
                               sizes=(400, 2500), edgecolor='w', alpha=0.7)

# Customize the axes and title
plt.xlabel('Horsepower')
plt.ylabel('Miles Per Gallon (MPG)')
plt.title('Car Performance: Horsepower vs. Fuel Efficiency')
plt.legend(title='Car Origin', bbox_to_anchor=(1.05, 1), loc=2)

# Show the plot
plt.show()