import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create dataframe
data = {
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']*4,
    'Year': [2010]*10 + [2011]*10 + [2012]*10 + [2013]*10,
    'SalesVolume': [
        157, 168, 122, 203, 234, 145, 208, 171, 200, 185, 
        161, 172, 115, 212, 241, 139, 215, 179, 210, 192, 
        165, 175, 119, 218, 247, 143, 219, 182, 220, 198,
        170, 178, 125, 225, 253, 147, 223, 185, 225, 202
    ]
}
df = pd.DataFrame(data)

# Scatterplot
plt.figure(figsize=(14, 10))
scatter_plot = sns.scatterplot(
    x='Year', 
    y='SalesVolume', 
    data=df, 
    hue='City', 
    palette=[
        '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', 
        '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', 
        '#bcbd22', '#17becf'
    ]
)

# Customizing the chart
plt.title('Yearly Sales Volume of Various Cities in the Fashion Industry', fontsize=16, pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Sales Volume (in thousands)', fontsize=14)

# Show the plot
plt.show()