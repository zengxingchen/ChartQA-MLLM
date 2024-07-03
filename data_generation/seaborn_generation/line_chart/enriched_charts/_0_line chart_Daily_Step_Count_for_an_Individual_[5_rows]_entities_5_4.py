
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Generate a DataFrame with the data
data = {
    'Day': [i for i in range(1, 366)],
    'Average_Temperature_C': [-2 + 0.5 * ((i // 30) % 12) for i in range(1, 366)]
}

# Custom adjustments for the data to follow the given requirement
data['Average_Temperature_C'][120] = 20  # A peak in the data for illustration
data['Average_Temperature_C'][240] = -10 # A dip in the data for illustration

df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_theme(style="whitegrid")

# Create and size the seaborn lineplot
plt.figure(figsize=(12, 6))
plot = sns.lineplot(x='Day', y='Average_Temperature_C', data=df, linewidth=2.5, color="#FF5733")

# Annotate a specific point with a peak temperature
plt.annotate('Peak temp', 
             xy=(121, df.loc[120, 'Average_Temperature_C']), 
             xycoords='data',
             xytext=(150, 25),
             textcoords='data',
             arrowprops=dict(arrowstyle="->",
                             connectionstyle="arc3"),
             )

# Annotate a specific point with a dip temperature
plt.annotate('Dip temp', 
             xy=(241, df.loc[240, 'Average_Temperature_C']), 
             xycoords='data',
             xytext=(210, -15),
             textcoords='data',
             arrowprops=dict(arrowstyle="->",
                             connectionstyle="arc3"),
             )

# Set the title and labels
plt.title('Yearly Temperature Trend')
plt.xlabel('Day of the Year')
plt.ylabel('Average Daily Temperature (°C)')

# Show the plot
plt.show()