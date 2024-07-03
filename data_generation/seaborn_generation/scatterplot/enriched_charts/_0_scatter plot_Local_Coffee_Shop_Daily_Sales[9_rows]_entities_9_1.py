
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create dataframe
data = {
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']*2,
    'Year': [2010]*10 + [2011]*10,
    'AverageTemperature': [15.7, 16.8, 12.2, 20.3, 23.4, 14.5, 20.8, 17.1, 20.0, 18.5, 16.1, 17.2, 11.5, 21.2, 24.1, 13.9, 21.5, 17.9, 21.0, 19.2]
}
df = pd.DataFrame(data)

# Scatterplot
plt.figure(figsize=(12, 8))
scatter_plot = sns.scatterplot(
    x='Year', 
    y='AverageTemperature', 
    data=df, 
    hue='City', 
    palette=[
        '#FF5733', '#33FF57', '#3357FF', '#57FFFF', 
        '#FF33FF', '#FFFF33', '#FF8333', '#33FF83', 
        '#8333FF', '#FF3383'
    ]
)

# Customizing the chart ( Topic Changed to 'Yearly Average Temperature of Various Cities' )
plt.title('Yearly Average Temperature of Various Cities')
plt.xlabel('Year')
plt.ylabel('Average Temperature (°C)')

# Show the plot
plt.show()