
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Day': [i for i in range(1, 32)],
    'Calories_Burned': [
        200, 210, 220, 215, 225, 235, 240, 245, 250, 255, 
        260, 265, 270, 275, 280, 285, 290, 295, 300, 305, 
        310, 315, 320, 325, 330, 335, 340, 345, 350, 355, 360
    ]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 8))

sns.lineplot(x='Day', y='Calories_Burned', data=df, color='#FF4500')

for day, calories in zip(data['Day'], data['Calories_Burned']):
    if day == 15:  
        plt.text(day, calories, f"{calories} cal", fontsize=9, ha='center')

plt.title('Daily Calories Burned Trend over a Month', fontsize=20, pad=20)
plt.xlabel('Day of the Month', fontsize=14)
plt.ylabel('Calories Burned (cal)', fontsize=14)

plt.show()