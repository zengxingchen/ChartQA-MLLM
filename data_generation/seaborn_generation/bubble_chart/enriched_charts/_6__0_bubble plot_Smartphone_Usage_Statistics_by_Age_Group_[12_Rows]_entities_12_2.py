
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Define the data as a dictionary, which then will be converted into a DataFrame
data = {
    'Age': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80],
    'Exercise_Hours': [0.5, 0.8, 1, 1.2, 1.5, 1.8, 2, 2.2, 2.5, 2.8, 3, 3.2, 3.5, 3.8, 4, 4.2, 4.5, 4.8, 5, 5.2, 5.5, 6, 6.5, 7, 7.5, 8, 8.5],
    'Stress_Level': [2, 3, 3.5, 4, 4.2, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.2, 8.5, 9, 9.2, 9.5, 9.8, 10, 10.5, 11, 12, 13, 13.5, 14, 15],
    'Count': [5, 6, 7, 8, 9, 10, 12, 14, 15, 17, 20, 22, 25, 28, 30, 32, 35, 37, 40, 42, 45, 50, 55, 60, 65, 70, 75]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Creating the bubble chart
plt.figure(figsize=(16, 12))
bubble_chart = sns.scatterplot(data=df, x='Age', y='Exercise_Hours', hue='Stress_Level', size='Count', sizes=(20, 1000),
                               palette=['#FF6347', '#4682B4', '#9ACD32', '#DA70D6', '#20B2AA', '#FF4500'])

# Customize the axes and title
bubble_chart.set_title('Exercise Hours and Stress Levels by Age', fontsize=20, pad=20)
bubble_chart.set_xlabel('Age (Years)', fontsize=16)
bubble_chart.set_ylabel('Exercise Hours (Per Week)', fontsize=16)

# Show the plot
plt.show()