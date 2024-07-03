
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'DailyWaterIntake': [2.1, 2.4, 1.8, 2.7, 2.2, 3.0, 1.9, 2.5, 1.7, 2.8, 2.6, 1.6, 2.9, 2.3, 2.0, 2.4, 1.8, 3.1, 2.2, 2.5, 1.9, 2.7, 2.1, 2.8, 2.3, 2.6, 1.7, 3.0, 2.5, 1.8],
    'HydrationLevel': [75, 80, 70, 85, 78, 88, 72, 82, 68, 86, 84, 65, 87, 79, 73, 81, 69, 89, 77, 83, 71, 85, 76, 86, 80, 83, 66, 88, 82, 70]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 10))
scatterplot = sns.scatterplot(x='DailyWaterIntake', y='HydrationLevel', data=df, color='#4682B4')

scatterplot.set_title('Daily Water Intake vs Hydration Level', fontsize=18, pad=20)
scatterplot.set_xlabel('Daily Water Intake (liters)', fontsize=14)
scatterplot.set_ylabel('Hydration Level (%)', fontsize=14)

plt.show()