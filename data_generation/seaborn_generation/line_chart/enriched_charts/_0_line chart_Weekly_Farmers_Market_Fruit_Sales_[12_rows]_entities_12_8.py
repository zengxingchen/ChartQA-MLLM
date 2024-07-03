
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data based on the table above
data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'Average_Temperature_C': [14.2, 14.5, 13.7, 13.9, 14.1, 15.2, 15.6, 16.2, 17.3, 17.7, 
                              18.1, 18.4, 18.9, 19.0, 19.5, 20.2, 20.3, 21.5, 21.2, 21.9, 
                              22.5, 23.1, 23.4, 24.5, 24.2, 25.1, 25.5, 25.3, 25.9, 26.4]
}

df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Create the line chart
plt.figure(figsize=(12, 6))
line_plot = sns.lineplot(x='Day', 
                         y='Average_Temperature_C', 
                         data=df, 
                         color='#3498db', 
                         linewidth=2.5)

# Annotating specific points
plt.annotate('Start of month', xy=(1, 14.2), xytext=(5, 15),
             arrowprops=dict(facecolor='#34495e', shrink=0.05))
plt.annotate('End of month', xy=(30, 26.4), xytext=(25, 27),
             arrowprops=dict(facecolor='#2ecc71', shrink=0.05))

# Setting chart title and labels
plt.title('Average Daily Temperature Trend Over a Month')
plt.xlabel('Day of the Month')
plt.ylabel('Average Temperature (C)')

# Show the final plot
plt.show()