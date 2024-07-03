
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating the data
data = {
    'Day': [i for i in range(1, 32)],
    'Average Daily Humidity (%)': [
        55.0, 57.2, 56.3, 58.1, 59.4, 60.8, 62.2, 61.6, 60.1, 58.8, 57.9,
        56.5, 57.6, 55.7, 54.3, 53.2, 52.1, 51.6, 53.4, 54.8, 56.2, 55.3,
        57.0, 58.7, 59.3, 60.6, 61.9, 62.5, 63.8, 64.4, 65.2
    ],
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Setting the theme and size of the plot, as well as choosing a palette
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 8))

# Creating the lineplot
humidity_plot = sns.lineplot(
    x='Day',
    y='Average Daily Humidity (%)',
    data=df,
    color="#3498DB",
    lw=2
)

# Adding title and labels
plt.title('Average Daily Humidity Over a Month in Coastal City', fontsize=14)
plt.xlabel('Day of the Month', fontsize=12)
plt.ylabel('Average Humidity (%)', fontsize=12)

# Annotations: highlighting the peak humidity
plt.annotate(
    'Peak Humidity',
    xy=(31, 65.2),
    xytext=(28, 66),
    arrowprops=dict(facecolor='black', shrink=0.05),
    fontsize=12,
    color='#333333'
)

# Show the plot
plt.show()