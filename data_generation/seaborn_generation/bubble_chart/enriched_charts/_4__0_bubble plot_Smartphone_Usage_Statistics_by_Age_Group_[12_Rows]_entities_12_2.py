
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Define the data as a dictionary, which then will be converted into a DataFrame
data = {
    'Age': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80],
    'Steps': [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100],
    'Calories': [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360],
    'Count': [5, 6, 7, 8, 9, 10, 12, 14, 15, 17, 20, 22, 25, 28, 30, 32, 35, 37, 40, 42, 45, 50, 55, 60, 65, 70, 75]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Creating the bubble chart
plt.figure(figsize=(16, 12))
bubble_chart = sns.scatterplot(data=df, x='Age', y='Steps', hue='Calories', size='Count', sizes=(50, 1500),
                               palette=['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#33FFF3', '#FFC733'])

# Customize the axes and title
bubble_chart.set_title('Steps and Calories Burned by Age', fontsize=20, pad=20)
bubble_chart.set_xlabel('Age (Years)', fontsize=16)
bubble_chart.set_ylabel('Steps Taken Per Day', fontsize=16)

# Show the plot
plt.show()