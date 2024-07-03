
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the DataFrame directly
data = {
    'Year': [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    'Electric Vehicle Sales': [10, 20, 55, 75, 120, 155, 200, 350, 490, 610, 730]
}
df = pd.DataFrame(data)

# Initialize the matplotlib figure to set the size
f, ax = plt.subplots(figsize=(10, 6))

# Plotting the line chart
sns.lineplot(x="Year", y="Electric Vehicle Sales", data=df, palette=["#FF5733"], marker='o')

# Customizing the axes and title
ax.set_title('Global Electric Vehicle Sales Over Time')
ax.set_xlabel('Year')
ax.set_ylabel('Electric Vehicle Sales (in thousands)')

# Adding annotations for specific data points
for x, y in zip(df['Year'], df['Electric Vehicle Sales']):
    ax.text(x, y, y, color="black", ha="center")

# Show the plot
plt.show()