
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating the data
data = {
    'Day': [i for i in range(1, 32)],
    'Average Daily Temperature (°C)': [
        10.5, 11.2, 12.0, 13.8, 14.6, 15.3, 15.9, 16.5, 17.0, 17.4, 17.8,
        18.2, 18.6, 19.0, 19.3, 19.5, 19.7, 19.9, 20.0, 20.1, 20.0, 19.8,
        19.5, 19.1, 18.6, 18.0, 17.3, 16.5, 15.6, 14.6, 13.5
    ],
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Setting the theme and size of the plot, as well as choosing a palette
sns.set_theme(style="whitegrid")
plt.figure(figsize=(14, 10))

# Creating the lineplot
temperature_plot = sns.lineplot(
    x='Day',
    y='Average Daily Temperature (°C)',
    data=df,
    color="#FF5733",
    lw=2
)

# Adding title and labels
plt.title('Average Daily Temperature Over a Month in a Mountainous Region', fontsize=16, pad=20)
plt.xlabel('Day of the Month', fontsize=12)
plt.ylabel('Average Temperature (°C)', fontsize=12)

# Annotations: highlighting the peak temperature
plt.annotate(
    'Peak Temperature',
    xy=(20, 20.1),
    xytext=(18, 21),
    arrowprops=dict(facecolor='black', shrink=0.05),
    fontsize=12,
    color='#333333'
)

# Show the plot
plt.show()