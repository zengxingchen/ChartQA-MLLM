
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'Visitors': [150, 160, 155, 165, 170, 180, 175, 190, 195, 200, 210, 215, 220, 225, 
                 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285, 290, 295, 300, 310]
}

df = pd.DataFrame(data)

sns.set_style("whitegrid")

plt.figure(figsize=(14, 7))
line_plot = sns.lineplot(x='Day', 
                         y='Visitors', 
                         data=df, 
                         color='#e74c3c', 
                         linewidth=2.5)

plt.annotate('Opening Day', xy=(1, 150), xytext=(4, 180),
             arrowprops=dict(facecolor='#34495e', shrink=0.05))
plt.annotate('End of Month', xy=(30, 310), xytext=(26, 320),
             arrowprops=dict(facecolor='#2ecc71', shrink=0.05))

plt.title('Daily Visitors to the Art Exhibit Over a Month')
plt.xlabel('Day of the Month')
plt.ylabel('Number of Visitors')

plt.show()