
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data for the chart
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Average_Temperature_C': [5.2, 6.1, 10.5, 14.8, 19.2, 23.5, 27.8, 26.9, 21.4, 15.2, 10.1, 6.8]
}

df = pd.DataFrame(data)
sns.set_style("whitegrid")

plt.figure(figsize=(16, 10))
line_plot = sns.lineplot(x='Month', 
                         y='Average_Temperature_C', 
                         data=df, 
                         color='#3498db', 
                         linewidth=3.0)

plt.annotate('Winter', xy=('January', 5.2), xytext=('March', 7.0),
             arrowprops=dict(facecolor='#e74c3c', shrink=0.05))
plt.annotate('Summer Peak', xy=('July', 27.8), xytext=('May', 25.0),
             arrowprops=dict(facecolor='#2ecc71', shrink=0.05))

plt.title('Monthly Average Temperature Over a Year', fontsize=18, pad=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Average Temperature (°C)', fontsize=14)

plt.show()