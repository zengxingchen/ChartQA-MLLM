
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'Average_Distance_km': [3.2, 3.5, 4.0, 3.8, 4.2, 4.5, 4.8, 5.1, 5.4, 5.2, 
                            5.6, 6.0, 5.8, 6.2, 6.5, 6.8, 6.7, 7.0, 7.2, 7.5, 
                            7.8, 8.0, 8.2, 8.5, 8.8, 9.0, 9.2, 9.5, 9.7, 10.0]
}

df = pd.DataFrame(data)
sns.set_style("whitegrid")

plt.figure(figsize=(14, 8))
line_plot = sns.lineplot(x='Day', 
                         y='Average_Distance_km', 
                         data=df, 
                         color='#FF5733', 
                         linewidth=2.5)

plt.annotate('Start of month', xy=(1, 3.2), xytext=(5, 4),
             arrowprops=dict(facecolor='#34495e', shrink=0.05))
plt.annotate('End of month', xy=(30, 10.0), xytext=(25, 10.5),
             arrowprops=dict(facecolor='#2ecc71', shrink=0.05))

plt.title('Average Daily Running Distance Over a Month')
plt.xlabel('Day of the Month')
plt.ylabel('Average Distance (km)')

plt.show()