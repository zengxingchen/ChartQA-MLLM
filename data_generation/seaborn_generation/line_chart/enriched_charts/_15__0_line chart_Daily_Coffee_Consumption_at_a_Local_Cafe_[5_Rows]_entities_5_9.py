
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Productivity": [50, 60, 55, 65, 70, 80, 75, 70, 60, 65, 55, 50]
}

df = pd.DataFrame(data)

# Set the aesthetics for the plot
sns.set(style="darkgrid")

# Create the line plot with color scheme and size
plt.figure(figsize=(14, 7))
line_plot = sns.lineplot(x="Month", y="Productivity", data=df, color="#1F77B4", marker="o")

# Change the headline and data type of the chart
line_plot.set_title('Monthly Productivity in a Software Development Team')
line_plot.set_xlabel('Month')
line_plot.set_ylabel('Productivity Score')

# Annotate a specific data point
plt.annotate('Highest Productivity', xy=('June', 80), xytext=('July', 85),
             arrowprops=dict(facecolor='#FF7F0E', shrink=0.05))

# Show the plot
plt.show()