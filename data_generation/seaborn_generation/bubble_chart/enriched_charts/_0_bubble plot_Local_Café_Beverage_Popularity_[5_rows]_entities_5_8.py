
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Since we will be plotting the data, create a DataFrame directly from the CSV data provided.
data = pd.DataFrame({
    'Brand': ['Toyota', 'Ford', 'Chevrolet', 'BMW', 'Mercedes', 'Audi', 'Tesla', 'Honda', 'Hyundai', 'Mazda', 'Porsche', 'Lexus', 'Land Rover', 'Ferrari', 'Lamborghini'],
    'Horsepower': [150, 200, 250, 300, 350, 320, 450, 180, 160, 170, 400, 290, 280, 600, 620],
    'Weight': [3500, 4000, 4200, 3800, 3700, 3900, 4400, 3400, 3300, 3200, 3600, 4000, 4800, 3000, 3100],
    'Price': [25000, 30000, 35000, 55000, 67000, 60000, 80000, 27000, 22000, 23000, 100000, 47000, 90000, 250000, 300000],
    'BrandValue': [80, 85, 75, 95, 90, 88, 89, 83, 76, 78, 98, 87, 92, 100, 99]
})

# Create the bubble chart using seaborns scatterplot method.
plt.figure(figsize=(14, 10))
bubble_chart = sns.scatterplot(
    data=data,
    x='Horsepower',
    y='Price',
    size='Weight',
    hue='BrandValue',
    palette=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0','#ffb3e6', '#c4e17f', '#76eec6', '#ffbbff', '#808000', '#FF6347', '#6e8b3d', '#c6e2ff', '#2e8b57', '#ffdab9'],
    sizes=(20, 2000),
    alpha=0.5
)

# Customize the legend
plt.legend(title='Brand Value Rating')

# Adding title and labels
plt.title('Comparison of Car Attributes', fontsize=20)
plt.xlabel('Horsepower', fontsize=14)
plt.ylabel('Price in USD', fontsize=14)

# Show the plot
plt.show()