
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating the data
data = {
    'Day': [i for i in range(1, 32)],
    'Average Daily Rainfall (inches)': [
        0.2, 0.15, 0.3, 0.1, 0.25, 0.4, 0.35, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8,
        0.85, 0.9, 0.95, 1.0, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.55, 1.6
    ]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Setting the theme and size of the plot
sns.set_theme(style="whitegrid")
plt.figure(figsize=(16, 8))

# Creating the lineplot
rainfall_plot = sns.lineplot(
    x='Day',
    y='Average Daily Rainfall (inches)',
    data=df,
    color="#1f77b4",
    lw=2
)

# Adding title and labels
plt.title('Average Daily Rainfall in Seattle Over a Month')
plt.xlabel('Day of the Month')
plt.ylabel('Average Rainfall (inches)')

# Annotations: highlighting the peak rainfall
plt.annotate(
    'Peak Rainfall',
    xy=(31, 1.6),
    xytext=(28, 1.7),
    arrowprops=dict(facecolor='black', shrink=0.05),
    fontsize=12,
    color='#333333'
)

# Show the plot
plt.show()