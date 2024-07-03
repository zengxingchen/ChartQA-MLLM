
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create dataframe
data = {
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']*4,
    'Year': [2010]*10 + [2011]*10 + [2012]*10 + [2013]*10,
    'Attendance': [
        30000, 28000, 25000, 22000, 27000, 24000, 21000, 23000, 26000, 20000,
        32000, 29000, 26000, 23000, 28000, 25000, 22000, 24000, 27000, 21000,
        31000, 30000, 25500, 22500, 27500, 24500, 21500, 23500, 26500, 20500,
        33000, 31000, 26500, 23500, 28500, 25500, 22500, 24500, 27500, 21500
    ]
}
df = pd.DataFrame(data)

# Scatterplot
plt.figure(figsize=(14, 10))
scatter_plot = sns.scatterplot(
    x='Year', 
    y='Attendance', 
    data=df, 
    hue='City', 
    palette=[
        '#FF5733', '#33FF57', '#3357FF', '#57FFFF', 
        '#FF33FF', '#FFFF33', '#FF8333', '#33FF83', 
        '#8333FF', '#FF3383'
    ]
)

# Customizing the chart
plt.title('Yearly Attendance at Major Concerts in Various Cities', pad=20)
plt.xlabel('Year')
plt.ylabel('Attendance')

# Show the plot
plt.show()