
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Stock Price": [120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175]
}

df = pd.DataFrame(data)

sns.set(style="darkgrid")

plt.figure(figsize=(14, 8))
line_plot = sns.lineplot(x="Month", y="Stock Price", data=df, color="#2E86C1", marker="o")

line_plot.set_title('Monthly Average Stock Prices in 2023', fontsize=16)
line_plot.set_xlabel('Month')
line_plot.set_ylabel('Stock Price (USD)')

plt.annotate('Highest Price', xy=('December', 175), xytext=('November', 180),
             arrowprops=dict(facecolor='#FF5733', shrink=0.05))

plt.show()