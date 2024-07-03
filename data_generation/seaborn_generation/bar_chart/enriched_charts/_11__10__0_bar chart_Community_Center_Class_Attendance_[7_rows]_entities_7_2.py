
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Monthly_Book_Sales_Thousands': [80, 85, 90, 100, 95, 105, 110, 120, 115, 130, 125, 140]
}

df = pd.DataFrame(data)

colors = ["#0073e6", "#e60073", "#33cc33", "#ffcc00", "#ff3300", 
          "#6600cc", "#33cccc", "#ff6699", "#ff9933", "#66ff66", 
          "#0099ff", "#ff99cc"]

plt.figure(figsize=(14, 8))

barplot = sns.barplot(
    x='Monthly_Book_Sales_Thousands',
    y='Month',
    data=df,
    palette=colors
)

for bar in barplot.patches:
    bar.set_height(0.4)

plt.title('Monthly Book Sales in Thousands')
plt.xlabel('Book Sales (Thousands)')
plt.ylabel('Month')

plt.tight_layout()
plt.show()