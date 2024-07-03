
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Let's create the data directly since this is just about visualization
data = {
    'Day': [i for i in range(1, 32)],
    'Average Daily Temperature (°F)': [
        101.5, 99.2, 100.3, 102.1, 103.4, 104.8, 106.2, 105.6, 104.1,
        102.8, 101.9, 100.5, 101.6, 99.7, 98.3, 97.2, 96.1, 95.6, 97.4,
        98.8, 100.2, 99.3, 101.0, 102.7, 103.3, 104.6, 105.9, 106.5,
        107.8, 108.4, 109.2
    ],
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Setting the theme and size of the plot, as well as choosing a palette.
sns.set_theme(style="whitegrid")
plt.figure(figsize=(14, 6))

# Creating the lineplot
temp_plot = sns.lineplot(
    x='Day',
    y='Average Daily Temperature (°F)',
    data=df,
    palette=["#FF5733"],
    lw=2
)

# Adding title and labels
plt.title('Average Daily Temperature in Death Valley Over a Month')
plt.xlabel('Day of the Month')
plt.ylabel('Average Temperature (°F)')

# Annotations: highlighting the peak temperature
plt.annotate(
    'Peak Temperature',
    xy=(31, 109.2),
    xytext=(28, 110),
    arrowprops=dict(facecolor='black', shrink=0.05),
    fontsize=12,
    color='#333333'
)

# Show the plot
plt.show()