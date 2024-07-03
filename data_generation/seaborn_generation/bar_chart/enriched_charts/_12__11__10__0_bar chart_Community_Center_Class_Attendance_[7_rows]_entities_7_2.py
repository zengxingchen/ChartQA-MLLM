
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Monthly_Gym_Membership_Signups': [200, 220, 250, 230, 240, 260, 270, 280, 290, 310, 320, 330]
}

df = pd.DataFrame(data)

colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", 
          "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf", 
          "#9edae5", "#f7b6d2"]

plt.figure(figsize=(12, 10))

barplot = sns.barplot(
    x='Month',
    y='Monthly_Gym_Membership_Signups',
    data=df,
    palette=colors
)

for bar in barplot.patches:
    bar.set_width(0.5)

plt.title('Monthly Gym Membership Signups', fontsize=16, pad=20)
plt.xlabel('Month')
plt.ylabel('Signups')

plt.tight_layout()
plt.show()