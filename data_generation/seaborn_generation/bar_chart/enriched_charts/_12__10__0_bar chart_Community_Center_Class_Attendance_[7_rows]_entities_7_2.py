
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Monthly_Internet_Users_Millions': [120, 115, 130, 140, 155, 160, 175, 170, 160, 150, 145, 130]
}

df = pd.DataFrame(data)

colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", 
          "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf", 
          "#9edae5", "#aec7e8"]

plt.figure(figsize=(14, 8))

barplot = sns.barplot(
    x='Monthly_Internet_Users_Millions',
    y='Month',
    data=df,
    palette=colors
)

for bar in barplot.patches:
    bar.set_height(0.7)

plt.title('Monthly Internet Users in a City', pad=20)
plt.xlabel('Internet Users (Millions)')
plt.ylabel('Month')

plt.tight_layout()
plt.show()