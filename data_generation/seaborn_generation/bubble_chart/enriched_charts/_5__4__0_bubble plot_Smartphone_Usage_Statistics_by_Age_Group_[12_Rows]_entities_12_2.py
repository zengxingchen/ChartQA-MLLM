
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {
    'Age': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],
    'Daily_Intake': [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350],
    'Calories': [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],
    'Benefit_Score': [10, 12, 14, 16, 18, 20, 22, 25, 28, 30, 32, 35, 37, 40, 42, 45, 48, 50, 52, 55, 57, 60, 62, 65, 68, 70]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 10))
bubble_chart = sns.scatterplot(data=df, x='Age', y='Daily_Intake', hue='Calories', size='Benefit_Score', sizes=(50, 1500),
                               palette=['#FFA07A', '#20B2AA', '#778899', '#FF6347', '#4682B4', '#FFD700'])

bubble_chart.set_title('Daily Nutrient Intake and Calories by Age', fontsize=20, pad=20)
bubble_chart.set_xlabel('Age (Years)', fontsize=16)
bubble_chart.set_ylabel('Daily Nutrient Intake (grams)', fontsize=16)

plt.legend(loc='upper right', bbox_to_anchor=(1.25, 1))
plt.show()