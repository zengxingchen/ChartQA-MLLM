
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Calorie Intake": [2200, 2100, 2300, 2400, 2500, 2600, 2550, 2450, 2350, 2250, 2150, 2050]
}

df = pd.DataFrame(data)

sns.set(style="whitegrid")

plt.figure(figsize=(12, 6))
line_plot = sns.lineplot(x="Month", y="Calorie Intake", data=df, color="#FF6347", marker="o")

line_plot.set_title('Monthly Average Calorie Intake in 2023', fontsize=18, pad=20)
line_plot.set_xlabel('Month')
line_plot.set_ylabel('Calorie Intake (kcal)')

plt.annotate('Lowest Intake', xy=('December', 2050), xytext=('November', 2100),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05))

plt.show()