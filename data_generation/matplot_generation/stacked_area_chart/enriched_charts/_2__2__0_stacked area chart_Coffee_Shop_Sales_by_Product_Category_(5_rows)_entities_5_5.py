
import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Fruits': [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105],
    'Vegetables': [70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125],
    'Dairy': [40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
}

# Create a dataframe
df = pd.DataFrame(data)

# Define x-axis based on 'Month'
x = df['Month']

# Plot using specific color codes
plt.figure(figsize=(16, 10))
plt.stackplot(x, df['Fruits'], df['Vegetables'], df['Dairy'], 
              colors=['#1f77b4', '#ff7f0e', '#2ca02c'])

# Adding title and labels
plt.title('Monthly Food Consumption Over A Year')
plt.xlabel('Month')
plt.ylabel('Consumption (kg)')

# Add annotations for 'Fruits' for the month of January and December
plt.annotate('Fruits in January', xy=(0, df['Fruits'][0]), 
             xytext=(0, 200), arrowprops=dict(facecolor='black', arrowstyle='->'))

plt.annotate('Fruits in December', xy=(11, df['Fruits'][11] + df['Vegetables'][11] + df['Dairy'][11]), 
             xytext=(11, 400), arrowprops=dict(facecolor='black', arrowstyle='->'))

# Display the figure
plt.show()