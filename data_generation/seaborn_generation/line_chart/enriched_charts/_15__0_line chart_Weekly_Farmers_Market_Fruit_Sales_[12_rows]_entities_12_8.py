
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data based on the new topic
data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'Stress_Level': [3.2, 3.5, 3.7, 4.0, 4.3, 4.8, 5.0, 5.3, 5.8, 6.0, 
                     6.5, 6.9, 7.2, 7.5, 7.8, 8.0, 7.7, 7.5, 7.2, 6.8, 
                     6.5, 6.2, 6.0, 5.7, 5.3, 5.0, 4.7, 4.3, 4.0, 3.8]
}

df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Create the line chart
plt.figure(figsize=(14, 8))
line_plot = sns.lineplot(x='Day', 
                         y='Stress_Level', 
                         data=df, 
                         color='#e74c3c', 
                         linewidth=2.5)

# Annotating specific points
plt.annotate('Start of month', xy=(1, 3.2), xytext=(5, 4.5),
             arrowprops=dict(facecolor='#2980b9', shrink=0.05))
plt.annotate('Mid month peak', xy=(16, 8.0), xytext=(12, 7.5),
             arrowprops=dict(facecolor='#f39c12', shrink=0.05))
plt.annotate('End of month', xy=(30, 3.8), xytext=(25, 5.0),
             arrowprops=dict(facecolor='#27ae60', shrink=0.05))

# Setting chart title and labels
plt.title('Daily Stress Levels Over a Month', pad=20)
plt.xlabel('Day of the Month')
plt.ylabel('Stress Level')

# Show the final plot
plt.show()