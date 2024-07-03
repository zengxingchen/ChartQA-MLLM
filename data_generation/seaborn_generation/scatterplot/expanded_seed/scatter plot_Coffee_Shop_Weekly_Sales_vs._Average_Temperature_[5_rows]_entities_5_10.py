
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Creating a DataFrame from the provided data
data = [
    {'Day': 'Monday', 'Weekly Sales (USD)': 1570, 'Average Temperature (Fahrenheit)': 70},
    {'Day': 'Tuesday', 'Weekly Sales (USD)': 1830, 'Average Temperature (Fahrenheit)': 68},
    {'Day': 'Wednesday', 'Weekly Sales (USD)': 1725, 'Average Temperature (Fahrenheit)': 71},
    {'Day': 'Thursday', 'Weekly Sales (USD)': 1900, 'Average Temperature (Fahrenheit)': 67},
    {'Day': 'Friday', 'Weekly Sales (USD)': 2050, 'Average Temperature (Fahrenheit)': 69}
]

df = pd.DataFrame(data)

# Create a scatterplot using Seaborn
# Using hue for categorical day differentiation, size for encoding weekly sales,
# and style to diversify markers for days.
plt.figure(figsize=(10, 6))  # Set the figure size
scatter_plot = sns.scatterplot(x='Average Temperature (Fahrenheit)', 
                               y='Weekly Sales (USD)', 
                               hue='Day', 
                               size='Weekly Sales (USD)',
                               style='Day', 
                               sizes=(100, 500), # Customize marker sizes
                               data=df)

# Customizing the plot with title and labels
plt.title('Scatterplot of Weekly Sales vs. Average Temperature')
plt.xlabel('Average Temperature (Fahrenheit)')
plt.ylabel('Weekly Sales (USD)')
plt.legend(title='Day of the week')

# Show the plot
plt.show()