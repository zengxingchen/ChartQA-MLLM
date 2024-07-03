
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating the data
data = {
    'Day': [i for i in range(1, 32)],
    'Average Daily Humidity (%)': [
        65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 
        83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95
    ],
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Setting the theme and size of the plot, as well as choosing a palette
sns.set_theme(style="whitegrid")
plt.figure(figsize=(16, 8))

# Creating the lineplot
humidity_plot = sns.lineplot(
    x='Day',
    y='Average Daily Humidity (%)',
    data=df,
    color="#1E90FF",
    lw=2
)

# Adding title and labels
plt.title('Average Daily Humidity Over a Month in a Tropical Region', fontsize=16, pad=20)
plt.xlabel('Day of the Month', fontsize=12)
plt.ylabel('Average Humidity (%)', fontsize=12)

# Annotations: highlighting the peak humidity
plt.annotate(
    'Peak Humidity',
    xy=(31, 95),
    xytext=(28, 97),
    arrowprops=dict(facecolor='black', shrink=0.05),
    fontsize=12,
    color='#333333'
)

# Show the plot
plt.show()