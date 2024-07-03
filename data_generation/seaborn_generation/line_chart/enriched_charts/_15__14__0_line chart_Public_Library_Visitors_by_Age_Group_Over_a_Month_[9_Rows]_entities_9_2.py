
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the DataFrame directly
data = {
    'Year': [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    'Annual Space Exploration Budget (in billion USD)': [15, 17, 20, 18, 22, 25, 28, 30, 32, 35, 37]
}
df = pd.DataFrame(data)

# Initialize the matplotlib figure to set the size
f, ax = plt.subplots(figsize=(14, 9))

# Plotting the line chart
sns.lineplot(x="Year", y="Annual Space Exploration Budget (in billion USD)", data=df, color="#2ca02c", marker='o')

# Customizing the axes and title
ax.set_title('Annual Space Exploration Budget Over Time', fontsize=18, pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Budget (in billion USD)', fontsize=14)

# Adding annotations for specific data points
for x, y in zip(df['Year'], df['Annual Space Exploration Budget (in billion USD)']):
    ax.text(x, y, y, color="black", ha="center", fontsize=10)

# Show the plot
plt.show()