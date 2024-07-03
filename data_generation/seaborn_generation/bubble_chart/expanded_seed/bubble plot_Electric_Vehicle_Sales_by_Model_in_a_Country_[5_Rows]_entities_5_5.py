
import seaborn as sns
import matplotlib.pyplot as plt

# Your given data
data = [
    {'Model': 'Tesla Model 3', 'Year': 2021, 'Sales (Units)': 80000, 'Battery Capacity (kWh)': 60, 'Average Range (Miles)': 263},
    {'Model': 'Chevrolet Bolt', 'Year': 2021, 'Sales (Units)': 20000, 'Battery Capacity (kWh)': 66, 'Average Range (Miles)': 259},
    {'Model': 'Nissan Leaf', 'Year': 2021, 'Sales (Units)': 15000, 'Battery Capacity (kWh)': 40, 'Average Range (Miles)': 150},
    {'Model': 'Ford Mustang Mach-E', 'Year': 2021, 'Sales (Units)': 25000, 'Battery Capacity (kWh)': 75, 'Average Range (Miles)': 300},
    {'Model': 'Porsche Taycan', 'Year': 2021, 'Sales (Units)': 5000, 'Battery Capacity (kWh)': 93, 'Average Range (Miles)': 227}
]

# Convert the data to a DataFrame
import pandas as pd
df = pd.DataFrame(data)

# Create a scatter plot using seaborn
plt.figure(figsize=(10, 6))
bubble_chart = sns.scatterplot(
    data=df,
    x='Battery Capacity (kWh)',
    y='Average Range (Miles)',
    size='Sales (Units)',
    hue='Model',
    sizes=(100, 1000),  # Range of bubble sizes
    palette='Set2',  # Color palette for different car models
    legend='full'  # Include legend for car models
)

# Customize the axes and title
plt.title('EV Sales, Battery Capacity, and Average Range in 2021')
plt.xlabel('Battery Capacity (kWh)')
plt.ylabel('Average Range (Miles)')

# Show the plotted bubble chart
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()