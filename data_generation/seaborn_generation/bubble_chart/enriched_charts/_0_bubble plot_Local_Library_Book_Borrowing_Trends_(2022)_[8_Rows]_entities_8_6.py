
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating the DataFrame from the data above
data = {
    'Model': ['Toyota Prius', 'Honda Civic', 'Ford F150', 'Chevrolet Impala', 'Tesla Model 3',
              'BMW 3 Series', 'Audi A4', 'Subaru Outback', 'Hyundai Elantra', 'Toyota Camry',
              'Honda Accord', 'Ford Mustang', 'Kia Soul', 'Chevrolet Bolt', 'Nissan Leaf',
              'Mercedes-Benz C-Class', 'Porsche 911', 'Jeep Wrangler'],
    'MPG': [50, 32, 22, 27, 130, 30, 27, 28, 33, 29, 30, 21, 27, 119, 111, 24, 20, 18],
    'Horsepower': [121, 158, 325, 197, 283, 255, 248, 182, 147, 203, 192, 310, 147, 200, 147, 255, 379, 285],
    'CO2_Emissions': [170, 225, 411, 341, 0, 344, 352, 313, 224, 309, 301, 409, 256, 0, 0, 369, 427, 492]
}

df = pd.DataFrame(data)

# Adjusting the figure size
plt.figure(figsize=(14, 8))

# Creating the bubble chart
sns.scatterplot(data=df, x="MPG", y="Horsepower", size="CO2_Emissions", sizes=(20, 500),
                hue="CO2_Emissions", palette=["#003f5c", "#2f4b7c", "#665191", "#a05195",
                                               "#d45087", "#f95d6a", "#ff7c43", "#ffa600"])

# Customizing the appearance
plt.title("Vehicle Efficiency: MPG, Horsepower and CO2 Emissions", fontsize=16)
plt.xlabel("Fuel Efficiency (Miles per Gallon)", fontsize=14)
plt.ylabel("Horsepower", fontsize=14)

# Adjusting legend to avoid covering data points
plt.legend(title="CO2 Emissions (g/km)", loc='upper right', bbox_to_anchor=(1.15, 1), fontsize=12)

# Showing the final result
plt.show()