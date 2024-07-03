
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the DataFrame directly
data = {
    'Year': [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    'Average Miles Traveled': [2000, 2500, 2700, 2400, 2800, 3000, 3100, 2900, 3300, 3500, 3700]
}
df = pd.DataFrame(data)

# Initialize the matplotlib figure to set the size
f, ax = plt.subplots(figsize=(14, 9))

# Plotting the line chart
sns.lineplot(x="Year", y="Average Miles Traveled", data=df, color="#1E90FF", marker='s')

# Customizing the axes and title
ax.set_title('Average Miles Traveled Over Time', fontsize=20, pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Average Miles Traveled', fontsize=14)

# Adding annotations for specific data points
for x, y in zip(df['Year'], df['Average Miles Traveled']):
    ax.text(x, y, y, color="black", ha="center", va="bottom")

# Show the plot
plt.show()