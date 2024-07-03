
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create DataFrame from the data provided
data = [
    {'Year': 2014, 'Smart Thermostats': 5.4, 'Smart Lights': 3.2, 'Smart Locks': 2.1, 'Smart Cameras': 4.7},
    {'Year': 2015, 'Smart Thermostats': 6.8, 'Smart Lights': 4.5, 'Smart Locks': 3.5, 'Smart Cameras': 5.6},
    {'Year': 2016, 'Smart Thermostats': 8.3, 'Smart Lights': 6.2, 'Smart Locks': 4.8, 'Smart Cameras': 7.1},
    {'Year': 2017, 'Smart Thermostats': 12.1, 'Smart Lights': 8.7, 'Smart Locks': 6.5, 'Smart Cameras': 9.4},
    {'Year': 2018, 'Smart Thermostats': 18.3, 'Smart Lights': 12.4, 'Smart Locks': 9.6, 'Smart Cameras': 14.3},
    {'Year': 2019, 'Smart Thermostats': 23.5, 'Smart Lights': 17.2, 'Smart Locks': 14.7, 'Smart Cameras': 18.9},
    {'Year': 2020, 'Smart Thermostats': 29.7, 'Smart Lights': 22.8, 'Smart Locks': 19.3, 'Smart Cameras': 23.4},
    {'Year': 2021, 'Smart Thermostats': 35.9, 'Smart Lights': 28.4, 'Smart Locks': 25.2, 'Smart Cameras': 29.1},
    {'Year': 2022, 'Smart Thermostats': 42.3, 'Smart Lights': 35.1, 'Smart Locks': 32.8, 'Smart Cameras': 35.7}
]
df = pd.DataFrame(data)
df = pd.melt(df, id_vars='Year', var_name='Device', value_name='Sales')

# Set the Seaborn style
sns.set_theme(style="whitegrid")

# Create the lineplot
sns.lineplot(data=df, x='Year', y='Sales', hue='Device', style='Device', 
             markers=True, dashes=False, palette='tab10', linewidth=2.5)

# Adding titles and labels
plt.title('Smart Device Sales Over Years')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Sales (Millions)', fontsize=12)

# Display legend
plt.legend(title='Device Type')

# Optionally, you could save the figure
# plt.savefig('smart_device_sales.png', dpi=300)

# Show the plot
plt.show()