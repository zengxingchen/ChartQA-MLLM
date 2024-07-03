
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the DataFrame directly
data = {
    'Year': [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    'Average Daily Steps': [4500, 4700, 4800, 4900, 5000, 5100, 5200, 5300, 5400, 5500, 5600]
}
df = pd.DataFrame(data)

# Initialize the matplotlib figure to set the size
f, ax = plt.subplots(figsize=(12, 8))

# Plotting the line chart
sns.lineplot(x="Year", y="Average Daily Steps", data=df, color="#4CAF50", marker='o')

# Customizing the axes and title
ax.set_title('Average Daily Steps Over Time', fontsize=16, pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Average Daily Steps', fontsize=12)

# Adding annotations for specific data points
for x, y in zip(df['Year'], df['Average Daily Steps']):
    ax.text(x, y, y, color="black", ha="center", va="bottom")

# Show the plot
plt.show()