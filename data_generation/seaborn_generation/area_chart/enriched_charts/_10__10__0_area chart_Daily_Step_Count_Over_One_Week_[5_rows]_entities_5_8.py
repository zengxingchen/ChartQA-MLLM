
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    'Calories_Burned': [220, 230, 225, 240, 235, 250, 245, 260, 255, 270, 265, 280, 275, 290, 285, 300, 295, 310, 305, 320, 315, 330, 325, 340, 335, 350, 345, 360, 355, 370, 365]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 10))
area_chart = sns.lineplot(data=df, x='Day', y='Calories_Burned', color='#FF6347')
area_chart.fill_between(df['Day'], df['Calories_Burned'], color='#FFA07A', alpha=0.5)

max_calories = df['Calories_Burned'].max()
max_day = df['Calories_Burned'].idxmax() + 1
plt.text(max_day, max_calories, 'Peak\nCalories', horizontalalignment='center', verticalalignment='bottom', color='#2E8B57')

plt.title("Daily Calories Burned Over a Month", pad=20)
plt.xlabel("Day of the Month")
plt.ylabel("Calories Burned")

plt.show()