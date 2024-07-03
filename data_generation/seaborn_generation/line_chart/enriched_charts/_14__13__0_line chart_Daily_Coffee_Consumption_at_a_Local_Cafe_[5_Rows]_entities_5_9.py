
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Profit": [300, 400, 500, 600, 700, 850, 900, 950, 1000, 1050, 1100, 1150]
}

df = pd.DataFrame(data)

sns.set(style="whitegrid")

plt.figure(figsize=(12, 6))
line_plot = sns.lineplot(x="Month", y="Profit", data=df, color="#2ecc71", marker="o")

line_plot.set_title('Monthly Profit of XYZ Corp', fontsize=16, pad=20)
line_plot.set_xlabel('Month')
line_plot.set_ylabel('Profit in $1000s')

plt.annotate('End of Fiscal Year', xy=('December', 1150), xytext=('October', 1200),
             arrowprops=dict(facecolor='#e74c3c', shrink=0.05))

plt.show()