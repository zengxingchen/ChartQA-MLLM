
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Visitors": [500, 800, 1200, 1500, 1800, 2200, 2400, 2300, 2100, 1900, 1300, 700]
}

df = pd.DataFrame(data)

sns.set(style="whitegrid")

plt.figure(figsize=(14, 7))
line_plot = sns.lineplot(x="Month", y="Visitors", data=df, color="#3498db", marker="o")

line_plot.set_title('Monthly Visitors to Central Park', fontsize=16, pad=20)
line_plot.set_xlabel('Month')
line_plot.set_ylabel('Number of Visitors')

plt.annotate('Peak Season', xy=('July', 2400), xytext=('June', 2500),
             arrowprops=dict(facecolor='#e74c3c', shrink=0.05))

plt.show()