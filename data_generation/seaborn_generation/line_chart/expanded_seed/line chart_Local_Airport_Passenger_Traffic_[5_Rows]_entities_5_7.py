
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create DataFrame from the provided data
data = [
    {'Year': 2019, 'Domestic Passengers': 540000, 'International Passengers': 230000},
    {'Year': 2020, 'Domestic Passengers': 150000, 'International Passengers': 50000},
    {'Year': 2021, 'Domestic Passengers': 210000, 'International Passengers': 60000},
    {'Year': 2022, 'Domestic Passengers': 340000, 'International Passengers': 140000},
    {'Year': 2023, 'Domestic Passengers': 380000, 'International Passengers': 160000}
]
df = pd.DataFrame(data)

# Melt the DataFrame to long format suitable for seaborn
df_melted = df.melt('Year', var_name='Type', value_name='Passengers')

# Create the lineplot with seaborn
sns.set_theme(style="darkgrid")
plt.figure(figsize=(10, 6))
lineplot = sns.lineplot(
    x='Year', 
    y='Passengers', 
    hue='Type', 
    style='Type', 
    data=df_melted, 
    markers=True, # To use markers for each data point
    dashes=False # To have solid lines for each category
)

# Customize the plot with titles and labels
plt.title('Yearly Passengers: Domestic vs International', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Passengers', fontsize=12)

# Annotate each data point on the plot
for index, row in df_melted.iterrows():
    lineplot.annotate(
        text=row['Passengers'], 
        xy=(row['Year'], row['Passengers']),
        textcoords="offset points",
        xytext=(0,5),
        ha='center'
    )

# Show the final plot
plt.legend(title='Passenger Type')
plt.tight_layout()
plt.show()