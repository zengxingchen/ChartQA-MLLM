
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'Visitors': [150, 160, 158, 145, 138, 132, 125, 135, 142, 150, 155, 160, 155, 152, 
                 145, 140, 138, 135, 128, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180]
}

df = pd.DataFrame(data)

sns.set_style("whitegrid")

plt.figure(figsize=(16, 8))
line_plot = sns.lineplot(x='Day', 
                         y='Visitors', 
                         data=df, 
                         color='#1abc9c', 
                         linewidth=2.5)

plt.annotate('Start of Month', xy=(1, 150), xytext=(4, 180),
             arrowprops=dict(facecolor='#2c3e50', shrink=0.05))
plt.annotate('End of Month', xy=(30, 180), xytext=(26, 190),
             arrowprops=dict(facecolor='#e74c3c', shrink=0.05))

plt.title('Monthly Decline in Gym Attendance', pad=20)
plt.xlabel('Day of the Month')
plt.ylabel('Number of Visitors')

plt.show()