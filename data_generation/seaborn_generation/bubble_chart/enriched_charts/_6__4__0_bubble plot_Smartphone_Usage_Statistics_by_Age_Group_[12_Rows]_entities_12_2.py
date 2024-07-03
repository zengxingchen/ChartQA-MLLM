
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {
    'Age': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80],
    'Temperature': [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41],
    'Humidity': [85, 83, 80, 78, 75, 73, 70, 68, 65, 63, 60, 58, 55, 53, 50, 48, 45, 43, 40, 38, 35, 33, 30, 28, 25, 23, 20],
    'Count': [4, 5, 6, 7, 8, 10, 12, 14, 15, 17, 20, 22, 25, 28, 30, 32, 35, 37, 40, 42, 45, 50, 55, 60, 65, 70, 75]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 10))
bubble_chart = sns.scatterplot(data=df, x='Age', y='Temperature', hue='Humidity', size='Count', sizes=(50, 1500),
                               palette=['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#33FFF3', '#FFC733'])

bubble_chart.set_title('Temperature and Humidity by Age', fontsize=20, pad=20)
bubble_chart.set_xlabel('Age (Years)', fontsize=16)
bubble_chart.set_ylabel('Temperature (°C)', fontsize=16)

plt.show()