
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Revenue": [300, 450, 700, 950, 1200, 1400, 1600, 1550, 1350, 1150, 850, 500]
}

df = pd.DataFrame(data)

sns.set(style="whitegrid")

plt.figure(figsize=(12, 6))
line_plot = sns.lineplot(x="Month", y="Revenue", data=df, color="#e74c3c", marker="o")

line_plot.set_title('Monthly Revenue of a Local Bakery', fontsize=16, pad=20)
line_plot.set_xlabel('Month')
line_plot.set_ylabel('Revenue in USD')

plt.annotate('Highest Revenue', xy=('July', 1600), xytext=('June', 1700),
             arrowprops=dict(facecolor='#2ecc71', shrink=0.05))

plt.show()