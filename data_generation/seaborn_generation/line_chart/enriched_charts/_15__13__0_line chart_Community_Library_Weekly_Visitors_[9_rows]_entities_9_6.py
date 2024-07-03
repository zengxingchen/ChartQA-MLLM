
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating the data
data = {
    'Day': [i for i in range(1, 32)],
    'Average Daily Temperature (°C)': [
        15.0, 16.2, 14.8, 17.5, 18.9, 20.1, 21.4, 22.6, 23.5, 24.2, 23.9,
        22.8, 21.2, 20.4, 19.1, 18.0, 17.6, 19.5, 20.3, 21.9, 23.1, 24.0,
        25.2, 26.4, 27.3, 28.1, 29.2, 30.0, 30.8, 31.5, 32.1
    ],
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Setting the theme and size of the plot, as well as choosing a palette
sns.set_theme(style="whitegrid")
plt.figure(figsize=(14, 9))

# Creating the lineplot
temperature_plot = sns.lineplot(
    x='Day',
    y='Average Daily Temperature (°C)',
    data=df,
    color="#E74C3C",
    lw=2
)

# Adding title and labels
plt.title('Average Daily Temperature Over a Month in a Mountainous Region', fontsize=16, pad=20)
plt.xlabel('Day of the Month', fontsize=14)
plt.ylabel('Average Temperature (°C)', fontsize=14)

# Annotations: highlighting the peak temperature
plt.annotate(
    'Peak Temperature',
    xy=(31, 32.1),
    xytext=(28, 33),
    arrowprops=dict(facecolor='black', shrink=0.05),
    fontsize=12,
    color='#333333'
)

# Show the plot
plt.show()