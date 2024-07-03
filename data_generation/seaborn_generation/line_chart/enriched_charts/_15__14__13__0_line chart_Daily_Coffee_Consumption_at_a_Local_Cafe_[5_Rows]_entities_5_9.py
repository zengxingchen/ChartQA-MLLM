
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Temperature": [30, 32, 35, 40, 42, 45, 43, 44, 39, 37, 33, 31]
}

df = pd.DataFrame(data)

sns.set(style="whitegrid")

plt.figure(figsize=(14, 7))
line_plot = sns.lineplot(x="Month", y="Temperature", data=df, color="#3498db", marker="o")

line_plot.set_title('Monthly Temperature Variation in City XYZ', fontsize=18, pad=20)
line_plot.set_xlabel('Month')
line_plot.set_ylabel('Temperature in °C')

plt.annotate('Highest Temperature', xy=('June', 45), xytext=('April', 47),
             arrowprops=dict(facecolor='#e74c3c', shrink=0.05))

plt.show()