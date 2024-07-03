
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the DataFrame directly
data = {
    'Year': [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    'Renewable Energy Investment (in billion USD)': [150, 170, 180, 220, 210, 240, 280, 300, 330, 350, 370]
}
df = pd.DataFrame(data)

# Initialize the matplotlib figure to set the size
f, ax = plt.subplots(figsize=(12, 8))

# Plotting the line chart
sns.lineplot(x="Year", y="Renewable Energy Investment (in billion USD)", data=df, color="#1f77b4", marker='o')

# Customizing the axes and title
ax.set_title('Global Renewable Energy Investment Over Time', fontsize=16)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Investment (in billion USD)', fontsize=14)

# Adding annotations for specific data points
for x, y in zip(df['Year'], df['Renewable Energy Investment (in billion USD)']):
    ax.text(x, y, y, color="black", ha="center", fontsize=10)

# Show the plot
plt.show()