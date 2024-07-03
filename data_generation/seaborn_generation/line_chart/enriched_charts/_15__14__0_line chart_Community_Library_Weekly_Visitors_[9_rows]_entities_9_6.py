
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating the data
data = {
    'Day': [i for i in range(1, 32)],
    'Average Daily Temperature (°F)': [
        45, 47, 49, 46, 50, 48, 52, 53, 51, 55, 54, 56, 58, 59, 61, 
        60, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76
    ]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Setting the theme and size of the plot
sns.set_theme(style="whitegrid")
plt.figure(figsize=(14, 7))

# Creating the lineplot
temp_plot = sns.lineplot(
    x='Day',
    y='Average Daily Temperature (°F)',
    data=df,
    color="#FF5733",
    lw=2
)

# Adding title and labels
plt.title('Average Daily Temperature in New York Over a Month')
plt.xlabel('Day of the Month')
plt.ylabel('Average Temperature (°F)')

# Annotations: highlighting the highest temperature
plt.annotate(
    'Highest Temperature',
    xy=(31, 76),
    xytext=(28, 78),
    arrowprops=dict(facecolor='black', shrink=0.05),
    fontsize=12,
    color='#333333'
)

# Show the plot
plt.show()