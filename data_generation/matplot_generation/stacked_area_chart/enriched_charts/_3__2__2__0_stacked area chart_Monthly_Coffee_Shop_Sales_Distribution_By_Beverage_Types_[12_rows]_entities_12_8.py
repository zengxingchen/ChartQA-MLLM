
import matplotlib.pyplot as plt
import pandas as pd

# Generate data points
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'New Technologies': [45, 50, 55, 60, 70, 80, 90, 85, 95, 100, 110, 120],
    'Adoption Rate': [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],
    'Projected Growth': [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
}

df = pd.DataFrame(data)

# Set the figure size
plt.figure(figsize=(18, 10))

# Plotting the stacked area chart
plt.stackplot(df['Month'],
              df['New Technologies'], df['Adoption Rate'], df['Projected Growth'],
              labels=['New Technologies', 'Adoption Rate', 'Projected Growth'],
              colors=['#FF5733', '#33FF57', '#3357FF'])

# Add title and labels
plt.title('Monthly Adoption and Growth of New Technologies', pad=20)
plt.xlabel('Month')
plt.ylabel('Metrics')

# Add legend
plt.legend(loc='upper right')

# Annotate specific data points
for i, (mon, tech, adopt, growth) in enumerate(zip(df['Month'], df['New Technologies'], df['Adoption Rate'], df['Projected Growth'])):
    if mon == 'December':
        plt.text(i, tech+adopt+growth, f'{tech+adopt+growth}', ha='center', va='bottom')

# Show the plot
plt.show()