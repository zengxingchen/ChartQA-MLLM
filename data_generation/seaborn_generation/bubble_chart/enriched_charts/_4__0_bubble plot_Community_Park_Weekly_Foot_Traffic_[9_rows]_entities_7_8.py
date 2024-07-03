
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {
    'Country': ['USA', 'USA', 'China', 'China', 'India', 'India', 'Germany', 'Germany', 'Brazil', 'Brazil', 'France', 'France'],
    'FoodType': ['Fruits', 'Vegetables', 'Fruits', 'Vegetables', 'Fruits', 'Vegetables', 'Fruits', 'Vegetables', 'Fruits', 'Vegetables', 'Fruits', 'Vegetables'],
    'NumberOfConsumers': [100000, 80000, 150000, 90000, 130000, 70000, 60000, 50000, 50000, 40000, 55000, 35000],
    'CaloriesIntake': [52, 34, 60, 30, 50, 28, 55, 25, 58, 32, 53, 29]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create the bubble chart
plt.figure(figsize=(16, 12))
bubble_plot = sns.scatterplot(data=df, x='Country', y='CaloriesIntake', size='NumberOfConsumers', hue='FoodType',
                              sizes=(100, 2000), alpha=0.7, palette=["#FFA07A", "#20B2AA"])

# Customize legend and axis labels
bubble_plot.legend(title='Food Type', loc='upper right')
plt.xlabel('Country')
plt.ylabel('Calories Intake (kcal)')
plt.title('Calories Intake by Food Type in Different Countries', pad=20)

# Show the plot
plt.show()