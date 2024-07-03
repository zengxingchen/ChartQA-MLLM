
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Temperature": [27, 30, 42, 55, 65, 74, 79, 78, 70, 58, 47, 35]
}

df = pd.DataFrame(data)

# Set the aesthetics for the plot
sns.set(style="darkgrid")

# Create the line plot with color scheme and size
plt.figure(figsize=(12, 6))
line_plot = sns.lineplot(x="Month", y="Temperature", data=df, color="#FF5733", marker="o")

# Change the headline and data type of the chart
line_plot.set_title('Average Monthly Temperatures in New York City')
line_plot.set_xlabel('Month')
line_plot.set_ylabel('Temperature (°F)')

# Annotate a specific data point
plt.annotate('Highest Average', xy=('July', 79), xytext=('August', 85),
             arrowprops=dict(facecolor='#FFC300', shrink=0.05))

# Show the plot
plt.show()